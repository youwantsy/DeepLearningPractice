import numpy as np

value_list = [[1,2],[3,4]]
tensor1 = np.array(value_list)

# tensor2 = np.array(tensor1)
# tensor1[0,0] = 10
# print(tensor2)

# tensor2 = np.copy(tensor1)
# tensor1[0,0] = 10
# print(tensor2)

tensor2 = np.asarray(tensor1)
tensor1[0,0] = 10
print(tensor2)