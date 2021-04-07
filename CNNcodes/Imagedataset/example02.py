import os
import cv2
import matplotlib.pyplot as plt

#%%
datasets_path = "C:/JSY/datasets/mnist/mnist_png.tar/mnist_png"

train_label_2_path = os.path.join(datasets_path, "training", "2")
sample_paths = os.listdir(train_label_2_path)
sample_path = os.path.join(train_label_2_path, sample_paths[0])
img = cv2.imread(sample_path, cv2.IMREAD_GRAYSCALE)

print("이미지 텐서 형태:", img.shape)

plt.imshow(img, cmap="gray")
plt.show()