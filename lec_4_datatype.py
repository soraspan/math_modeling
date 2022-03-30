def changer(a, b):
  a = 2
  b[0] = 'good'

x = 10
L = [1, 2]

changer(x, L)

print(x)
print(L)

L = [1, 2]
changer(x, L[:])

print(L)

#complex
x = 3
y = 4

z = complex(x, y)
print(z)

w = complex(y, x)

print(z + w)

#string
s = 'hello'
print(s[0])


#tuple
t = (1, 4, 9)
print(t)
print(t[0])

#dict
d = {'a1':4, 4:'a1', 'str':'hello'}
print(d['a1'])
print(d[4])
print(d['str'])

d['str'] = 'good'
print(d)