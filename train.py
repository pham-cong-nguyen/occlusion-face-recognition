from absl import app, flags, logging
from absl.flags import FLAGS
import os, json
import tensorflow as tf
import bcolz
import numpy as np
import tqdm
import matplotlib.pyplot as plt

from modules.models import ArcFaceModel
from modules.losses import SoftmaxLoss
from modules.utils import set_memory_growth, load_yaml, get_ckpt_inf
import modules.dataset as dataset

from sklearn import preprocessing
from modules.utils import ImgAugTransform
from modules.evaluations import expand2square, calculate_accuracy,\
                                get_gallery_pr2, get_probe_pr2, get_val_pair
from modules.utils import split, load_yaml

os.environ['CUDA_VISIBLE_DEVICES'] = '0'
flags.DEFINE_string('cfg_path', './configs/arc_res50_new.yaml', 'config file path')
flags.DEFINE_string('gpu', '0', 'which gpu to use')
flags.DEFINE_enum('mode', 'fit', ['fit', 'eager_tf'],
                  'fit: model.fit, eager_tf: custom GradientTape')


def main(_):
    set_memory_growth()

    cfg = load_yaml(FLAGS.cfg_path)
    model = ArcFaceModel(size=cfg['input_size'],
                         backbone_type=cfg['backbone_type'],
                         num_classes=cfg['num_classes'],
                         head_type=cfg['head_type'],
                         embd_shape=cfg['embd_shape'],
                         w_decay=cfg['w_decay'],
                         training=True)
    model.summary()

    learning_rate = tf.constant(cfg['base_lr'])
    optimizer = tf.keras.optimizers.SGD(
                    learning_rate=learning_rate, momentum=0.9, nesterov=True)
    loss_fn = SoftmaxLoss()
    ckpt_path = tf.train.latest_checkpoint('./checkpoints/' + cfg['sub_name'])
    if ckpt_path is not None:
        print("[*] load ckpt from {}".format(ckpt_path))
        model.load_weights(ckpt_path)
    else:
        print("[*] training from scratch.")

    model.compile(optimizer=optimizer, loss=loss_fn)

    data_path = 'data'
    lfw, lfw_issame = get_val_pair(data_path, 'lfw_align_112/lfw')
    lfw = np.transpose(lfw, [0, 2, 3, 1]) * 0.5 + 0.5
    
    image_1 = lfw[0::2]
    image_2 = lfw[1::2]

    augment = ImgAugTransform()
    if FLAGS.mode == 'eager_tf':
        top_left_all = [0.008807]
        for epochs in range(cfg['epochs']):
            logging.info("Shuffle ms1m dataset.")
            dataset_len = cfg['num_samples']
            steps_per_epoch = dataset_len // cfg['batch_size']
            train_dataset = dataset.load_tfrecord_dataset(
                    cfg['train_dataset'], cfg['batch_size'], cfg['binary_img'],
                    is_ccrop=cfg['is_ccrop'])

            for batch, (x,y) in enumerate(train_dataset):
                x0_new = np.array(x[0], dtype=np.uint8)
                x1_new = np.array(x[1], dtype=np.float32)
                for i in np.arange(len(x0_new)):
                    x0_new[i] = augment(x0_new[i])
                temp =  np.array(x0_new, dtype=np.float32)/255.0
                
                loss = model.train_on_batch(*((temp, x1_new), x1_new))
                
                if batch % 50 == 0:
                    verb_str = "Epoch {}/{}: {}/{}, loss={:.6f}, lr={:.6f}"
                    print(verb_str.format(epochs, cfg['epochs'],
                                        batch,
                                        steps_per_epoch, loss,
                                        cfg['base_lr']/(1.0+cfg['w_decay']*(epochs*45489+batch))))

                    if batch % cfg['save_steps'] == 0:
                        resnet_model = tf.keras.Model(inputs=model.get_layer('resnet50').input,
                                                        outputs=model.get_layer('resnet50').output)

                        output_model = tf.keras.Model(inputs=model.get_layer('OutputLayer').input,
                                                        outputs=model.get_layer('OutputLayer').output)
                        
                        dist_all = []
                        top_left_batch = []
                        for idx in range(0, len(lfw_issame), cfg['batch_size']):
                            tem = resnet_model.predict(image_1[idx:idx + cfg['batch_size']])
                            embeds_1 = output_model.predict(tem)
                            norm_embeds_1 =  preprocessing.normalize(embeds_1, norm='l2', axis=1)
                            
                            tem = resnet_model.predict(image_2[idx:idx + cfg['batch_size']])
                            embeds_2 = output_model.predict(tem)
                            norm_embeds_2 =  preprocessing.normalize(embeds_2, norm='l2', axis=1)

                            diff = np.subtract(norm_embeds_1, norm_embeds_2)
                            dist = np.sqrt(np.sum(np.square(diff), 1))/2
                            dist_all.extend(dist)

                        thresholds = np.arange(0, 1, 0.01)
                        for thr in thresholds:
                            tpr, fpr, _ = calculate_accuracy(thr, np.array(dist_all), lfw_issame)
                            top_left = np.sqrt((1-tpr)**2 + fpr**2)
                            top_left_batch.append(top_left)
                        print("The current top left: {:.6f}     Threshold: {:.2f}".format(np.min(top_left_batch), 0.01*np.argmin(top_left_batch)))
                        
                        if not len(top_left_all):
                            print("The best top left: {:.6f}     Threshold: {:.2f}".format(np.min(top_left_batch), 0.01*np.argmin(top_left_batch)))
                        else:
                            print("The best top left: {:.6f}".format(top_left_all[-1]))
                        
                        if not len(top_left_all):
                            top_left_all.append(np.min(top_left_batch))
                            print('[*] save ckpt file!')
                            model.save_weights('checkpoints/{}/e_{}_b_{}.ckpt'.format(
                                cfg['sub_name'], epochs, batch % steps_per_epoch))

                        elif top_left_all[-1] > np.min(top_left_batch):
                            top_left_all.append(np.min(top_left_batch))
                            print('[*] save ckpt file!')
                            model.save_weights('checkpoints/{}/e_{}_b_{}.ckpt'.format(
                                cfg['sub_name'], epochs, batch % steps_per_epoch))
                            
                    model.save_weights('checkpoints/train_{}/{}.ckpt'.format(
                            cfg['sub_name'], cfg['sub_name']))

if __name__ == '__main__':
    app.run(main)
