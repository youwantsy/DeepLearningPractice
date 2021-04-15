import os
import cv2
import pandas as pd
import matplotlib.pyplot as plt

#%%
original_path = "C:/JSY/datasets/kaggle/train"
train_path = "C:/JSY/datasets/kaggle/train"
test_path = "C:/JSY/datasets/kaggle/test1"

file_list = os.listdir(original_path)
total_image_count = len(file_list)
print(total_image_count)

#%%
labels = ["dog", "cat"]
images = [0,0]
for i, file in enumerate(file_list):
    if labels[0] in file:
        images[0] += 1
    elif labels[1] in file:
        images[1] += 1
    print("검사 수:", (i+1))

plt.bar(labels, images)
plt.show()

#%%
heights = []
widths = []

for i, file in enumerate(file_list):
    file_path = os.path.join(original_path, file)
    img = cv2.imread(file_path)
    heights.append(img.shape[0])
    widths.append(img.shape[1])
    print("검사 수:", (i+1))

dataframe = pd.DataFrame({"height":heights, "width":widths})
print(dataframe.describe())