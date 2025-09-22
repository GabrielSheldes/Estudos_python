def cabecalho():
    print('/n fatec diadema - luigi papaiz')
cont_linha = 5

for i in range(16):
    if cont_linha > 4:
        cabecalho()
        cont_linha = 1
        
    print (f'{cont_linha} testando a função cabeçalho)
    cont_linha += 1
