import os
import json
import math, random
import numpy as np
import tensorflow as tf
import pickle
import matplotlib.pyplot as plt
from PIL import Image
from sklearn import preprocessing

from tensorflow.keras.models import Model, model_from_json, Sequential
from tensorflow.keras.layers import Multiply, Input, BatchNormalization, Dropout, Flatten,\
                                     Dense, Subtract, Reshape, Concatenate
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn.metrics import confusion_matrix
import bcolz

os.environ['CUDA_VISIBLE_DEVICES'] = '-1'

def get_val_pair(path, name):
    carray = bcolz.carray(rootdir=os.path.join(path, name), mode='r')
    issame = np.load('{}/{}_list.npy'.format(path, name))

    return carray, issame

def calculate_accuracy(threshold, dist, actual_issame):
    predict_issame = np.less(dist, threshold)
    tp = np.sum(np.logical_and(predict_issame, actual_issame))
    fp = np.sum(np.logical_and(predict_issame, np.logical_not(actual_issame)))
    tn = np.sum(np.logical_and(np.logical_not(predict_issame),
                            np.logical_not(actual_issame)))
    fn = np.sum(np.logical_and(np.logical_not(predict_issame), actual_issame))

    tpr = 0 if (tp + fn == 0) else float(tp) / float(tp + fn)
    fpr = 0 if (fp + tn == 0) else float(fp) / float(fp + tn)
    acc = float(tp + tn) / dist.size
    f1 = 2*float(tp) / float(2*tp + fp + fn)
    return tpr, fpr, acc, f1


from modules.models import ArcFaceModel
from absl import app, flags, logging
from absl.flags import FLAGS
from modules.utils import load_yaml

os.environ
def main():
    cfg = load_yaml('./configs/arc_res50_mask.yaml')
    model = ArcFaceModel(size=cfg['input_size'],
                         backbone_type=cfg['backbone_type'],
                         num_classes=cfg['num_classes'],
                         head_type=cfg['head_type'],
                         embd_shape=cfg['embd_shape'],
                         w_decay=cfg['w_decay'],
                         training=False)
    model.summary()

    ckpt_path = tf.train.latest_checkpoint('./checkpoints/' + cfg['sub_name'])
    if ckpt_path is not None:
        print("[*] load ckpt from {}".format(ckpt_path))
        model.load_weights(ckpt_path)
    else:
        print("[*] training from scratch.")

    temp1 = np.ones((62,112,3))
    temp2 = np.zeros((50,112,3))
    masked_img = np.concatenate([temp1, temp2], axis =0)

    path_img1 = '/home/anhdq23/Desktop/nguyen/data/AR/test2/M-002-12.bmp'
    path_img2 = '/home/anhdq23/Desktop/nguyen/data/AR/test2/M-003-01.bmp'
    img1 = Image.open(path_img1)
    img1 = img1.resize((112, 112))
    img1 = np.array(img1)/255.0
    

    img2 = Image.open(path_img2)
    img2 = img2.resize((112, 112))
    img2 = np.array(img2)/255.0 
    mask_img2 = np.multiply(img2, masked_img)

    fc1 = model.predict(mask_img2.reshape((1,112,112,3)))
    norm_fc1 = preprocessing.normalize(fc1.reshape((1,512)), norm='l2', axis=1)

    fc2 = model.predict(img2.reshape((1,112,112,3)))
    norm_fc2 = preprocessing.normalize(fc2.reshape((1,512)), norm='l2', axis=1)
    
    diff = np.subtract(norm_fc1, norm_fc2)
    dist = np.sqrt(np.sum(np.square(diff), 1))/2
    print(dist)
    
    for i in np.arange(20):
        print(np.sqrt(np.sum(np.square(diff[0][i*25:i*25+25]), 0))/2)

    fig = plt.figure()
    ax = fig.add_subplot(2,1,1)
    ax.plot(np.arange(512), norm_fc1[0])

    # ax = fig.add_subplot(2,1,2)
    ax.plot(np.arange(512), norm_fc2[0])
    ax = fig.add_subplot(2,1,2)
    ax.plot(np.arange(512), diff[0])
    plt.show()

if __name__ == "__main__":
    main()

'''
M-001-13, M-001-01
10,  13,  44,  60,  65,  71,  81, 136, 143, 152, 164, 183, 194,
       217, 226, 266, 286, 324, 360, 362, 392, 394, 404, 418, 419, 444,
       445, 446, 457, 466, 487, 500, 509'''

'''
M-001-12, M-001-01
13,  65,  67,  71,  74,  87, 113, 194, 261, 271, 292, 401, 404
'''

'''
M-001-11, M-001-01
13,  65,  71,  74,  89, 376, 446
'''

'''
M-001-24, M-001-01
 13,  23,  34,  36,  44,  65,  74,  86,  87,  89, 109, 194, 248,
       261, 274, 324, 327, 336, 350, 355, 360, 376, 394, 413, 422, 446,
       457, 467
'''

'''
M-001-25, M-001-01
13,  34,  65,  74,  87, 112, 114, 194, 223, 271, 324, 326, 336,
       353, 369, 372, 374, 394, 409, 444, 446, 457, 500
'''

'''
M-001-26, M-001-01
13,  34,  44,  65,  71,  74,  81,  86,  87,  89, 194, 217, 261,
       271, 324, 336, 376, 392, 404, 444, 446, 457
'''

'''
M-002-13, M-002-01
 3,  15,  79,  81,  89,  93, 221, 231, 265, 295, 300, 302, 367,
       389, 405, 438, 446, 449, 459, 476, 480, 484, 494, 504, 510
'''