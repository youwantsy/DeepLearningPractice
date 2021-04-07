import os
import numpy as np
import cv2

image_dir = "C:/JSY/images"
file_names = os.listdir(image_dir)

heights = []
widths = []

for file_name in file_names:
    file_path = os.path.join(image_dir, file_name)
    img = cv2.imread(file_path)
    h, w, _= img.shape
    heights.append(h)
    widths.append(w)

heights_unique = np.unique(heights)
widths_unique = np.unique(widths)

print("heights", "\n", heights, "\n", heights_unique)
print("widths", "\n", widths, "\n", widths_unique)
print("min height", np.min(heights_unique))
print("min width", np.min(widths_unique))