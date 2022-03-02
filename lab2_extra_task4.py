a = int(input('Введите ваше число: '))

b = []
for i in range(1, a+1):
  if a % i == 0:
    b.append(i)

print('Простые ножители вашего числа: ', end=' ')
k = 0
for i in range(len(b)):
  for j in range(1, b[i]+1):
    if b[i] % j !=0:
      k += 1
  if k = 2:
    print(b[i], end=' ')
print()