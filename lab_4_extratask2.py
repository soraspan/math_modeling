def fib(n):
  f1 = 0
  f2 = 1
  
  if n > 1:
    for i in range(n-2):
      f1, f2 = f2, f1 + f2
    return f2
  else:
    return f1

print(fib(1))