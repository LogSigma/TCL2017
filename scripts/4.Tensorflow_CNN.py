import os
import numpy as np
import pandas as pd
import scipy as sp
import skimage as ski
from skimage import filters, transform
import matplotlib.pyplot as plt
import itertools as it
from glob import glob
import tensorflow as tf
from sklearn import model_selection
from skimage.measure import ransac, CircleModel, LineModelND
from skimage.restoration import denoise_tv_chambolle, denoise_bilateral, denoise_wavelet

data = bad_data + good_data
print('Bad & Good : %s' % len(data))
