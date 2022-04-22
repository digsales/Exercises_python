import datetime

ano = datetime.date.today().year
pessoa = dict()

while True:
    try:
        pessoa['nome'] = str(input('Nome: ')).strip().title()
        break
    except:
        print('\033[31mAlgo deu errado, tente novamente!\033[0m')
while True:
    try:
        pessoa['ano nascimento'] = int(input('Ano de nascimento: '))
        if pessoa['ano nascimento'] < (ano - 200) or pessoa['ano nascimento'] > ano:
            print('\033[31mDigite um ano válido!\033[0m')
        else:
            break
    except:
        print('\033[31mAlgo deu errado, tente novamente!\033[0m')
while True:
    try:
        pessoa['ctps'] = int(input('Carteira de trabalho (0 caso não possua): '))
        break
    except:
        print('\033[31mAlgo deu errado, tente novamente!\033[0m')

pessoa['idade'] = ano - pessoa['ano nascimento']

if pessoa['ctps'] != 0:
    while True:
        try:
            pessoa['contratacao'] = int(input('Ano de contratacao: '))
            if pessoa['contratacao'] < (ano - 200) or pessoa['contratacao'] > ano:
                print('\033[31mDigite um ano válido!\033[0m')
            else:
                break
        except:
            print('\033[31mAlgo deu errado, tente novamente!\033[0m')
    while True:
        try:
            pessoa['salario'] = float(input('Salário: R$'))
            break
        except:
            print('\033[31mAlgo deu errado, tente novamente!\033[0m')

if pessoa['ctps'] != 0:
    contribuicao = ano - pessoa['contratacao']
    if contribuicao < 35:
        pessoa['aposenta'] = f'em {35 - contribuicao} anos'
    else:
        pessoa['aposenta'] = 'APOSENTÁVEL'
print('—' * 30)
print(f'{"FICHA DE TRABALHO":^30}')
print('—'* 30)

for k, v in pessoa.items():
    if k == 'salario':
        print(f'{f"{k.upper()}:":>15} {f"R${v:.2f}":<15}')
    else:
        print(f'{f"{k.upper()}:":>15} {v:<15}')
print('—' * 30)
