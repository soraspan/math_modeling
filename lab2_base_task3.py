x = int(input('Введите год: '))

if x % 4 == 0 and (x % 100 != 0 or x % 400 == 0):
  print(f'{x}-високосный ')
else:
  print(f'{x}-невисокосный')