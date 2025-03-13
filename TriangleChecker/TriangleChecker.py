a=float(input('Введите первую сторону'))
b=float(input('Введите вторую сторону'))
c=float(input('Введите третью сторону'))
if (a+b>c) and (b+c>a) and (c+a>b):
  print('Существует')
else:
  print('Не существует')
