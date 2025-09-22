def maximo(a, b):
    if a > b:
        return a
    else:
        return b

x = int(input('x? '))
y = int(input('y? '))

m = maximo(x,y)

print(f'Máximo: {m}')
