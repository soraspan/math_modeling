a = [1, 2, 3]

def my_func(arg1):
  z = 1
  for i in range(len(arg1)):
    z *= arg1[i]
  return z    

print(my_func(a))