def triangulo(a, b, c):

    '''Essa função recebe em seus paramentros a, b, c
tres floats e devolve como resposta um valor booleano indicando se
essas medidas podem formar um triangulo'''

    if a < b+c and b < a+c and c < a+b:
       return True
    else:
        return False

def tipo_triangulo(a, b, c):
    if a == b and b == c:
        return 'equilatero'
    else:
        if a == b or b == c or c == a:
            return 'isosceles'
        else:
            return 'escaleno'

a = float(input('primeiro num: '))
b = float(input('Segundo num: '))
c = float(input('Terceiro num: '))

if triangulo (a, b, c):
    print ('fomam um triangulo')
else:
  print('não formam um triangulo')

tipo = tipo_triangulo(a, b, c)
print (f'Triangulo {tipo}')
