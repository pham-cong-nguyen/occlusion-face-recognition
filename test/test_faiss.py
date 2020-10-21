import os, time
import json
import numpy as np
import tensorflow as tf
import pickle
import faiss
import matplotlib.pyplot as plt
from PIL import Image
from sklearn import preprocessing
from sklearn.metrics import confusion_matrix
from absl import app, flags, logging
from absl.flags import FLAGS

from tensorflow.keras.models import Model, model_from_json, Sequential
from tensorflow.keras.layers import Multiply, Input, BatchNormalization, Dropout, Flatten,\
                                     Dense, Subtract, Reshape, Concatenate

from modules.evaluations import expand2square, calculate_accuracy,\
                                get_gallery_pr2, get_probe_pr2
from modules.utils import split, load_yaml
from modules.models import ArcFaceModel

os.environ['CUDA_VISIBLE_DEVICES'] = '-1'

flags.DEFINE_string('cfg_path', './configs/arc_res50_mask.yaml', 'config file path')

def main():
    # with open('/home/anhdq23/Desktop/nguyen/VT_simulation/weights/arcface_ret50.json', 'r') as f:
    #     model_json = json.load(f)
    # model = model_from_json(model_json)
    # model.load_weights('/home/anhdq23/Desktop/nguyen/VT_simulation/weights/arcface_ret50.h5')

    cfg = load_yaml('./configs/arc_res50_mask.yaml')
    model = ArcFaceModel(size=cfg['input_size'],
                         backbone_type=cfg['backbone_type'],
                         num_classes=cfg['num_classes'],
                         head_type=cfg['head_type'],
                         embd_shape=cfg['embd_shape'],
                         w_decay=cfg['w_decay'],
                         training=False)
    ckpt_path = tf.train.latest_checkpoint('./checkpoints/' + cfg['sub_name'])
    if ckpt_path is not None:
        print("[*] load ckpt from {}".format(ckpt_path))
        model.load_weights(ckpt_path)
    else:
        print("[*] training from scratch.")

    resnet_model = tf.keras.Model(inputs=model.get_layer('resnet50').input,
                                    outputs=model.get_layer('resnet50').output)
    resnet_head = tf.keras.Model(inputs=resnet_model.input,
                                    outputs=resnet_model.get_layer('conv2_block1_add').output)
    resnet_tail = split(resnet_model, 18, 1000) # conv2_block1_out
    output_model = tf.keras.Model(inputs=model.get_layer('OutputLayer').input,
                                    outputs=model.get_layer('OutputLayer').output)

    temp1 = np.ones((62,112,3))
    temp2 = np.zeros((50,112,3))
    masked_img = np.concatenate([temp1, temp2], axis =0)

    path_to_data = '/home/anhdq23/Desktop/nguyen/data/AR/test2'
    anchor_names = list(get_gallery_pr2(path_to_data)) # From 1 to 100
    name_dicts = get_probe_pr2(path_to_data) # Dictionary: {anchor_name:[name_image, ...]}

    dist_all = []
    labels_ARface = []
    for subject in np.arange(100):
        tmp = np.zeros((600,))
        tmp[subject*6: subject*6+6] += 1
        labels_ARface.extend(list(tmp))
    labels_ARface = np.array(labels_ARface)

    database_image_names = []
    database_feature_list = []

    for anchor_name in anchor_names:
        # Woman
        if anchor_name == 'W-042-01.bmp':
            anchor_name = 'W-042-14.bmp'
        if anchor_name == 'W-028-01.bmp':
            anchor_name = 'W-028-14.bmp'
        if anchor_name == 'W-025-01.bmp':
            anchor_name = 'W-025-14.bmp'
        if anchor_name == 'W-016-01.bmp': #for W7
            anchor_name = 'W-016-16.bmp'
        if anchor_name == 'W-003-01.bmp':
            anchor_name = 'W-003-14.bmp'
        if anchor_name == 'W-050-01.bmp':
            anchor_name = 'W-050-03.bmp'
        if anchor_name == 'W-012-01.bmp':
            anchor_name = 'W-012-03.bmp'
        
        # Man
        if anchor_name == 'M-009-01.bmp':
            anchor_name = 'M-009-14.bmp'
        if anchor_name == 'M-018-01.bmp':
            anchor_name = 'M-018-14.bmp'
        if anchor_name == 'M-028-01.bmp':
            anchor_name = 'M-028-02.bmp'
        if anchor_name == 'M-043-01.bmp':
            anchor_name = 'M-043-15.bmp'
        if anchor_name == 'M-048-01.bmp':
            anchor_name = 'M-048-14.bmp'
        

        img1 = Image.open(os.path.join(path_to_data, anchor_name))
        # img1 = expand2square(img1, (255, 255, 255))
        img1 = img1.resize((112, 112))
        img1 = np.array(img1)/255.0
        img1 = np.multiply(img1, masked_img)

        fc1 = resnet_head.predict(img1.reshape((1,112,112,3)))
        fc1 = resnet_tail.predict(fc1)
        fc1 = output_model.predict(fc1)
        norm_fc1 = preprocessing.normalize(fc1.reshape((1,512)), norm='l2', axis=1)
        database_image_names.append(anchor_name)
        database_feature_list.append(norm_fc1)

    print(np.array(database_feature_list).shape, database_feature_list[0].shape)
    # Init faiss
    res = faiss.StandardGpuResources()  # use a single GPU
    index_flat = faiss.IndexFlatL2(512)
    # gpu_index_flat = faiss.index_cpu_to_gpu(res, 0, index_flat)
    gpu_index_flat = index_flat
    gpu_index_flat.add(np.array(database_feature_list).reshape((-1,512)))  # add vectors to the index

    count =0
    for key in list(name_dicts.keys()):
        print(key)
        for name in name_dicts[key]:
            img2 = Image.open(os.path.join(path_to_data, name)).resize((112, 112))
            img2 = img2.resize((112, 112))
            img2 = np.array(img2)/255.0
            img2 = np.multiply(img2, masked_img)

            fc2 = resnet_head.predict(img2.reshape((1,112,112,3)))
            fc2 = resnet_tail.predict(fc2)
            fc2 = output_model.predict(fc2)
            norm_fc2 = preprocessing.normalize(fc2.reshape((1,512)), norm='l2', axis=1)

            D, I = gpu_index_flat.search(norm_fc2, k=1)  # actual search
            print(name, database_image_names[I[0][0]])
            if name[0:5] == database_image_names[I[0][0]][0:5]:
                count +=1
    print(count)

    plt.plot(dist_all)
    plt.show()
    thresholds = np.arange(0, 1, 0.01)
    tpr_all = []
    fpr_all = []
    for thr in thresholds:
        tpr, fpr, acc, f1 = calculate_accuracy(thr, np.array(dist_all), labels_ARface)
        top_left = np.sqrt((1-tpr)**2 + fpr**2)
        print('thr %.4f' % thr , 'tpr %.4f' % tpr, 'fpr %.4f' % fpr, \
        'top left %.4f' % top_left, 'acc %.4f' % acc, 'f1_score %.4f'%f1)
        # top_left_batch.append(top_left)
        tpr_all.append(tpr)
        fpr_all.append(fpr)

    for threshold in thresholds:
        predict_issame = np.less(np.array(dist_all), threshold)
        conf_matrix = confusion_matrix(labels_ARface, predict_issame)
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

#arcres50: ARface: thr 0.5100 tpr 0.7517 fpr 0.0009 top left 0.2483 acc 0.9967 f1_score 0.8178
#mbv2: ARface thr 0.4600 tpr 0.6683 fpr 0.0012 top left 0.3317 acc 0.9954 f1_score 0.7460
#occ-arcres50: thr 0.5300 tpr 0.7967 fpr 0.0005 top left 0.2033 acc 0.9974 f1_score 0.8613