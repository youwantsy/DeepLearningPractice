import cv2

filepath = "/JSY/images/bichon02.jpg"

img = cv2.imread(filepath)
# img = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)

print("img.shape: {}".format(img.shape))
img = cv2.resize(img, dsize=(500, 300))
print("img.shape: {}".format(img.shape))

cv2.imshow("win1", img)
cv2.waitKey()
cv2.destroyWindow("win1")