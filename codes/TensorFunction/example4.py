import numpy as np

# 특정 위치에 요소 추가
tensor = np.array([[1,1], [3,3]])
tensor = np.insert(tensor, 0, [0,0], axis=0)
tensor = np.insert(tensor, 2, [2,2], axis=0)
print(tensor.shape, "\n", tensor)

# 맨끝에 요소 추가
tensor = np.array([[1,1], [2,2]])
tensor = np.append(tensor, np.array([[3,3]]), axis=0)
print(tensor.shape, "\n", tensor)

# 특정 위치의 요소 제거
tensor = np.array([[1,1], [2,2], [3,3]])
tensor = np.delete(tensor, 1, axis=0)
print(tensor.shape, "\n", tensor)
#%%
# 요소 중복 제거
tensor = np.array([[1,1,2,2,3,3]])
tensor = np.unique(tensor)
print(tensor.shape, "\n", tensor)
