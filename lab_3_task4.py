import numpy as np

n = int(input('n = '))
m = int(input('m = '))

a = np.zeros((n, m))

for i in range(n):
  for j in range(m):
    if (np.sin(n * (i + 1) + m * (j + 1))) > 0:
      a[i, j] = np.sin(n * (i + 1) + m * (j + 1))
    else:
      a[i, j] = 0
print(a)