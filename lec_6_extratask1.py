import numpy as np
import matplotlib.pyplot as plt

a = 1
b = 1
A = 1
B = 0.125
delta = np.pi / 2
N = 500

t = np.linspace(0, 10, N)

x = A * np.sin(a * t + delta)
y = B * np.sin(b * t)

plt.plot(x, y)

plt.show()