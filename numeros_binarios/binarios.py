import ttg
from time import sleep
cor = {'limpa':'\033[0m', 'vermelho':'\033[1;91m', 'verde':'\033[1;92m', 'ciano':'\033[1;96m',
       'amarelo':'\033[1;93m'}
# Titulo
print('-=' * 12)
print(f'{'NÚMEROS BINÁRIOS':^25}')
print('-=' * 12)
# Pedindo para o usuário escolher umas das opções
print('''ESCOLHA A OPÇÃO DESEJADA:
[ 1 ] CONVERSÃO DE BINÁRIOS PARA DÉCIMAL
[ 2 ] CONVERSÃO DE DÉCIMAL PARA BINÁRIO
[ 3 ] SOMANDO NÚMEROS BINÁRIOS
[ 4 ] VISUALIZAR A TABELA VERDADE
[ 5 ] REALIZAR CALCULOS EXPRESSÕES BOOLEANAS''')
escolhido = int(input('Digite o número da sua opção: '))
# Estrutura condicional aninhada para realização das operações que o
# usuário escolheu.
if escolhido == 1:
    #Titulo
    print('-' * 25)
    print(f'{'CONVERSOR DE DECIMAL':^25}\n'
          f'{'PARA BINÁRIO':^25}')
    print('-' * 25)
    # Perguntando ao usuário o valor da conversão
    valor = int(input('Digite um valor inteiro: '))
    # Calculo da conversão de décimal para binário
    binario = bin(valor)
    # Retornando o valor decimal e binário que o usuário escolheu
    print(f'VALOR INTEIRO: {valor}\n'
          f'VALOR BINÁRIO: {binario[2:]}')
elif escolhido == 2:
    # Titulo
    print('-' * 25)
    print(f'{'CONVERSOR DE BINÁRIO':^25}\n'
          f'{'PARA DÉCIMAL':^25}')
    print('-' * 25)
    # Pedindo ao usuário para digitar um valor em binário.
    binario = input('Digite um valor em binário: ')
    decimal = int(binario, 2)
    # Retornando ao usuário o valor convertido em decimal
    print(f'VALOR BINÁRIO: {binario}\n'
          f'VALOR INTEIRO: {decimal}')
