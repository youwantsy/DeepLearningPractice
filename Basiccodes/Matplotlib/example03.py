from PIL import Image
import matplotlib.pyplot as plt

#%%
file_path = "/JSY/images/bichon02.jpg"
img = Image.open(file_path)
print(type(img))

plt.imshow(img)
plt.axis("off")
plt.show()
