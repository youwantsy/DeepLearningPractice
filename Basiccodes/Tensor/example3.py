import numpy as np


tensor = np.array(
    [
        [-1, -5, 84],
        [2, 0.5, 56],
        [7, 1.9, 1],
        [-19, 6, 8]
    ]
)

print(tensor)
print("텐서 타입: {}".format(type(tensor)))
print("텐서 형태: {}, {}D".format(tensor.shape, tensor.ndim))
print("텐서 요소 타입: {}".format(tensor.dtype))
print("텐서 전체 요소수: {}".format(tensor.size))
print("텐서 0차원 요소수: {}, {}".format(len(tensor), tensor.shape[0]))