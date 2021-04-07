import numpy as np

tensor = np.array(-1)

print(tensor)
print("텐서 타입: {}".format(type(tensor)))
print("텐서 형태: {}, {}D".format(tensor.shape, tensor.ndim))
print("텐서 요소 타입: {}".format(tensor.dtype))
