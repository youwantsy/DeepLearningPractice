import os
import matplotlib.pyplot as plt
from glob import glob
import tensorflow as tf

#%%
datasets_path = "C:/JSY/datasets/mnist/mnist_png.tar/mnist_png"

#%%
train_samples = glob(datasets_path + "/training/*/*.png")
print("총 훈련 샘플 수:", len(train_samples))

#%%
labels = os.listdir(os.path.join(datasets_path, "training"))
print("레이블 리스트:", labels)

#%%
samples_per_label=[]
for label in labels:
    samples = os.listdir(os.path.join(datasets_path, "training", label))
    samples_per_label.append(len(samples))
print("레이블당 샘플 수:", samples_per_label)

#%%
plt.bar(labels, samples_per_label)
plt.title("Label_Sample")
plt.show()