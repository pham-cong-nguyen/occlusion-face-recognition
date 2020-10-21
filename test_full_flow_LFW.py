import os
import json
import numpy as np
import tensorflow as tf
import pickle
import matplotlib.pyplot as plt
from PIL import Image
from sklearn import preprocessing
from absl import app, flags, logging
from absl.flags import FLAGS

from tensorflow.keras.models import Model, model_from_json, Sequential
from tensorflow.keras.layers import Multiply, Input, BatchNormalization, Dropout, Flatten,\
                                     Dense, Subtract, Reshape, Concatenate
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn.metrics import confusion_matrix
from modules.evaluations import expand2square, calculate_accuracy,\
                                get_gallery_pr2, get_probe_pr2,\
                                get_val_pair
from modules.utils import split, load_yaml
from modules.models import ArcFaceModel

os.environ['CUDA_VISIBLE_DEVICES'] = '-1'

# flags.DEFINE_string('cfg_path', './configs/arc_res50.yaml', 'config file path')
def main():
    # with open('/home/anhdq23/Desktop/nguyen/VT_simulation/weights/arcface_ret50.json', 'r') as f:
    #     model_json = json.load(f)
    # model = model_from_json(model_json)
    # model.load_weights('/home/anhdq23/Desktop/nguyen/VT_simulation/weights/arcface_ret50.h5')
    # model.summary()
    cfg = load_yaml('./configs/arc_res50_new.yaml')
    model = ArcFaceModel(size=cfg['input_size'],
                         backbone_type=cfg['backbone_type'],
                         num_classes=cfg['num_classes'],
                         head_type=cfg['head_type'],
                         embd_shape=cfg['embd_shape'],
                         w_decay=cfg['w_decay'],
                         training=False)
    model.summary()
    ckpt_path = tf.train.latest_checkpoint('./checkpoints/' + cfg['sub_name'])
    print(ckpt_path)
    if ckpt_path is not None:
        print("[*] load ckpt from {}".format(ckpt_path))
        model.load_weights(ckpt_path)
    else:
        print("[*] training from scratch.")

    model_mask = ArcFaceModel(size=cfg['input_size'],
                    backbone_type=cfg['backbone_type'],
                    num_classes=cfg['num_classes'],
                    head_type=cfg['head_type'],
                    embd_shape=cfg['embd_shape'],
                    w_decay=cfg['w_decay'],
                    training=False)
    ckpt_path = tf.train.latest_checkpoint('./checkpoints/' + 'arc_res50_mask')
    print(ckpt_path)
    if ckpt_path is not None:
        print("[*] load ckpt from {}".format(ckpt_path))
        model_mask.load_weights(ckpt_path)
    else:
        print("[*] training from scratch.")

    data_path = '/home/anhdq23/Desktop/nguyen/arcface-tf2/data'
    lfw, lfw_issame = get_val_pair(data_path, 'lfw_align_112/lfw')
    lfw = np.transpose(lfw, [0, 2, 3, 1]) * 0.5 + 0.5

    image_1 = lfw[0::2]
    image_2 = lfw[1::2]
    
    dist_all = []
    import sys
    sys.path.append('/home/anhdq23/Desktop/nguyen/VT_simulation/')
    from detector import get_detector
    predictor = get_detector()
    for idx in range(len(lfw_issame)):
        print(idx)
        _, labels, _ = predictor.predict(image_1[idx], 1500/2, 0.6) 
        if labels.numpy()[0] == 1:
            fc1 = model_mask.predict(image_1[idx].reshape((1,112,112,3)))
            norm_fc1 = preprocessing.normalize(fc1.reshape((1,cfg['embd_shape'])), norm='l2', axis=1)

            fc2 = model_mask.predict(image_2[idx].reshape((1,112,112,3)))
            norm_fc2 = preprocessing.normalize(fc2.reshape((1,cfg['embd_shape'])), norm='l2', axis=1)
        else:
            fc1 = model.predict(image_1[idx].reshape((1,112,112,3)))
            norm_fc1 = preprocessing.normalize(fc1.reshape((1,cfg['embd_shape'])), norm='l2', axis=1)

            fc2 = model.predict(image_2[idx].reshape((1,112,112,3)))
            norm_fc2 = preprocessing.normalize(fc2.reshape((1,cfg['embd_shape'])), norm='l2', axis=1)

        # dist = tf.keras.losses.cosine_similarity(fc1.reshape((1,512)), fc2.reshape((1,512)))
        diff = np.subtract(norm_fc1, norm_fc2)
        dist = np.sqrt(np.sum(np.square(diff), 1))/2
        dist_all.extend(dist)

    plt.plot(dist_all)
    plt.show()
    thresholds = np.arange(0, 1, 0.01)

    tpr_all = []
    fpr_all = []
    for thr in thresholds:
        tpr, fpr, acc, f1 = calculate_accuracy(thr, np.array(dist_all), lfw_issame)
        top_left = np.sqrt((1-tpr)**2 + fpr**2)
        print('thr %.4f' % thr , 'tpr %.4f' % tpr, 'fpr %.4f' % fpr, \
        'top left %.4f' % top_left, 'acc %.4f' % acc, 'f1_score %.4f'%f1)
        # top_left_batch.append(top_left)
        tpr_all.append(tpr)
        fpr_all.append(fpr)

    for threshold in thresholds:
        predict_issame = np.less(np.array(dist_all), threshold)
        conf_matrix = confusion_matrix(lfw_issame, predict_issame)
        print(conf_matrix)

    plt.figure()
    lw = 2
    plt.plot(fpr_all, tpr_all, color='darkorange',
            lw=lw, label='ROC curve')
    plt.xlim([0.0, 1.])
    plt.ylim([0.0, 1.])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver operating characteristic')
    plt.legend(loc="lower right")
    plt.show()

if __name__ == "__main__":
    main()