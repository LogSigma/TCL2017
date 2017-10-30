import numpy as np
import scipy as sp
from glob import glob
import tensorflow as tf
from sklearn import model_selection

# Labels
train_label = np.array(tuple(item[0] for item in train), dtype=np.float32)
test_label = np.array(tuple(item[0] for item in test), dtype=np.float32)

# Images
#train_image = np.array(tuple(item[1] for item in train), dtype=np.uint8)
#test_image = np.array(tuple(item[1] for item in test), dtype=np.uint8)
train_image = np.stack((item[1].astype(np.float32).reshape((100 * 100,)) for item in train))#.astype(np.float32)
test_image = np.stack((item[1].astype(np.float32).reshape((100 * 100,)) for item in test))#.astype(np.float32)

print('Train : %s' % len(train))
print('Test : %s' % len(test))

n_class = len(set(tuple(item[0] for item in data)))

train_onehot = tf.one_hot(indices = train_label,
                          depth = n_class,
                          on_value = 1.,
                          off_value = 0.,
                          axis = -1)  # col : -1, idx : 0

test_onehot = tf.one_hot(indices = test_label,
                         depth = n_class,
                         on_value = 1.,
                         off_value = 0.,
                         axis = -1)  # col : -1, idx : 0

# Training Parameters
learning_rate = 0.001
training_steps = 1000
batch_size = 128
display_step = 200

