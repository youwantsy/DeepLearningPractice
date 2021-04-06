import numpy as np

#%%
tensor = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print("tensor[2:5]:", tensor[2:5])
print("tensor[:-7]:", tensor[:-7])
print("tensor[1:7:2]:", tensor[1:7:2])
print("tensor[::-1]:", tensor[::-1])

#%%
tensor = np.array(
    [
        [0, 10, 20, 30],
        [1, 11, 21, 31],
        [2, 12, 22, 32],
        [3, 13, 23, 33],
        [4, 14, 24, 34],
        [5, 15, 25, 35],
        [6, 16, 26, 36],
        [7, 17, 27, 37],
        [8, 18, 28, 38],
        [9, 19, 29, 39]
    ]
)

print(tensor[0:8], "\n")
print(tensor[8:10], "\n")

#%%
print(tensor[0:8, :], "\n")
print(tensor[8:10, :], "\n")

#%%
print(tensor[0:int(len(tensor)*0.8)], "\n")
print(tensor[int(len(tensor)*0.8):len(tensor)], "\n")

#%%
print("tensor[0:8, 2:]", "\n", tensor[0:8, 2:], "\n")
print("tensor[8:10, 2:]", "\n", tensor[8:10,2:], "\n")

#%%
tensor = np.array(
    [
        [0, 10, 20, 30],
        [1, 11, 21, 31],
        [2, 12, 22, 32],
        [3, 13, 23, 33],
        [4, 14, 24, 34],
        [5, 15, 25, 35],
    ]
)
print(tensor[np.array([0,3]), 1:3], "\n")
print(tensor[np.array([i for i in range(tensor.shape[0]) if i%3==0]), 1:3], "\n")
print(tensor[np.array([True, False, False, True, False, False]), 1:3], "\n")
print(tensor[np.array([i%3==0 for i in range(tensor.shape[0])]), 1:3], "\n")