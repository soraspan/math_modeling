import numpy as np

c = 1
a = np.zeros((4, 5))
for i in range(4):
  for j in range(5):
    a[i, j] = c
    c += 1

slice = a[0:3,1:3]
print(slice, '\n')

slice = a[2::,0:2]
print(slice, '\n')

slice = a[1,2::]
print(slice, '\n')

slice = a[3,3::]
print(slice, '\n')