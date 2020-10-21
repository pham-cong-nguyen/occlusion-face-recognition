import yaml
import numpy as np
import tensorflow as tf
from absl import logging
import imgaug.augmenters as iaa
from tensorflow.keras.models import Model


def set_memory_growth():
    gpus = tf.config.experimental.list_physical_devices('GPU')
    if gpus:
        try:
            # Currently, memory growth needs to be the same across GPUs
            for gpu in gpus:
                tf.config.experimental.set_memory_growth(gpu, True)
                logical_gpus = tf.config.experimental.list_logical_devices(
                    'GPU')
                logging.info(
                    "Detect {} Physical GPUs, {} Logical GPUs.".format(
                        len(gpus), len(logical_gpus)))
        except RuntimeError as e:
            # Memory growth must be set before GPUs have been initialized
            # logging.info(e)
            print("No GPU")


def load_yaml(load_path):
    """load yaml file"""
    with open(load_path, 'r') as f:
        loaded = yaml.load(f, Loader=yaml.Loader)

    return loaded


def get_ckpt_inf(ckpt_path, steps_per_epoch):
    """get ckpt information"""
    split_list = ckpt_path.split('e_')[-1].split('_b_')
    epochs = int(split_list[0])
    batchs = int(split_list[-1].split('.ckpt')[0])
    steps = (epochs - 1) * steps_per_epoch + batchs

    return epochs, steps + 1


def l2_norm(x, axis=1):
    """l2 norm"""
    norm = np.linalg.norm(x, axis=axis, keepdims=True)
    output = x / norm

    return output

class ImgAugTransform:
    def __init__(self):
        self.aug = iaa.Sequential([
            iaa.Sometimes(0.15, iaa.MotionBlur(k=5, angle=[-45, 45])),
            iaa.Sometimes(0.35,
                          iaa.OneOf([iaa.MultiplyAndAddToBrightness(mul=(0.5, 1.5), add=(-30, 30)),
                                     iaa.GammaContrast(gamma=(0.7, 1.75)),
                                     iaa.pillike.Autocontrast(cutoff=(0, 15.0)),
                                     iaa.Sometimes(0.25, iaa.GaussianBlur(sigma=(0, 1.3)))
                                     ])),
            iaa.Fliplr(0.5),
            iaa.Sometimes(0.35,
                          iaa.OneOf([
                                     iaa.SaltAndPepper(0.05),
                                     iaa.Affine(rotate=(-20, 20), mode='symmetric')
                                     ]))
        ])

    def __call__(self, img):
        # img = np.array(img, dtype=np.uint8)
        return self.aug.augment_image(img)

'''
    brief:  get sub_model from start_layer to end_layer
    Input:
        1, model: tf.keras.model.Model
        2, start: index of start layer in original model
        3, end: index of end layer in original model
    Output:
        1, Sub_model: tf.keras.model.Model
'''
def split(model, start, end):
    confs = model.get_config()
    kept_layers = set()
    for i, l in enumerate(confs['layers']):
        if i == 0:
            confs['layers'][0]['config']['batch_input_shape'] = model.layers[start].input_shape
            if i != start:
                # confs['layers'][0]['name'] += str(random.randint(0, 100000000)) 
                confs['layers'][0]['config']['name'] = confs['layers'][0]['name']
        elif i < start or i > end:
            continue
        kept_layers.add(l['name'])
    # filter layers
    layers = [l for l in confs['layers'] if l['name'] in kept_layers]
    layers[1]['inbound_nodes'][0][0][0] = layers[0]['name']
    # set conf
    confs['layers'] = layers
    confs['input_layers'][0][0] = layers[0]['name']
    confs['output_layers'][0][0] = layers[-1]['name']
    # create new model
    submodel = Model.from_config(confs)
    for l in submodel.layers:
        orig_l = model.get_layer(l.name)
        if orig_l is not None:
            l.set_weights(orig_l.get_weights())
    return submodel