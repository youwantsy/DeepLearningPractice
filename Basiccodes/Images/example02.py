import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf

import matplotlib
font_name = matplotlib.font_manager.FontProperties(
    fname="C:/Windows/Fonts/gulim.ttc").get_name()
matplotlib.rc('font', family=font_name)

def step(x):
    return np.array(x>0, dtype=np.int)

def sigmoid(x):
    return 1 / (1+np.exp(-x))

def relu(x):
    return np.maximum(0, x)

# input
x = np.arange(-10, 10, 0.1)

fig = plt.figure(figsize=(6,6))
fig.suptitle("서브플롯")

plt.subplot(3,2,1)
plt.title("\n\nsign 함수")
plt.plot(x, np.sign(x))

plt.subplot(3,2,2)
plt.title("tanh 함수")
plt.plot(x, np.tanh(x))

plt.subplot(3,2,3)
plt.title("step 함수")
plt.plot(x, step(x))

plt.subplot(3,2,4)
plt.title("sigmoid 함수")
plt.plot(x, sigmoid(x))

plt.subplot(3,2,5)
plt.title("relu 함수")
plt.plot(x, relu(x))

plt.show()