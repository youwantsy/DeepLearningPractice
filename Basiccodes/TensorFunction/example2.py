import numpy as np

tensor = np.zeros((2,3))
print(tensor)

tensor = np.ones((2,3))
print(tensor)

tensor = np.random.rand(2,3)
print(tensor)

tensor = np.random.randn(2,3)
print(tensor)

tensor = np.random.normal(0, 1, (2,3)) # np.random.randn(2,3) 과 동일
print(tensor)

tensor = np.random.randint(0, 256, size=(2,3))
print(tensor)

tensor = np.arange(0,11,2)
print(tensor)
