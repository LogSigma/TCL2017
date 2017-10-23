import os
from os import path
import scipy as sp
import itertools as it

from PIL import Image, ImageOps
from glob import glob

path_stamp = "./data/stamp"

def flip_and_rotator(marked, axis=None, angle=0):
  
  flip_axis = {'vertical' : lambda x: x[:,::-1],
               'horizontal': lambda x:x[::-1,:],
               'transposed': lambda x:x[::-1,::-1]}
  
  if axis in flip_axis.key():
    flipped = flip_axis[axis](marked)
  else axis not in flip_axis.key():
    raise Exception('')
  
  rotated = sp.ndimage.rotate(flipped, angle, cval=255, mode='nearest', reshape=0)
  
  return rotated

#%%
file_paths = 

bad_name = sorted(glob(path_out + '/' + '*.png'))
bad_list = list((sp.misc.imresize(sp.misc.imread(bad), size=(100,100))) for bad in bad_name)

mark_list = bad_list
axis_list = ['vertical', 'horizontal', 'transposed']
angle_gen = range(0, 360, 30)

raw_list = [flip_and_rotator(mark, axis=axis, angle=angle) for mark, axis, angle in it.product(mark_list, axis_list, angle_gen)]

# The results
print('Augmentated pattern : %s' % len(raw_list))
i = 1
for sample in raw_list:
  sample = 255 - sample
  img = Image.fromarray(sample)
  img = ImageOps.invert(img)
  #img.show()
  img_filename = path_oug + '/' + str(i) + '.png'
  i = i + 1
  img.save(img_filename)
  
            
            
            
            
