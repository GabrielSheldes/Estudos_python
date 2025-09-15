n1 = float(input('valor do produto'))
n2 = float(input('quantidade: '))

total = n1 * n2
if total > 200.00:
    opcao = input('desconto [D] ou parcelamento [P]? ')
    if opcao == 'D':
        desc = 0.05 * total
        total -= desc
        print(f'Desconto de R$ {desc:.2f}')
    else:
        print(f'4 parcelas de R$ {total/4:.2f}')

print (f'total: R$ {total:.2f}')
              
