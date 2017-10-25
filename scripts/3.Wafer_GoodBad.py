import os
import numpy as np
import pandas as pd
import scipy as sp
import skimage as ski

from skimage import filters, transform
import matplotlib.pyplot as plt
import itertools as it

good_path_src = "./data/good_img"
bad_path_src = "./data/bad_img"

bad_list = sorted(glob(dirname + '/' + '*.png'))
bad_data = tuple((1, sp.misc.imresize(sp.misc.imread(bad), size=(100, 100))) for bad in bad_list)
print('Bad Data : %s' % len(bad_data))

good_list = sorted(glob(dirname + '/' + '*.png'))
good_data = tuple((0, sp.misc.imresize(sp.misc.imread(good), size=(100, 100))) for good in good_list)
print('Good Data : %s' % len(good_data))
