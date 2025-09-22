def se_par(n):
    resto = n % 2
    if resto == 0:
        return True
    else:
        return False
x = int(input('Numero? '))

if se_par(x):
    print ('é par')
else:
    print ('é impar')
