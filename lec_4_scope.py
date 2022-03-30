x0 = 10 #global view

def move(t): #local view
  x = x0 * t
  return x
  
print(move(3))

a = 'good'

def my_func():
  a = 'bad'
  print(a)

my_func()
print(a)

def my_func1():
  global a
  a = 'bad'
  print(a)

my_func1()
print(a)