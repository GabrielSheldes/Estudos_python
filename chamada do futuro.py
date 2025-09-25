from random import choice

def exibe(alunos):
    for aluno in alunos:
        print(f'\'{aluno}\',')
    print()

def exibe_agardavel(chamda):
    for registro in chamda:
        print(registro)

def filtra_chamada(chamada,criterio):
    filtrada = [ ]
    for registro in chamada:
        nome, presenca = registro
        if presenca == criterio:
            filtrada.append(nome)
        return filtrada
        
    
def executa_chamada(alunos):
    alunos_chamados = []
    while alunos !=[]:
        sorteado = choice (alunos)
        presente=input (f'{sorteado}\nestá presente? (p/f)? ')
        print()
        alunos.remove(sorteado)
        alunos_chamados.append([sorteado, presente])
    return alunos_chamados


alunos = [
'ALEX DOS SANTOS SOUSA',
'ARTHUR DE OLIVEIRA BORGES',
'CAMILLA MIDORI KANASHIRO SANTOS',
'CARLOS EDUARDO LIMA SILVA',
'DIEGO LIMA HENRIQUE',
'EDUARDO DE SOUSA BARBOSA',
'EDUARDO FELIPE DOS SANTOS ALVES',
'ERICK SILVA',
'EVELY ARAUJO DE MENDONCA',
'FAGNER CARDOSO DA SILVA',
'FREDY ISAAC FARIAS DE OLIVEIRA',
'GABRIEL BENATTO ALENCAR STOLSES',
'GABRIEL SHELDES FERREIRA ARANTES',
'GABRIELY BENITO MONTEIRO',
'GUILHERME MARINHO POZATI CORREA',
'GUSTAVO MATOS DE SOUSA',
'HELDER VIRISSIO ARAUJO',
'HUGO GUSTAVO MARTINS DA SILVA',
'JANELSON ARAUJO DE JESUS',
'JANIEL MELO DE SOUSA',
'JOHNNY DA SILVA FRANCO DE LIMA',
'KAYKE ALENCAR SILVA',
'LEONARDO FERNANDEZ RIBEIRO',
'LUCAS HENRIK RODRIGUES DE MEIRA',
'LUCIANO GOBETTI FILHO',
'LUIZ FELIPE SILVA GRAVA',
'LUIZ FERNANDO MENEZES',
'MACIEL DOS SANTOS',
'MARCOS VINICIUS DA SILVA ROCHA',
'MARCOS VINICIUS MARTINS DOS SANTOS',
'MICHAEL DOUGLAS DANTAS DA SILVA',
'NICOLAS ALVES DOS SANTOS',
'PEDRO HENRIQUE OLIVEIRA SILVA',
'RENATO ALVES PINTO',
'RYAN SANTOS OLIVEIRA',
'THIAGO MONTEIRO DO NASCIMENTO',
'VITOR ANTONIO ROMUALDO',
'YASMIN RODRIGUES DE ANDRADE',]

exibe(alunos)

chamada = executa_chamada(alunos)

presentes = filtra_chamada(chamada, 'p')
presentes.sort()

exibe_agradavel(presentes
