import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

image_path = "C:/JeongSeongYun/practice/images/bichon01.jpg"
img = Image.open(image_path)
tensor = np.array(img)

print("img 타입: {}".format(type(img)))
print("텐서 타입: {}".format(type(tensor)))
print("텐서 형태: {}D, {}".format(tensor.ndim, tensor.shape))
print("높이 픽셀: {}".format(tensor.shape[0]))
print("너비 픽셀: {}".format(tensor.shape[1]))
print("채널 수: {}".format(tensor.shape[2]))
print("[B, G, R]: {}".format(tensor[0,0]))

plt.title("PIL RGB")
plt.imshow(tensor)
plt.show()