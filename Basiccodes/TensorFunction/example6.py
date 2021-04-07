import numpy as np

# %%
tensor = np.array([2, 1, 3])
tensor_asc = np.sort(tensor, axis=0)
print("올림차순", tensor_asc)

# %%
tensor = np.array([2, 1, 3])
tensor_desc = np.sort(tensor, axis=0)[::-1]
print("내림차순", tensor_desc)

# %%
tensor = np.array([2, 1, 3])
tensor_argsorted = np.argsort(tensor)
print("올림차순 인덱스:", tensor_argsorted)
print("올림차순 값:", end="")
for index in tensor_argsorted:
    print(tensor[index], end="")
print()