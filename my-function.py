
def exibe_media(a, b, c):
    soma = (a + b + c)
    print (soma / 3)

def retorn_media(n1, n2, n3):
    soma = (n1 + n2 + n3)
    return soma / 3

x = int(input('x?'))
y = input(' y ?'))
z = input(' z? '))

r1 = retorn_media(x, y, z)
print(f'ri = {r1}')
r2 = exibe_media(x, y, z)
print(f'r2 = {r2}')
