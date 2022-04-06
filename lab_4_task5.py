import numpy as np

def my_func(x, **kwrgs):
  if x == 'tri':
    Stri = (kwrgs['c'] * kwrgs['h']) / 2
    return Stri
  elif x == 'quad':
    Squad = kwrgs['a']**2
    return Squad
  elif x == 'circ':
    Scirc = np.pi * kwrgs['r']**2
    return Scirc

print(my_func('tri', c=2, h=3))
print(my_func('quad', a=2))
print(my_func('circ', r=1))