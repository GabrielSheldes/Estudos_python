a =  float (input('a? '))
b =  float (input('b? '))
c =  float (input('c? '))

if a < b+c and b < a+c and c < a+b:
    print ('formam um triangulo!')
    if a == b and b == c:
        print ('Tipo: Equilatero')
    else:
        if a == b or b == c or a == c:
            print ('isosceles')
        else:
            print ('escaleno')
else:
    print('Não formam um triangulo')
