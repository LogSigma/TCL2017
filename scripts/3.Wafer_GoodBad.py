import os
import scipy as sp
from glob import glob


train_bad_path_src = "./data/train/bad_img"
train_good_path_src = "./data/train/good_img"

train_bad_list = sorted(glob(train_bad_path_src + '/' + '*.png'))
train_bad_data = tuple((1, sp.misc.imresize(sp.misc.imread(bad), size=(100, 100))) for bad in train_bad_list)
print('Bad Data : %s' % len(train_bad_data))

train_good_list = sorted(glob(train_good_path_src + '/' + '*.png'))
train_good_data = tuple((0, sp.misc.imresize(sp.misc.imread(good), size=(100, 100))) for good in train_good_list)
print('Good Data : %s' % len(train_good_data))
