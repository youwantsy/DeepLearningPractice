import numpy as np
import random

person_list = []
for i in range(5):
    person = [random.randint(28, 50), random.randint(100, 900)]
    person_list.append(person)

dataset = np.array(person_list)

print("텐서 형태: {}D, {}".format(dataset.ndim, dataset.shape))
print("샘플 수: {}".format(dataset.shape[0]))
print("특성 수: {}".format(dataset.shape[1]))
print(dataset)
