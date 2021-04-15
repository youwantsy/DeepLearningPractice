import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0.1, 1, 0.01)
y = (1/(2*np.pi)*x)*np.exp(-1/2*x*x)
plt.plot(x, y)
plt.show()

#%%
x = np.arange(0, 2*np.pi, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)

plt.figure(1)
plt.plot(x, y1)

plt.figure(2)
plt.plot(x, y2)

plt.show()

#%%
plt.plot(x,y1)
plt.plot(x,y2)
plt.show()

#%%
x = np.arange(0, 100, 0.5)
y1 = x**2
y2 = x**3

plt.xlabel("x")
plt.ylabel("y")

plt.xlim(0, 5)
plt.ylim(0, 100)

plt.xticks(np.arange(0, 5.5, step=0.5))
plt.yticks(np.arange(0, 110, step=10))

plt.grid(linestyle=":")

plt.plot(x, y1, label="x**2")
plt.plot(x, y2, label="x**3")
plt.legend()

plt.show()