a=  float(input('a? '))
b=  float(input('b? '))
c=  float(input('c? '))

if a == b and b == c:
    print('Equiátero')
else:
    if a == b or a == c or b ==c:
        print('isósceles')
    else:
        print('Escaleno')
