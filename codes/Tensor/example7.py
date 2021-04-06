import cv2
import matplotlib.pyplot as plt

image_path = "C:/JeongSeongYun/practice/images/bichon01.jpg"
tensor = cv2.imread(image_path)

print("텐서 타입: {}".format(type(tensor)))
print("텐서 형태: {}D, {}".format(tensor.ndim, tensor.shape))
print("높이 픽셀: {}".format(tensor.shape[0]))
print("너비 픽셀: {}".format(tensor.shape[1]))
print("채널 수: {}".format(tensor.shape[2]))
print("[B, G, R]: {}".format(tensor[0,0]))

plt.title("OpenCV BGR")
plt.imshow(tensor)
plt.show()

tensor = cv2.cvtColor(tensor, cv2.COLOR_BGR2RGB)
print("[R, G, B]: {}".format(tensor[0, 0]))
plt.title("OpenCV RGB")
plt.imshow(tensor)
plt.show()