elif escolhido == 3:
    # Titulo
    print('-' * 25)
    print(f'{'SOMANDO NÚMEROS ':^25}\n'
          f'{'BINÁRIOS':^25}')
    print('-' * 25)
    #Pedindo ao usuário para escolher uma das opções.
    print('ESCOLHA UMA DAS OPÇÕES ABAIXO:')
    print('[ 1 ] ADIÇÃO')
    print('[ 2 ] SUBTRAÇÃO')
    # Lendo a opção que o usuário escolheu.
    escolha = int(input('Digite o valor: '))
    # Adição
    if escolha == 1:
         print('QUANTAS PARCELAS DESEJA:')
         print('DIGITE [1] PARA DUAS PARCELAS')
         print('DIGITE [2] PARA TRÊS PARCELAS')
         print('DIGITE [3] PARA QUATRO PARCELAS')
         num = int(input('Digite aqui: '))
         if num == 1:
            print(f'CERTO. VAMOS REALIZAR A OPERAÇÃO.')
            n1_str = input('Primeiro valor binario: ') # Lendo o valor binário que o usuário escolheu
            n2_str = input('Segundo valor binario: ')
            n1_dec = int(n1_str, 2) # Transformando este valor de str para um valor inteiro
            n2_dec = int(n2_str, 2)
            somar_dec = n1_dec + n2_dec # Somando o valores convertidos para inteiros
            result_bin = bin(somar_dec) # Resultado dos valores inteiros em binários
            print('PROCESSANDO...')
            sleep(3)
            print('RESULTADO')
            print(f'A soma entre {n1_str} + {n2_str} é = {result_bin[2:]}')
         elif num == 2:
            print(f'CERTO. VAMOS REALIZAR AS OPERAÇÕES.')
            n1_str = input('Primeiro valor binário: ')
            n2_str = input('Segundo valor binário: ')
            n3_str = input('Terceiro valor binário: ')
            n1_dec = int(n1_str, 2)
            n2_dec = int(n2_str, 2)
            n3_dec = int(n3_str, 2)
            somar_dec = n1_dec + n2_dec + n3_dec
            result_bin = bin(somar_dec)
            print('PROCESSANDO...')
            sleep(3)
            print('RESULTADO')
            print(f'A soma entre {n1_str} + {n2_str} + {n3_str} é = {result_bin[2:]}')
         elif num == 3:
            print(f'CERTO. VAMOS REALIZAR AS OPERAÇÕES.')
            n1_str = input('Primeiro valor binário: ')
            n2_str = input('Segundo valor binário: ')
            n3_str = input('Terceiro valor binário: ')
            n4_str = input('Quarto valor binário: ')
            n1_dec = int(n1_str, 2)
            n2_dec = int(n2_str, 2)
            n3_dec = int(n3_str, 2)
            n4_dec = int(n4_str, 2)
            soma_dec = n1_dec + n2_dec + n3_dec + n4_dec
            result_bin = bin(soma_dec)
            print('PROCESANDO...')
            sleep(3)
            print('RESULTADO')
            print(f'A soma entre {n1_str} + {n2_str} + {n3_str} + {n4_str} é = {result_bin[2:]}')
         else:
             print(f'OPÇÃO {num} INVÁLIDA. TENTE NOVAMENTE.')
    else:
        print(f'OPÇÃO {escolha} INVÁLIDA. TENTE NOVAMENTE.')
    # Subtração
    if escolha == 2:
        print('QUANTAS PARCELAS DESEJA:')
        print('DIGITE [1] PARA DUAS PARCELAS')
        print('DIGITE [2] PARA TRÊS PARCELAS')
        print('DIGITE [3] PARA QUATRO PARCELAS')
        num = int(input('Digite aqui: '))
        if num == 1:
            print(f'CERTO. VAMOS REALIZAR A OPERAÇÃO.')
            n1_str = input('Primeiro valor binario: ') # Lendo o valor binário que o usuário escolheu
            n2_str = input('Segundo valor binario: ')
            n1_dec = int(n1_str, 2) # Transformando este valor de str para um valor inteiro
            n2_dec = int(n2_str, 2)
            somar_dec = n1_dec - n2_dec # Subtraindo o valores convertidos para inteiros
            result_bin = bin(somar_dec) # Resultado dos valores inteiros em binários
            print('PROCESSANDO...')
            sleep(3)
            print('RESULTADO')
            if n1_str < n2_str:
                result_format = f'{result_bin[0] + result_bin[3:]}'
                print(f'A subtração entre {n1_str} - {n2_str} é = {result_format}')
            else:
                print(f'A subtração entre {n1_str} - {n2_str} é = {result_bin[2:]}')
        elif num == 2:
            print(f'CERTO. VAMOS REALIZAR AS OPERAÇÕES.')
            n1_str = input('Primeiro valor binário: ')
            n2_str = input('Segundo valor binário: ')
            n3_str = input('Terceiro valor binário: ')
            n1_dec = int(n1_str, 2)
            n2_dec = int(n2_str, 2)
            n3_dec = int(n3_str, 2)
            somar_dec = n1_dec - n2_dec - n3_dec
            result_bin = bin(somar_dec)
            result_format = f'{result_bin[0] + result_bin[3:]}'
            print('PROCESSANDO...')
            sleep(3)
            print('RESULTADO')
            print(f'A subtração entre {n1_str} - {n2_str} - {n3_str} é = {result_format}')
        elif num == 3:
            print(f'CERTO. VAMOS REALIZAR AS OPERAÇÕES.')
            n1_str = input('Primeiro valor binário: ')
            n2_str = input('Segundo valor binário: ')
            n3_str = input('Terceiro valor binário: ')
            n4_str = input('Quarto valor binário: ')
            n1_dec = int(n1_str, 2)
            n2_dec = int(n2_str, 2)
            n3_dec = int(n3_str, 2)
            n4_dec = int(n4_str, 2)
            soma_dec = n1_dec - n2_dec - n3_dec - n4_dec
            result_bin = bin(soma_dec)
            result_format = f'{result_bin[0] + result_bin[3:]}'
            print('PROCESANDO...')
            sleep(3)
            print('RESULTADO')
            print(f'A subtração entre {n1_str} - {n2_str} - {n3_str} - {n4_str} é = {result_format}')
        else:
            print(f'OPÇÃO {num} INVÁLIDA. TENTE NOVAMENTE.')
