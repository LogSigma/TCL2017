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
