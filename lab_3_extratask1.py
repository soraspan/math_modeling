import numpy as np

a, b, c = np.zeros((2, 2)), np.zeros((2, 2)), np.zeros((2, 2))

for i in range(2):
  for j in range(2):
    a[i, j] = int(input())
print(a)
for i in range(2):
  for j in range(2):
    b[i, j] = int(input())
print(b)
for i in range(2):
  for j in range(2):
    if a[i, j] > b[i, j]:
      c[i, j] = a[i, j]
    else:
      c[i, j] = b[i, j]
print(c)