elif escolhido == 4:
    print('QUANTAS PROPOSIÇÕES DESEJA?')
    print('[ 1 ] PARA UMA PROPOSIÇÃO: ["a"]')
    print('[ 2 ] PARA DUAS PROPOSIÇÕES: ["a","b"]')
    print('[ 3 ] PARA TÊS PROPOSIÇÕES: ["a","b", "c"]')
    print('[ 4 ] PARA QUATRO PROPOSIÇÕES: ["a","b", "c", "d"]')
    escolha = int(input('Digite aqui: '))
    if escolha == 1:
        tabela = ttg.Truths(['a'], ascending=True)
        tabela_str = str(tabela)
        tabela_str = tabela_str.replace('1', 'V').replace('0', 'F')
        tabela_colorida = ((((tabela_str.replace('F', f'{cor['vermelho']}0{cor['limpa']}').replace
                      ('V', f'{cor['verde']}1{cor['limpa']}')).replace
                      ('|', f'{cor['amarelo']}|{cor['limpa']}')).replace
                      ('+', f'{cor['amarelo']}+{cor['limpa']}')). replace
                      ('-', f'{cor['ciano']}-{cor['limpa']}'))
        print(tabela_colorida)
    elif escolha == 2:
        print(ttg.Truths(['a','b'], ascending=True))
    elif escolha == 3:
        print(ttg. Truths(['a', 'b', 'c'], ascending=True))
    elif escolha == 4:
        print(ttg.Truths(['a', 'b', 'c', 'd'], ascending=True))
    else:
        print(f'OPÇÃO {escolha} INVÁLIDA. TENTE NOVAMENTE.')

elif escolhido == 5:
    valor1 = input('Primeira proposição: ')
    valor2 = input('Segunda proposição: ')
    funcao = input('Qual o operador? ')
    neg = input('Esta negativado? ').upper().strip()
    tabela = input('ATÉ QUE PROPOSIÇÃO DESEJA IR? ').lower()
    if neg == 'SIM':
        print('O QUE ESTA NEGATIVADO?')
        print(f'OPÇÃO [1]: "{valor1}"')
        print(f'OPÇÃO [2]: "{valor2}"')
        print(f'OPÇÃO [3]: "{valor1} {funcao} {valor2}"')
        escolha = int(input('Digite a opção: '))
        if escolha == 1 and tabela == 'b':
            tabela = ttg.Truths(['a', 'b'], [f'(not {valor1}) {funcao} {valor2}'], ascending=True)
            print(tabela)
        elif escolha == 2 and tabela == 'b':
            tabela = ttg.Truths(['a', 'b'], [f'{valor1} {funcao} (not {valor2})'],
                                ascending=True)
            print(tabela)
        elif escolha == 3 and tabela == 'b':
            tabela = ttg.Truths(['a', 'b'], [f'not ({valor1} {funcao} {valor2})'],
                                ascending=True)
            print(tabela)
        if escolha == 1 and tabela == 'c':
            tabela = ttg.Truths(['a', 'b', 'c'], [f'(not {valor1}) {funcao} {valor2}'],
                                ascending=True)
            print(tabela)
        elif escolha == 2 and tabela == 'c':
            tabela = ttg.Truths(['a', 'b', 'c'], [f'{valor1} {funcao} (not {valor2})'],
                                ascending=True)
            print(tabela)
        elif escolha == 3 and tabela == 'c':
            tabela = ttg.Truths(['a', 'b', 'c'], [f'not ({valor1} {funcao} {valor2})'],
                                ascending=True)
            print(tabela)
        if escolha == 1 and tabela == 'd':
            tabela = ttg.Truths(['a', 'b', 'c', 'd'], [f'(not {valor1}) {funcao} {valor2}'],
                                ascending=True)
            print(tabela)
        elif escolha == 2 and tabela == 'd':
            tabela = ttg.Truths(['a', 'b', 'c', 'd'], [f'{valor1} {funcao} (not {valor2})'],
                                ascending=True)
            print(tabela)
        elif escolha == 3 and tabela == 'd':
            tabela = ttg.Truths(['a', 'b', 'c', 'd'], [f'not ({valor1} {funcao} {valor2})'],
                                ascending=True)
            print(tabela)
        else:
            print(f'OPÇÃO {tabela} INVÁLIDA. TENTE NOVAMENTE.')
    else:
        if tabela == 'b':
            tabela = ttg.Truths(['a', 'b'], [f'{valor1} {funcao} {valor2}'], ascending=True)
            print(tabela)
        elif tabela == 'c':
            tabela = ttg.Truths(['a', 'b', 'c'], [f'{valor1} {funcao} {valor2}'],
                                ascending=True)
            print(tabela)
        elif tabela == 'd':
            tabela = ttg.Truths(['a', 'b', 'c', 'd'], [f'{valor1} {funcao} {valor2}'],
                                ascending=True)
            print(tabela)
        else:
            print(f'OPÇÃO {tabela} INVÁLIDA. TENTE NOVAMENTE.')
else:
    print(f'OPÇÃO {escolhido} INVÁLIDA. TENTE NOVAMENTE.')
