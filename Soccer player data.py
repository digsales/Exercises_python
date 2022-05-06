lista = list()
jogador = dict()
gols = []
soma = 0

while True:
    while True:
        try:
            jogador['Nome'] = str(input('Nome do jogador: ')).strip().title()
            break
        except:
            print('\033[31mERROR! tente novamente!\033[0m')

    while True:
        try:
            jogos = int(input('Quantidade de partidas: '))
            break    
        except:
            print('\033[31mERROR! tente novamente!\033[0m')

    for c in range(0, jogos):
        while True:
            try:
                gol = int(input(f'Quantos gols na {c + 1}º partida: '))
                gols.append(gol)
                soma += gol
                break    
            except:
                print('\033[31mERROR! tente novamente!\033[0m')
    jogador['Gols'] = gols[:]
    jogador['Total de gols'] = soma
    soma = 0
    lista.append(jogador.copy())
    jogador.clear()
    gols.clear()
    while True:
        try:
            chave = str(input('Quer continuar? [S/N]: ')).strip().upper()
            if chave in 'SN':
                break
            else:
                print('\033[31mDigite S para continuar e N para parar!\033[0m')
        except:
            print('\033[31mERROR! tente novamente!\033[0m')
    if chave == 'S':
        pass
    else:
        break

print('—' * 50)
print(f'{"cod":<4}', end='')
print(f'{"nome":<16}', end='')
print(f'{"gols":<20}', end='')
print(f'{"total":<5}')
print('—' * 50)
for p, j in enumerate(lista):
    print(f'{p:<4}', end='')
    print(f'{j["Nome"]:<16}', end='')
    print(f'{str(j["Gols"]):20}', end='')
    print(f'{j["Total de gols"]:<5}')
print('—' * 50)

while True:
    while True:
        try:
            levantamento = int(input('Mostrar dados de qual jogador? [999 para encerrar]: '))
            if levantamento == 999:
                break
            elif levantamento < 0:
                print('\033[31mDigite um valor válido!\033[0m')
            elif levantamento > len(lista) - 1:
                print('\033[31mDigite um valor válido!\033[0m')
            else:
                break
        except:
            print('\033[31mERROR! Digite um valor inteiro!\033[0m')
    if levantamento == 999:
        print('<< ENCERRADO >>')
        break
    else:
        print('—' * 30)
        print(f"{lista[levantamento]['Nome'].upper()}")
        print('—' * 30)
        for p, g in enumerate(lista[levantamento]['Gols']):
            print(f'{f"{p + 1}ª Partida: ":>15} {f"{g} gols":<15}')
        print('—' * 30)
        print(f"TOTAL: {lista[levantamento]['Total de gols']} gols")
        print('—' * 30)
        print('')
