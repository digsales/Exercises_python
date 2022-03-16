import datetime

ano = datetime.date.today().year
mes = datetime.date.today().month
dia = datetime.date.today().day

while True:
    try:
        nasc = int(input('Digite seu ano de nascimento: '))
        if nasc < ano - 150:
            print('\033[1;31m' + f'Digite um ano acima de {ano - 150}!' + '\033[0;0m')
        elif nasc > ano:
            print('\033[1;31m' + f'Digite um valor igual ou inferior a {ano}' + '\033[0;0m')
        else:
            if ano - nasc > 18:
                print('\033[1;32m' + 'MAIOR' + '\033[m')
            elif ano - nasc == 18:
                while True:
                    try:
                        mesnasc = int(input('Digite o número do MÊS de seu nascimento: '))
                        if mesnasc < 1 or mesnasc > 12:
                            print('\033[1;31m' + 'Por favor digite um valor entre 1 e 12!' + '\033[m')
                        else:
                            break
                    except:
                        print('\033[1;31m' + 'Por favor digite um valor inteiro!' + '\033[m')
                if mes < mesnasc:
                    print('\033[1;33m' + 'MENOR' + '\033[m')
                elif mes > mesnasc:
                    print('\033[1;32m' + 'MAIOR' + '\033[m')
                else:
                    while True:
                        try:
                            dianasc = int(input('Digite o número do DIA de seu nascimento: '))
                            if mesnasc in (1, 3, 5, 7, 8, 10, 12):
                                if dianasc < 1 or dianasc > 31:
                                    print('\033[1;31m' + 'Por favor digite um valor entre 1 e 31!' + '\033[m')
                                else:
                                    if dia < dianasc:
                                        print('\033[1;33m' + 'MENOR' + '\033[m')
                                    elif dia >= dianasc:
                                        print('\033[1;32m' + 'MAIOR' + '\033[m')
                                    break
                            elif mesnasc in (4, 6, 9, 11):
                                if dianasc < 1 or dianasc > 30:
                                    print('\033[1;31m' + 'Por favor digite um valor entre 1 e 30!' + '\033[m')
                                else:
                                    if dia < dianasc:
                                        print('\033[1;33m' + 'MENOR' + '\033[m')
                                    elif dia >= dianasc:
                                        print('\033[1;32m' + 'MAIOR' + '\033[m')
                                    break
                            else:
                                if ano % 4 == 0:
                                    if dianasc < 1 or dianasc > 29:
                                        print('\033[1;31m' + 'Por favor digite um valor entre 1 e 29!' + '\033[m')
                                    else:
                                        if dia < dianasc:
                                            print('\033[1;33m' + 'MENOR' + '\033[m')
                                        elif dia >= dianasc:
                                            print('\033[1;32m' + 'MAIOR' + '\033[m')
                                        break
                                else:
                                    if dianasc < 1 or dianasc > 28:
                                        print('\033[1;31m' + 'Por favor digite um valor entre 1 e 28!' + '\033[m')
                                    else:
                                        if dia < dianasc:
                                            print('\033[1;33m' + 'MENOR' + '\033[m')
                                        elif dia >= dianasc:
                                            print('\033[1;32m' + 'MAIOR' + '\033[m')
                                        break
                        except:
                            print('\033[1;31m' + 'Por favor digite um valor inteiro!' + '\033[m')
            else:
                print('\033[1;33m' + 'MENOR' + '\033[m')
            break
    except:
        print('\033[1;31m' + 'Por favor digite um valor inteiro!' + '\033[0;0m')
