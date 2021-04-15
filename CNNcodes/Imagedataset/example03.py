import cv2
from glob import glob
import numpy as np
import tensorflow as tf
import os
import matplotlib.pyplot as plt
#%%

def height_width_info(sample_path_list):
    heights = []
    widths = []
    for i, sample in enumerate(sample_path_list):
        img = cv2.imread(sample, cv2.IMREAD_GRAYSCALE)
        h, w = img.shape
        heights.append(h)
        widths.append(w)
    return (np.unique(heights), np.unique(widths))

datasets_path = "C:/JSY/datasets/mnist/mnist_png.tar/mnist_png"
train_path = datasets_path + "/training"
test_path = datasets_path + "/testing"

train_sample_path_list = glob(datasets_path + "/training/*/*.png")
result = height_width_info(train_sample_path_list)
print("훈련 이미지:", result)

test_sample_path_list = glob(datasets_path + "/testing/*/*.png")
result = height_width_info(test_sample_path_list)
print("테스트 이미지:", result)

#%%
train_idg = tf.keras.preprocessing.image.ImageDataGenerator(
    rescale=1./255.,
    validation_split=0.2
)
test_idg = tf.keras.preprocessing.image.ImageDataGenerator(
    rescale=1./255.
)

#%%
train_iterator = train_idg.flow_from_directory(
    train_path,
    target_size=(28,28),
    batch_size=32,
    color_mode="grayscale",
    class_mode="categorical",
    subset="training"
)

val_iterator = train_idg.flow_from_directory(
    train_path,
    target_size=(28,28),
    batch_size=32,
    color_mode="grayscale",
    class_mode="categorical",
    subset="validation"
)

test_iterator = test_idg.flow_from_directory(
    test_path,
    target_size=(28,28),
    batch_size=32,
    color_mode="grayscale",
    class_mode="categorical"
)

#%%
model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28,28,1)),
    tf.keras.layers.Dense(512, activation="relu"),
    tf.keras.layers.Dense(10, activation="softmax")
])

#%%
model.compile(
    loss=tf.keras.losses.categorical_crossentropy,
    optimizer=tf.keras.optimizers.RMSprop(),
    metrics=["accuracy"]
)

#%%
model.fit_generator(
    train_iterator,
    validation_data=val_iterator,
    epochs=10,
    verbose=1
)

#%%
eval_result = model.evaluate_generator(test_iterator)
print("테스트 평가 결과:", eval_result)

#%%
label_path = os.path.join(test_path, "3")
img_path = os.path.join(label_path, os.listdir(label_path)[0])
img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
plt.imshow(img, cmap="gray")
plt.show()


img = img /255.
print(img.shape)
img = img[np.newaxis, ..., np.newaxis]
print(img.shape)

result = model.predict_classes(img)
print(result)