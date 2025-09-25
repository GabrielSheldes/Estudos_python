from triangulo import *

'''Essa função recebe em seus paramentros a, b, c
tres floats e devolve como resposta um valor booleano indicando se
essas medidas podem formar um triangulo'''



a = float(input('primeiro num: '))
b = float(input('Segundo num: '))
c = float(input('Terceiro num: '))

if triangulo (a, b, c):
    print ('fomam um triangulo')
else:
  print('não formam um triangulo')

tipo = tipo_triangulo(a, b, c)
print (f'Triangulo {tipo}')
