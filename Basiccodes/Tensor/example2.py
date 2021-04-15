import numpy as np

tensor = np.array([-1,2,7,19])

print(tensor)
print("텐서 타입: {}".format(type(tensor)))
print("텐서 형태: {}, {}D".format(tensor.shape, tensor.ndim))
print("텐서 요소 타입: {}".format(tensor.dtype))
print("텐서 전체 요소수: {}".format(tensor.size))
print("텐서 0차원 요소수: {}, {}".format(len(tensor), tensor.shape[0]))
