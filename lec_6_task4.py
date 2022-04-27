import matplotlib.pyplot as plt
import numpy as np

def log_spiral(e = 3):
  fi = np.arange(0, 1440, 0.01)
  r = e**fi
  x = r * np.cos(fi)
  y = r * np.sin(fi)

  plt.plot(x, y)
  plt.show()

def arch_spiral(k):
  fi = np.arange(0, 1440 , 0.01)
  r = k * fi
  x = r * np.cos(fi)
  y = r * np.sin(fi)
  
  plt.plot(x, y)
  plt.show()

def staf_spiral(k):
  fi = np.arange(0.01, 1440, 0.01)
  r = k / np.sqrt(fi)
  x = r * np.cos(fi)
  y = r * np.sin(fi)
  
  plt.plot(x, y)
  plt.axis('equal')
  plt.show()

def rose(k):
  fi = np.arange(0.01, 360, 0.01)
  r = np.sin(k * fi)
  x = r * np.cos(fi)
  y = r * np.sin(fi)
  
  plt.plot(x, y)
  plt.axis('equal')
  plt.show()
  
rose(2 / 5)