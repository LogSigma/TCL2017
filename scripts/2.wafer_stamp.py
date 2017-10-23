import os
from os import path
import scipy as sp
import itertools as it

from PIL import Image, ImageOps
from glob import glob

path_stamp = "./data/stamp"

def flip_and_rotator(marked, axis=None, angle=0):
  
  flip_axis = {'vertical' : lambda x: x[:,::-1],
