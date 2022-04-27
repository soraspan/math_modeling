import matplotlib.pyplot as plt
import numpy as np

def giperbola_plotter():
  x1 = np.arange(-10, 0, 0.01)
  x2 = np.arange(0, 10, 0.01)
  y1 = 1 / x1
  y2 = 1 / x2
  
  plt.plot(x1, y1)
  plt.plot(x2, y2)
  plt.show()

giperbola_plotter()