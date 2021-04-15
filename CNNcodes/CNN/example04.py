import os
import random
import shutil

import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Flatten

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

plt.bar(label_list, train_image_num_list, width=0.2, label="Train img num")
plt.bar(label_list, test_image_num_list, width=0.2, align="edge", label="Test img num")
plt.legend(fontsize="16")
plt.xticks(fontsize="16")
plt.yticks(fontsize="16")
plt.show()


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

# %%
model = tf.keras.models.Sequential([
    Conv2D(32, (3, 3), activation="relu", input_shape=(150, 150, 3)),
    MaxPooling2D((2, 2)),
    Conv2D(64, (3, 3), activation="relu"),
    MaxPooling2D((2, 2)),
    Conv2D(128, (3, 3), activation="relu"),
    MaxPooling2D((2, 2)),
    Conv2D(128, (3, 3), activation="relu"),
    Flatten(),
    Dense(512, activation="relu"),
    Dense(1, activation="sigmoid")
])

model.summary()


#%%
model.compile(
    loss=tf.keras.losses.binary_crossentropy,
    optimizer=tf.keras.optimizers.RMSprop(),
    metrics=["accuracy"]
)
#%%
checkpoint_path = "C:/JSY/Checkpoint/cp.ckpt"
checkpoint_dir = os.path.dirname(checkpoint_path)

cp_callback = tf.keras.callbacks.ModelCheckpoint(filepath=checkpoint_path,
                                                 verbose=1,
                                                 save_weights_only=True,
                                                 period=3)
#%%

history = model.fit_generator(
    train_dir_iterator,
    validation_data=val_dir_iterator,
    callbacks=[cp_callback],
    epochs=20,
    verbose=1
)

#%%
plt.plot(history.epoch, history.history["loss"], "bo", label="Train loss")
plt.plot(history.epoch, history.history["val_loss"], "g--", label="Validation loss")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.legend()
plt.show()

#%%
plt.plot(history.epoch, history.history["accuracy"], "bo", label="Train acc")
plt.plot(history.epoch, history.history["val_accuracy"], "g--", label="Validation acc")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.legend()
plt.show()

#%%
