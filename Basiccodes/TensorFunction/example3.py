import numpy as np

# 형태 변경
tensor1 = np.array([[[1,2,3],[3,4,5]]])
tensor2 = np.reshape(tensor1, (1,3,2))
print(tensor1.shape, "\n", tensor1)
print(tensor2.shape, "\n", tensor2)


# 0축 추가
tensor1 = np.array([[[1,2,3],[3,4,5]]])
tensor2 = np.reshape(tensor1, (1,1,2,3))
#tensor2 = tensor1[np.newaxis, ...]
#tensor2 = np.expand_dims(tensor1, axis = 0)
print(tensor1.shape, "\n", tensor1)
print(tensor2.shape, "\n", tensor2)

# 끝축 추가
tensor1 = np.array([[[1,2,3], [3,4,5]]])
tensor2 = np.reshape(tensor1, (1,2,3,1))
# tensor2 = tensor1[..., np.newaxis]
# tensor2 = np.expand_dims(tensor1, axis=-1)
print(tensor1.shape, "\n", tensor1)
print(tensor2.shape, "\n", tensor2)

# 1D로 변경
tensor1 = np.array([[[1,2,3],[3,4,5]]])
tensor2 = np.reshape(tensor1, (6,))
#tensor2 = tensor1.flatten()
print(tensor1.shape, "\n", tensor1)
print(tensor2.shape, "\n", tensor2)

# 요소 수가 1인 축 제거
tensor1 = np.array([[[1,2,3], [3,4,5]]])
tensor2 = np.squeeze(tensor1)
print(tensor1.shape, "\n", tensor1)
print(tensor2.shape, "\n", tensor2)