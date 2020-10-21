import os
import numpy as np
import bcolz
from PIL import Image

'''
    brief: Load protocol2 gallery set (1 image per identity) for AR face dataset
    Input:
        1, path_to_data
    Output:
        1, np.array of name image
'''
def get_gallery_pr2(path_to_data):
    anchor_name = []
    for file in os.listdir(path_to_data):
        bar = file.split('-')
        if bar[2] == '01.bmp':
            anchor_name.append(file)
    return np.sort(anchor_name)

'''
    brief: Load protocol2 probe set for AR face dataset
    Input:
        1, path_to_data
    Output:
        1, dictionary like {1:[M-001s-11.bmp', M-002-11.bmp',...], 2:[...]
                                                        , ..., 100:[...]}
'''
def get_probe_pr2(path_to_data):
    name_dict = {}
    # MAN images
    for man in np.arange(1, 10, 1):
        name_dict[man] = []
        name_dict[man].append('M-00%s-11.bmp'%man)
        name_dict[man].append('M-00%s-12.bmp'%man)
        name_dict[man].append('M-00%s-13.bmp'%man)
        name_dict[man].append('M-00%s-24.bmp'%man)
        name_dict[man].append('M-00%s-25.bmp'%man)
        name_dict[man].append('M-00%s-26.bmp'%man)
    for man in np.arange(10, 51, 1):
        name_dict[man] = []
        name_dict[man].append('M-0%s-11.bmp'%man)
        name_dict[man].append('M-0%s-12.bmp'%man)
        name_dict[man].append('M-0%s-13.bmp'%man)
        name_dict[man].append('M-0%s-24.bmp'%man)
        name_dict[man].append('M-0%s-25.bmp'%man)
        name_dict[man].append('M-0%s-26.bmp'%man)
    
    # WOMAN images
    for woman in np.arange(1, 10, 1):
        name_dict[woman+50] = []
        name_dict[woman+50].append('W-00%s-11.bmp'%woman)
        name_dict[woman+50].append('W-00%s-12.bmp'%woman)
        name_dict[woman+50].append('W-00%s-13.bmp'%woman)
        name_dict[woman+50].append('W-00%s-24.bmp'%woman)
        name_dict[woman+50].append('W-00%s-25.bmp'%woman)
        name_dict[woman+50].append('W-00%s-26.bmp'%woman)
    for woman in np.arange(10, 51, 1):
        name_dict[woman+50] = []
        name_dict[woman+50].append('W-0%s-11.bmp'%woman)
        name_dict[woman+50].append('W-0%s-12.bmp'%woman)
        name_dict[woman+50].append('W-0%s-13.bmp'%woman)
        name_dict[woman+50].append('W-0%s-24.bmp'%woman)
        name_dict[woman+50].append('W-0%s-25.bmp'%woman)
        name_dict[woman+50].append('W-0%s-26.bmp'%woman)
    return name_dict

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

'''
    brief: to pad a color into non-square image
    Input:
        1, pil_img: image that is needed to pad
        2, background_color: color is used to pad
    Output:
        1, Image
'''
def expand2square(pil_img, background_color):
    width, height = pil_img.size
    if width == height:
        return pil_img
    elif width > height:
        result = Image.new(pil_img.mode, (width, width), background_color)
        result.paste(pil_img, (0, (width - height) // 2))
        return result
    else:
        result = Image.new(pil_img.mode, (height, height), background_color)
        result.paste(pil_img, ((height - width) // 2, 0))
        return result