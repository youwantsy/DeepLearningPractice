import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 10, 0.2)
y1 = np.sin(x)
y2 = np.cos(x)
#%%
plt.plot(x, y1, "r", label="np.sin(x)")
plt.plot(x, y2, "g", label="np.cos(X)")
plt.legend()
plt.show()

#%%
plt.plot(x, y1, ":r", label="np.sin(x)")
plt.plot(x, y2, "-.g", label="np.cos(x)")
plt.legend()
plt.show()

#%%
plt.plot(x, y1, "or", label="np.sin(x)")
plt.plot(x, y2, "^g", label="np.cos(x)")
plt.legend()
plt.show()