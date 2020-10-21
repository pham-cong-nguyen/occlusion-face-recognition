from absl import app, flags, logging
from absl.flags import FLAGS
import os, json
import tensorflow as tf
import bcolz
import numpy as np
import tqdm
import matplotlib.pyplot as plt
from PIL import Image
from sklearn import preprocessing

from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input

from modules.models import ArcFaceModel
from modules.losses import SoftmaxLoss
from modules.utils import set_memory_growth, load_yaml, get_ckpt_inf,\
                            split, ImgAugTransform
from modules.evaluations import get_gallery_pr2, get_probe_pr2
import modules.dataset as dataset


os.environ['CUDA_VISIBLE_DEVICES'] = '0'
flags.DEFINE_string('cfg_path', './configs/arc_res50_mix.yaml', 'config file path')
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
    learning_rate = tf.constant(cfg['base_lr'])
    optimizer = tf.keras.optimizers.SGD(
                    learning_rate=learning_rate, momentum=0.9, nesterov=True)
    loss_fn = SoftmaxLoss()

    ckpt_path = tf.train.latest_checkpoint('./checkpoints/train_' + cfg['sub_name'])
    if ckpt_path is not None:
        print("[*] load ckpt from {}".format(ckpt_path))
        model.load_weights(ckpt_path)
    else:
        print("[*] training from scratch.")
    model.compile(optimizer=optimizer, loss=loss_fn)
    

    # resnet_model = tf.keras.Model(inputs=model.get_layer('resnet50').input,
    #                                 outputs=model.get_layer('resnet50').output)
    # resnet_head = tf.keras.Model(inputs=resnet_model.input,
    #                                 outputs=resnet_model.get_layer('conv2_block1_add').output)
    # resnet_tail = split(resnet_model, 18, 1000) # conv2_block1_out
    # output_model = tf.keras.Model(inputs=model.get_layer('OutputLayer').input,
    #                                 outputs=model.get_layer('OutputLayer').output)
    # archead = tf.keras.Model(inputs=model.get_layer('ArcHead').input,
    #                                 outputs=model.get_layer('ArcHead').output)

    temp1 = np.ones((62,112,3))
    temp2 = np.zeros((50,112,3))
    masked_img = np.concatenate([temp1, temp2], axis =0).reshape(1,112,112,3)

    temp1 = np.ones((1,18,28,256))
    temp2 = np.zeros((1,10,28,256))
    masked = np.concatenate([temp1, temp2], axis =1)
    # inputs = Input((112, 112, 3))
    # labels = Input([])
    # s = resnet_head(inputs)
    # s = tf.keras.layers.Multiply()([s, tf.constant(masked, dtype=tf.float32)])
    # s = resnet_tail(s)
    # s = output_model(s)
    # s = archead([s, labels])
    # new_model = Model((inputs, labels), s)
    # new_model.summary()

    # new_model.compile(optimizer=optimizer, loss=loss_fn)

    path_to_data = '/home/anhdq23/Desktop/nguyen/data/AR/test2'
    anchor_names = get_gallery_pr2(path_to_data) # From 1 to 100
    name_dicts = get_probe_pr2(path_to_data) # Dictionary: {anchor_name:[name_image, ...]}

    augment = ImgAugTransform()
    import faiss

    if FLAGS.mode == 'eager_tf':
        top_left_all = [0.012]
        best_acc = 0.8
        for epochs in range(cfg['epochs']):
            logging.info("Shuffle ms1m dataset.")
            dataset_len = cfg['num_samples']
            steps_per_epoch = dataset_len // cfg['batch_size']
            train_dataset = dataset.load_tfrecord_dataset(
                    cfg['train_dataset'], cfg['batch_size'], cfg['binary_img'],
                    is_ccrop=cfg['is_ccrop'])
            
            sub_train_dataset = dataset.load_tfrecord_dataset(
                    cfg['train_dataset'], cfg['batch_size'], cfg['binary_img'],
                    is_ccrop=cfg['is_ccrop'])

            for batch, ((x,y) ,(sub_x, sub_y)) in enumerate(zip(train_dataset, sub_train_dataset)):
                x0_new = np.array(x[0], dtype=np.uint8)
                x1_new = np.array(x[1], dtype=np.float32)
                for i in np.arange(len(x0_new)):
                    x0_new[i] = augment(x0_new[i])
                temp =  np.array(x0_new, dtype=np.float32)/255.0
                temp = np.multiply(temp, masked_img)

                sub_x0_new = np.array(sub_x[0], dtype=np.uint8)
                sub_x1_new = np.array(sub_x[1], dtype=np.float32)
                for i in np.arange(len(sub_x0_new)):
                    sub_x0_new[i] = augment(sub_x0_new[i])
                sub_temp =  np.array(sub_x0_new, dtype=np.float32)/255.0
                
                model.train_on_batch(*((sub_temp, sub_x1_new), sub_x1_new))
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
                        
                        database_image_names = []
                        database_feature_list = []
                        for anchor_name in anchor_names:
                            img1 = Image.open(os.path.join(path_to_data, anchor_name))
                            img1 = img1.resize((112, 112))
                            img1 = np.array(img1)/255.0
                            img1 = np.multiply(img1, masked_img)

                            fc1 = resnet_model.predict(img1.reshape((1,112,112,3)))
                            fc1 = output_model.predict(fc1)
                            norm_fc1 = preprocessing.normalize(fc1.reshape((1,512)), norm='l2', axis=1)
                            database_image_names.append(anchor_name)
                            database_feature_list.append(norm_fc1)

                        index_flat = faiss.IndexFlatL2(512)
                        gpu_index_flat = index_flat
                        gpu_index_flat.add(np.array(database_feature_list).reshape((-1,512)))  # add vectors to the index
                        count =0
                        for key in list(name_dicts.keys()):
                            for name in name_dicts[key]:
                                img2 = Image.open(os.path.join(path_to_data, name)).resize((112, 112))
                                img2 = img2.resize((112, 112))
                                img2 = np.array(img2)/255.0
                                img2 = np.multiply(img2, masked_img)

                                fc2 = resnet_model.predict(img2.reshape((1,112,112,3)))
                                fc2 = output_model.predict(fc2)
                                norm_fc2 = preprocessing.normalize(fc2.reshape((1,512)), norm='l2', axis=1)

                                D, I = gpu_index_flat.search(norm_fc2, k=1)  # actual search
                                if name[0:5] == database_image_names[I[0][0]][0:5]:
                                    count +=1
                        acc = count/600.0
                        if acc > best_acc:
                            best_acc = acc
                            print('[*] save ckpt file!')
                            model.save_weights('checkpoints/{}/e_{}_b_{}.ckpt'.format(
                                cfg['sub_name'], epochs, batch % steps_per_epoch))
                        print("The current acc: {:.6f} ".format(acc))
                        print("The best acc: {:.6f} ".format(best_acc))

                    model.save_weights('checkpoints/train_{}/{}.ckpt'.format(
                            cfg['sub_name'], cfg['sub_name']))


if __name__ == '__main__':
    app.run(main)
