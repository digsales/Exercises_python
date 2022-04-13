from time import sleep
lista = []
aluno = []

while True:
    while True:
        try:
            nome = str(input('Nome: ')).strip().title()
            break
        except:
            print('\033[31mAlgo deu errado, tente novamente!\033[0m')
    while True:
        try:
            nota1 = float(input('Nota 1: '))
            if nota1 < 0:
                print('\033[31mDigite um valor 0 ou maior!\033[0m')
            else:
                break
        except:
            print('\033[31mDigite um valor válido!\033[0m')
    while True:
        try:
            nota2 = float(input('Nota 2: '))
            if nota2 < 0:
                print('\033[31mDigite um valor 0 ou maior!\033[0m')
            else:
                break
        except:
            print('\033[31mDigite um valor válido!\033[0m')
    aluno.append(nome)
    aluno.append(nota1)
    aluno.append(nota2)
    lista.append(aluno[:])
    aluno.clear()
    while True:
        try:
            continuar = str(input('Quer continuar [S/N]: '))
            if continuar in 'SsNn':
                break
            else:
                print('\033[31mDigite S ou N!\033[0m')
        except:
            print('\033[31mAlgo deu errado, tente novamente!\033[0m')
    if continuar in 'Ss':
        pass
    else:
        break
print('=-' * 30)
print('')
print('—' * 30)
print(f'{"Nº":<5}', end='')
print(f'{"NOME":<15}', end='')
print(f'{"MÉDIA":<10}', end='')
print('')
print('—' * 30)
for p, n in enumerate(lista):
    print(f'{p:<5}', end='')
    print(f'{n[0]:<15}', end='')
    print(f'{(n[1] + n[2]) / 2:<10}')
print('—' * 30)
print('\n')

while True:
    while True:
        try:
            chave = int(input('Mostrar notas de qual aluno [999 para parar]: '))
            if chave == 999:
                break
            if 0 > chave or chave > len(lista) - 1:
                print('\033[31mDigite um valor válido!\033[0m')
            else:
                break
        except:
            print('\033[31mDigite um valor inteiro!\033[0m')
    if chave == 999:
        print('Finalizando...')
        sleep(0.5)
        print('\033[1;32mAÇÂO FINALIZADA\033[0m')
        break
    else:
        for p, n in enumerate(lista):
            if p == chave:
                print(f'    Notas de {n[0]} são {n[1]} e {n[2]}.')
        print('')
