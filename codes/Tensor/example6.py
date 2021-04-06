import random
import numpy as np

year_temp = []
for date in range(2):
    day_temp = []
    for hour in range(0, 24, 4):
        curr_temp = random.randint(15, 25)
        max_temp = 25
        min_temp = 15
        mean_temp = int((max_temp+min_temp)/2)
        temperature = [curr_temp, max_temp, min_temp, mean_temp]
        day_temp.append(temperature)
    year_temp.append(day_temp)

dataset = np.array(year_temp)

print("텐서 형태: {}D, {}".format(dataset.ndim, dataset.shape))
print("측정 일수: {}".format(dataset.shape[0]))
print("측정 주기: {}".format(dataset.shape[1]))
print("측정 값수: {}".format(dataset.shape[2]))
print(dataset)