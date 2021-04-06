import numpy as np
#%%
tensor = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print("tensor[2]:", tensor[2])
print("tensor[-2]:", tensor[-2])

#%%
tensor = np.array(
    [
        [0, 1, 2, 3, 4],
        [5, 6, 7, 8, 9]
    ]
)

print("tensor[1]:", tensor[1])
print("tensor[1, 2]:", tensor[1, 2])
print("tensor[1, -1]:", tensor[1, -1])

#%%
tensor = np.array(
    [
        [0, 1, 2, 3, 4],
        [5, 6, 7, 8, 9]
    ]
)

print("tensor[1][3]:", tensor[1][3])

#%%
tensor = np.array([10, 11, 12, 13, 14, 15, 16, 17, 18, 19])
print(tensor[np.array([2, 4, 7])])

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
print(tensor[np.array([0, 2, 4, 6, 8])])
print(tensor[np.array([i for i in range(tensor.shape[0]) if i%2 == 0])])

#%%
tensor = np.array([10, 11, 12, 13, 14])
print(tensor[np.array([True, False, False, True, True])])

#%%
tensor = np.array([10, 11, 12, 13, 14, 15, 16, 17, 18, 19])
condition = (tensor % np.array(3)) == np.array(0)
print(condition)
print(tensor[condition])

#%%
