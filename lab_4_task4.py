import numpy as np

def my_func(a, b, N):
  Z = np.linspace(a, b, N)
  fx = np.zeros((N, 2))
  for i in range(len(Z)):
    fx[i, 0] = Z[i]
    fx[i, 1] = Z[i]**2+2
  return fx

print(my_func(1, 10, 20))