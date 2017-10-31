import os
from os import path
import numpy as np
from PIL import Image, ImageOps

path_src = "./data/train/bad_txt"
path_out = "./data/train/img"
abspath_src = path.abspath(path_src)
abspath_out = path.abspath(path_out)

file_paths = [path.join(abspath_src, name) for name in os.listdir(path_src) if path.isfile(path.join(abspath_src, name))]
#file = file_paths[1]

for file in file_paths:
  data = np.genfromtxt(file, delimiter=';', dtype=None)
  coordinates = data[data[:,4]==b'W'][:,2:4].astype(np.uint8)
  array = np.zeros(shape=(50,70), dtype=np.uint8)
  array[coordinates[:,1], coordinates[:,0]] = 1
  
  wafer = array.astype(np.float64)
  for __ in range(0,49):
    for _ in range(0,69):
      wafer[__,_] = (1/11)*array[__-1,__-1] + (1/11)*array[__-1,_] + (1/11)*array[__-1,_+1] + (1/11)*array[__,_-1] + (3/11)*array[__,_] + (1/11)*array[__,_+1] + (1/11)*array[__+1,_-1] + (1/11)*array[__+1,_] + (1/11)*array[__+1,_+1]
      
      if wafer[__,_] > 0.45:
        wafer[__,_] = 255
      else :
        wafer[__,_] = 0
  
  wafer = wafer.astype(np.uint8)
  img = Image.fromarray(wafer).crop((10, 10, 62, 42)).resize((100,100))
  img = ImageOps.invert(img)
  #img.show()
  img_filename = file.replace(abspath_src, abspath_out)[:-4] + '.png'
  img.save(img_filename)
  lot_id = file.split(path.sep)[-1].split('.')[0]
  print(lot_id, '-- image generated')
    
