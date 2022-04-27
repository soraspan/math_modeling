import matplotlib.pyplot as plt
import numpy as np

def elip_plot():
  x = np.arange(-15, 15, 0.1)
  y = np.arange(-15, 15, 0.1)

  X, Y = np.meshgrid(x, y)

  fxy = (X - 3)**2 / 2**2 + (Y - 4)**2 / 3**2

  plt.contour(X, Y, fxy, levels=[1])
  plt.axis('equal')
  plt.show

elip_plot()