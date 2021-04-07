import numpy as np
import tensorflow as tf
#%%
dataset = np.array(
    [
        [1, 11, 21, 31],
        [2, 12, 22, 32],
        [3, 13, 23, 33],
        [4, 14, 24, 34],
        [5, 15, 25, 35]
    ]
)

np.random.shuffle(dataset)
print(dataset)

#%%
dataset = np.array(
    [
        [1, 11, 21, 31],
        [2, 12, 22, 32],
        [3, 13, 23, 33],
        [4, 14, 24, 34],
        [5, 15, 25, 35]
    ]
)
dataset_cloned = np.array(dataset)
np.random.shuffle(dataset_cloned)
print(dataset)
print(dataset_cloned)

#%%
dataset = np.array(
    [
        [1, 11, 21, 31],
        [2, 12, 22, 32],
        [3, 13, 23, 33],
        [4, 14, 24, 34],
        [5, 15, 25, 35]
    ]
)
dataset_cloned = tf.random.shuffle(dataset)
dataset_cloned = dataset_cloned.numpy()

print(dataset)
print(dataset_cloned)