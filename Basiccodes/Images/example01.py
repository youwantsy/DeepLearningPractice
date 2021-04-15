import cv2
import tensorflow as tf
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

#%%
def getDatasetWithOpenCV(file_path):
    img = cv2.imread(file_path)
    img = cv2.resize(img, dsize=(640, 480))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img

def getDatasetWithPIL(file_path):
    img = Image.open(file_path)
    img = img.resize((640, 480))
    img = np.array(img)
    return img

def getDatasetWithTensorFlow(file_path):
    img = tf.keras.preprocessing.image.load_img(
        file_path,
        target_size=(480, 640)
    )
    img = np.array(img)
    return img

if __name__ == "__main__":
    file_path = "/JSY/images/bichon02.jpg"

    imgO = getDatasetWithOpenCV(file_path)
    imgT = getDatasetWithTensorFlow(file_path)
    imgP = getDatasetWithPIL(file_path)

    plt.imshow(imgO)
    plt.show()