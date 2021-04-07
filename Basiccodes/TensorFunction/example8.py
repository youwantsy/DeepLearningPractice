import numpy as np
#%% 최댓값 최솟값 찾기
tensor = np.random.randint(0, 256, (5,))
tensor = tensor / np.array(255)
tensor = np.round(tensor, 2)

max_index = np.argmax(tensor)
min_index = np.argmin(tensor)
print(tensor)
print("max_index:", max_index, "max_value", tensor[max_index])
print("min_index:", min_index, "min_value", tensor[min_index])
#%% 0이 아닌 요소 찾기
tensor = np.array([1, 0, 0, 1, 0])
print("전체 요소 수:", len(tensor))
print("0이 아닌 요소 수:", np.count_nonzero(tensor))

#%% 텐서 결합 함수
tensor1 = np.array([[1,2], [3,4], [5,6]])
tensor2 = np.array([[7,8], [9,0]])
tensor_concated = np.concatenate((tensor1, tensor2))
print(tensor_concated)

#%% 텐서 집계 함수
tensor = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print("전체 합:", np.sum(tensor))
print("평균:", np.mean(tensor))
print("최대:", np.max(tensor))
print("최소:", np.min(tensor))
print("누적:", np.cumsum(tensor))