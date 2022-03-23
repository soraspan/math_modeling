import numpy as np

g = 9.8

x0 = 0
y0 = 0
Vx0 = 3
Vy0 = 5

t = np.arange(1, 5, 1)
x = x0 + Vx0 * t
y = y0 + Vy0 * t -  g * t**2 / 2

coords = np.zeros((len(t), 3))
for i in range(len(t)):
  coords[i, 0] = t[i]
  coords[i, 1] = x[i]
  coords[i, 2] = y[i]
print(coords)