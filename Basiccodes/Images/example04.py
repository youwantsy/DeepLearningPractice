import cv2

filepath = "C:/JSY/images/bichon01.jpg"
img = cv2.imread(filepath)

cv2.imwrite("C:/JSY/images/test1.JPG", img)
