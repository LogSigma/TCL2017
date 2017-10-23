import os
from os import path
import numpy as np
import pandas as pd
from PIL import Image, ImageOps

path_src = "./data/txt"
path_out = "./data/imp"
abspath_src = path.abspath(path_src)
abspath_out = path.abspath(path_out)

file_paths = [path.join(abspath_src, name) for name in os.listdir(path_src) if path.isfile(path.join(abspath_src, name))]
#file = file_paths[1]

for file in file_paths:
  data = np.genfromtxt(file, delimiter=';', dtype=None)
  coordinates = data[data[:,4]==b'W'][:,2:4].astype(np.uint8)
  array = np.zeros(shape=(50,70), dype=np.uint8)
  array[coordinates[:,1], coordinates[:,0]] = 1
  
  wafer = array.astype(np.float64)
  for __ in range(0,49):
    for _ in range(0,69):
      wafer[__,_] = (1/11)*array[__-1,__-1] +(1/11)*array[__-1,_]
