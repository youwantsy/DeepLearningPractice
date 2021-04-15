import os
import random
import shutil

import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.layers import MaxPooling2D, Conv2D, Flatten, Dense, ZeroPadding2D
# %%
original_path = "C:/JSY/datasets/kaggle/train"
train_path = "C:/JSY/datasets/kaggle/train"
test_path = "C:/JSY/datasets/kaggle/test1"
file_list = os.listdir(original_path)

random.shuffle(file_list)
print(file_list)

#%%
train_file_list = file_list[:24000]
print(len(train_file_list))

test_file_list = file_list[24000:25000]
print(len(test_file_list))

#%%
def image_copy(file_list, path):
    for i, file in enumerate(file_list):
        tokens = file.split(".")
        label = tokens[0]
        dst_path = os.path.join(path, label, file)
        if not os.path.exists(dst_path):
            src_path = os.path.join(train_path, file)
            shutil.copyfile(src_path, dst_path)
            print("복사 {} ({}/{})".format(file, (i+1), len(file_list)))

#%%
if len(os.listdir(os.path.join(train_path,"dog"))) == 0:
    image_copy(train_file_list, train_path)
    image_copy(test_file_list, test_path)
    print("이미지 복사 완료")
else:
    print("이미지 복사 되어 있음")
#%%
label_list = ["dog", "cat"]

def get_image_num_list(path):
    image_num_list = []
    for label in label_list:
        label_path = os.path.join(path, label)
        image_num = len(os.listdir(label_path))
        image_num_list.append(image_num)
    return image_num_list

train_image_num_list = get_image_num_list(train_path)
test_image_num_list = get_image_num_list(test_path)

# %%
train_path = "C:/JSY/datasets/kaggle/train"
test_path = "C:/JSY/datasets/kaggle/test1"

train_idg = tf.keras.preprocessing.image.ImageDataGenerator(
    rescale=1. / 255.,
    validation_split=0.2
)

test_idg = tf.keras.preprocessing.image.ImageDataGenerator(
    rescale=1. / 255.
)

train_dir_iterator = train_idg.flow_from_directory(
    train_path,
    target_size=(150, 150),
    batch_size=20,
    class_mode="binary",
    subset="training"
)

val_dir_iterator = train_idg.flow_from_directory(
    train_path,
    target_size=(150, 150),
    batch_size=20,
    class_mode="binary",
    subset="validation"
)

test_dir_iterator = test_idg.flow_from_directory(
    test_path,
    target_size=(150, 150),
    batch_size=20,
    class_mode="binary"
)
