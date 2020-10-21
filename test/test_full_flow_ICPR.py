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

os.environ['CUDA_VISIBLE_DEVICES'] = '0'
flags.DEFINE_string('cfg_path', './configs/arc_res50_new.yaml', 'config file path')
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

    import sys
    sys.path.append('/home/anhdq23/Desktop/nguyen/VT_simulation/')
    from detector import get_detector
    predictor = get_detector()

    ICPR_dict = dict()
    path_ICPR = '/home/anhdq23/Desktop/nguyen/data/ICPR_cropped_face'
    for name_fold in os.listdir(path_ICPR):
        print(name_fold)
        path_fold = os.path.join(path_ICPR, name_fold)
        if name_fold not in ICPR_dict.keys():
            ICPR_dict[name_fold] = []
        for name_image in os.listdir(path_fold):
            path_image = os.path.join(path_fold, name_image)
            if '60' not in name_image[-10:-4] and '90' not in name_image[-10:-4]\
                and '75' not in name_image[-10:]:
                image = Image.open(path_image)
                image = expand2square(image, (255, 255, 255))
                image = image.resize((112, 112))
                image = np.array(image)/255.0 
                _, labels, _ = predictor.predict(image, 1500/2, 0.6) 
                if labels.numpy()[0] == 1:
                    fc1 = model_mask.predict(image.reshape((1,112,112,3)))
                    norm_fc1 = preprocessing.normalize(fc1.reshape((1,cfg['embd_shape'])), norm='l2', axis=1)

                else:
                    fc1 = model.predict(image.reshape((1,112,112,3)))
                    norm_fc1 = preprocessing.normalize(fc1.reshape((1,cfg['embd_shape'])), norm='l2', axis=1)
                ICPR_dict[name_fold].append(norm_fc1)

    path_ICPR = '/home/anhdq23/Desktop/nguyen/data/ICPR_cropped_face'
    anchor_list = []
    name_list = []
    for name_fold in os.listdir(path_ICPR):
        print(name_fold)
        path_fold = os.path.join(path_ICPR, name_fold)
        for name_image in os.listdir(path_fold):
            path_image = os.path.join(path_fold, name_image)
            if '+0+0' in name_image[-10:] or '+0-15' in name_image[-10:] or\
            '+0+15' in name_image[-10:] or '+15+0' in name_image[-10:] or\
            '-15+0' in name_image[-10:]:
                print(name_image)
                image = Image.open(path_image)
                image = expand2square(image, (255, 255, 255))
                image = image.resize((112, 112))
                image = np.array(image)/255.0 
                _, labels, _ = predictor.predict(image, 1500/2, 0.6) 
                if labels.numpy()[0] == 1:
                    fc1 = model_mask.predict(image.reshape((1,112,112,3)))
                    norm_fc1 = preprocessing.normalize(fc1.reshape((1,cfg['embd_shape'])), norm='l2', axis=1)

                else:
                    fc1 = model.predict(image.reshape((1,112,112,3)))
                    norm_fc1 = preprocessing.normalize(fc1.reshape((1,cfg['embd_shape'])), norm='l2', axis=1)
                
                anchor_list.append(norm_fc1)
                name_list.append(name_fold)

    # Init faiss
    import faiss
    count_true = 0
    count_all = 0 
    res = faiss.StandardGpuResources()  # use a single GPU
    index_flat = faiss.IndexFlatL2(512)
    # gpu_index_flat = faiss.index_cpu_to_gpu(res, 0, index_flat)
    gpu_index_flat = index_flat
    gpu_index_flat.add(np.array(anchor_list).reshape((-1,512)))
    for key in list(ICPR_dict.keys()):
        for feature in ICPR_dict[key]:
            D, I = gpu_index_flat.search(feature, k=1)  # actual search
            print(key, name_list[I[0][0]])
            if key == name_list[I[0][0]]:
                count_true +=1
            count_all +=1
    print(count_true, count_all)

if __name__ == "__main__":
    main()