
def converte(data):
    d, m, a = data.split('/')
    d = int(d)
    m = int(m)
    a = int(a)
    return d, m, a

def bissexto(a):
    if (a % 4 == 0 and a % 100 != 0)or a % 400 == 0:
        return True
    else:
        return False
    

def dia_maximo(m,a):
    if m == 2:
        return 28 +int(bissexto(a))
    else:
        if m == 4 or m == 6 or m == 9 or m == 11:
            return 30
        else:
            return 31
    
def valida(d, m, a):
    if a < 1900:
        return False
    else:
        if m < 1 or m > 12:
            return False
        else:
            if d < 1 or d > dia_maximo(m, a):
                return False
            else:
                return True

def calcula_ds(d, m, a):
    pagamento = int(input('Quantos dias para pagar? : '))
    d +=pagamento
    if d > dia_maximo(m, a):
        d = (d - dia_maximo(m, a)) 
        m += 1
        if m > 12:
            m = 1
            a += 1
    return d, m, a

def exibe_ds(d, m ,a):
    d, m, a = calcula_ds(d, m, a)
    print(f'{d:02}/{m:02}/{a}')
    
def main( ):
    d, m, a = converte(input('Data? '))

    if valida(d, m, a) == True:
        exibe_ds(d, m, a)
    else:
        print('Data inválida!')

main() 

