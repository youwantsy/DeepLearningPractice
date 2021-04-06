import os
import numpy as np
import cv2

image_dir = "images"
file_names = os.listdir(image_dir)

heights = []
widths = []

for file_name in file_names:
    file_path = os.path.join(image_dir, file_name)
    img = cv2.imread(file_path)
    h, w, _= img.shape
    heights.append(h)
    widths.append(w)
