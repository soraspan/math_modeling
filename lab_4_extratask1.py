def my_func(a, n):
  k = 1
  for i in range(n):
    k *= a
  return k

print(my_func(3, 3))