from math import sqrt
a = float(input('A ?'))
b = float(input('B ?'))
c = float(input('C ?'))

d = b**2 - 4 * a * c
if d >=0:
    x1 = (-b - sqrt(d)) / (2 * a)
    x2 = (-b + sqrt(d)) / (2 * a)
    print(f'x1 = {x1:.2f}')
    print(f'x2 = {x2:.2f}')
else:
    print ('Não existem raizes reias.')
