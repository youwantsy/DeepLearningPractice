import tensorflow as tf
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

dataset_path = "C:/JSY/datasets/mnist/mnist_png.tar"
test_path = dataset_path + "/testing"

model = tf.keras.models.load_model("model.h5")

new_img_path = os.path.join(test_path, "7", "64.png")

img = cv2.imread(new_img_path, cv2.IMREAD_GRAYSCALE)

plt.imshow(img, cmap="gray")
plt.show()

img = img / 255
input = img[np.newaxis, ..., np.newaxis]

output = model.predict_classes(input)
print("예측 숫자: {}".format(output[0]))