import ttg
from time import sleep
cor = {'limpa':'\033[0m', 'vermelho':'\033[1;91m', 'verde':'\033[1;92m', 'ciano':'\033[1;96m',
       'amarelo':'\033[1;93m', 'branco':'\033[1;97m', 'roxo':'\033[1;95m'}
# Titulo
print(f'{cor['branco']}-={cor['limpa']}' * 12)
print(f'{cor['ciano']}{'NÚMEROS BINÁRIOS':^25}{cor['limpa']}')
print(f'{cor['branco']}-={cor['limpa']}' * 12)
# Pedindo para o usuário escolher umas das opções
print(f'''{cor['amarelo']}ESCOLHA A OPÇÃO DESEJADA:{cor['limpa']}
{cor['verde']}[ 1 ]{cor['limpa']} {cor['branco']}CONVERSÃO DE DÉCIMAL PARA BINÁRIO{cor['limpa']}
{cor['verde']}[ 2 ]{cor['limpa']} {cor['branco']}CONVERSÃO DE BINÁRIO PARA DÉCIMAL{cor['limpa']}
{cor['verde']}[ 3 ]{cor['limpa']} {cor['branco']}SOMANDO NÚMEROS BINÁRIOS{cor['limpa']}
{cor['verde']}[ 4 ]{cor['limpa']} {cor['branco']}VISUALIZAR A TABELA VERDADE{cor['limpa']}
{cor['verde']}[ 5 ]{cor['limpa']} {cor['branco']}REALIZAR CALCULOS EXPRESSÕES BOOLEANAS{cor['limpa']}''')
escolhido = int(input(f'{cor['roxo']}DIGITE O NÚMERO DA SUA OPÇÃO: {cor['limpa']}'))
# Estrutura condicional aninhada para realização das operações que o
# usuário escolheu.
if escolhido == 1:
    #Titulo
    print(f'{cor['branco']}-{cor['limpa']}' * 25)
    print(f'{cor['ciano']}{'CONVERSOR DE DECIMAL':^25}\n'
          f'{'PARA BINÁRIO':^25}{cor['limpa']}')
    print(f'{cor['branco']}-{cor['limpa']}' * 25)
    # Perguntando ao usuário o valor da conversão
    valor = int(input(f'{cor['branco']}Digite um valor inteiro: {cor['limpa']}'))
    # Calculo da conversão de décimal para binário
    binario = bin(valor)
    binario_str = str(binario[2:])
    binario_str = binario_str.replace('1', 'V').replace('0', 'F')
    binario_colorido = (binario_str.replace('F', f'{cor['vermelho']}0{cor['limpa']}').replace
                        ('V', f'{cor['verde']}1{cor['limpa']}'))
    # Retornando o valor decimal e binário que o usuário escolheu
    print(f'{cor['verde']}VALOR INTEIRO{cor['limpa']}{cor['branco']}: {valor}{cor['limpa']}\n'
          f'{cor['verde']}VALOR BINÁRIO:{cor['limpa']} {binario_colorido}')
elif escolhido == 2:
    # Titulo
    titulo = f'CONVERSOR DE BINÁRIO'
    titulo2 = f'PARA DÉCIMAL'
    print(f'{cor['branco']}-{cor['limpa']}' * 25)
    print(f'{cor['ciano']}{titulo:^25}{cor['limpa']}')
    print(f'{cor['ciano']}{titulo2:^25}{cor['limpa']}')
    print(f'{cor['branco']}-{cor['limpa']}' * 25)
    # Pedindo ao usuário para digitar um valor em binário.
    binario = input(f'{cor['branco']}Digite um valor em binário: {cor['limpa']}')
    decimal = int(binario, 2)
    binario_str = str(binario)
    binario_str = binario_str.replace('1', 'V').replace('0', 'F')
    binario_colorido = (binario_str.replace('F', f'{cor['vermelho']}0{cor['limpa']}').replace
                        ('V', f'{cor['verde']}1{cor['limpa']}'))
    # Retornando ao usuário o valor convertido em decimal
    print(f'{cor['verde']}VALOR BINÁRIO{cor['limpa']}: {binario_colorido}\n'
          f'{cor['verde']}VALOR INTEIRO{cor['limpa']}{cor['branco']}: {decimal}{cor['limpa']}')
elif escolhido == 3:
    # Titulo
    titulo = f'SOMANDO NÚMEROS'
    titulo2 = f'BINÁRIOS'
    print(f'{cor['branco']}-{cor['limpa']}' * 25)
    print(f'{cor['ciano']}{titulo:^25}\n'
          f'{titulo2:^25}{cor['limpa']}')
    print(f'{cor['branco']}-{cor['limpa']}' * 25)
    #Pedindo ao usuário para escolher uma das opções.
    print(f'{cor['amarelo']}ESCOLHA UMA DAS OPÇÕES ABAIXO:{cor['limpa']}')
    print(f'{cor['verde']}[ 1 ]{cor['limpa']} {cor['branco']}ADIÇÃO{cor['limpa']}')
    print(f'{cor['verde']}[ 2 ]{cor['limpa']} {cor['branco']}SUBTRAÇÃO{cor['limpa']}')
    print(f'{cor['branco']}-{cor['limpa']}' * 25)
    # Lendo a opção que o usuário escolheu.
    escolha = int(input(f'{cor['roxo']}DIGITE A OPÇÃO: {cor['limpa']}'))
    print(f'{cor['branco']}-{cor['limpa']}' * 25)
    # Adição
    if escolha == 1:
            print(f'{cor['amarelo']}QUANTAS PARCELAS DESEJA:{cor['limpa']}')
            print(f'{cor['branco']}DIGITE{cor['limpa']} {cor['verde']}[1]{cor['limpa']} '
               f'{cor['branco']}PARA DUAS PARCELAS{cor['limpa']}')
            print(f'{cor['branco']}DIGITE{cor['limpa']} {cor['verde']}[2]{cor['limpa']} '
               f'{cor['branco']}PARA TRÊS PARCELAS{cor['limpa']}')
            print(f'{cor['branco']}DIGITE{cor['limpa']} {cor['verde']}[3]{cor['limpa']} '
                  f'{cor['branco']}PARA QUATRO PARCELAS{cor['limpa']}')
            print(f'{cor['branco']}-{cor['limpa']}' * 25)
            num = int(input(f'{cor['roxo']}DIGITE AQUI: {cor['limpa']}'))
            print(f'{cor['branco']}-{cor['limpa']}' * 25)
            if num == 1:
                print(f'{cor['verde']}CERTO. VAMOS REALIZAR A OPERAÇÃO.{cor['limpa']}')
                # Lendo o valor binário que o usuário escolheu
                n1_str = input(f'{cor['branco']}Primeira Parcela: {cor['limpa']}')
                n2_str = input(f'{cor['branco']}Segunda Parcela: {cor['limpa']}')
                n1_dec = int(n1_str, 2) # Transformando este valor de str para um valor inteiro
                n2_dec = int(n2_str, 2)
                somar_dec = n1_dec + n2_dec # Somando o valores convertidos para inteiros
                result_bin = bin(somar_dec) # Resultado dos valores inteiros em binários
                result_str = str(result_bin[2:])
                result_str = result_str.replace('1', 'V').replace('0', 'F')
                n1_str = n1_str.replace('1', 'V').replace('0', 'F')
                n2_str = n2_str.replace('1', 'V').replace('0', 'F')
                n1_colorido = (n1_str.replace('F', f'{cor['vermelho']}0{cor['limpa']}').replace
                               ('V', f'{cor['verde']}1{cor['limpa']}'))
                n2_colorido = (n2_str.replace('F', f'{cor['vermelho']}0{cor['limpa']}').replace
                               ('V', f'{cor['verde']}1{cor['limpa']}'))
                result_colorido = (result_str.replace('F', f'{cor['vermelho']}0{cor['limpa']}').replace
                                ('V', f'{cor['verde']}1{cor['limpa']}'))
                print(f'{cor['branco']}-{cor['limpa']}' * 25)
                processando = 'PROCESSANDO...'
                print(f'{cor['roxo']}{processando:^25}{cor['limpa']}')
                print(f'{cor['branco']}-{cor['limpa']}' * 25)
                sleep(3)
                print(f'{cor['verde']}RESULTADO{cor['limpa']}')
                print(f'{cor['branco']}A soma entre{cor['limpa']} {n1_colorido} {cor['branco']}+{cor['limpa']} '
                  f'{n2_colorido} {cor['branco']}é ={cor['limpa']} {result_colorido}')
            elif num == 2:
                print(f'{cor['verde']}CERTO. VAMOS REALIZAR AS OPERAÇÕES.{cor['limpa']}')
                n1_str = input(f'{cor['branco']}Primeira Parcela: {cor['limpa']}')
                n2_str = input(f'{cor['branco']}Segunda Parcela: {cor['limpa']}')
                n3_str = input(f'{cor['branco']}Terceira Parcela: {cor['limpa']}')
                n1_dec = int(n1_str, 2)
                n2_dec = int(n2_str, 2)
                n3_dec = int(n3_str, 2)
                somar_dec = n1_dec + n2_dec + n3_dec
                result_bin = bin(somar_dec)
                result_str = str(result_bin[2:])
                result_str = result_str.replace('1', 'V').replace('0', 'F')
                n1_str = n1_str.replace('1', 'V').replace('0', 'F')
                n2_str = n2_str.replace('1', 'V').replace('0', 'F')
                n3_str = n3_str.replace('1', 'V').replace('0', 'F')
                n1_colorido = (n1_str.replace('F', f'{cor['vermelho']}0{cor['limpa']}').replace
                           ('V', f'{cor['verde']}1{cor['limpa']}'))
                n2_colorido = (n2_str.replace('F', f'{cor['vermelho']}0{cor['limpa']}').replace
                           ('V', f'{cor['verde']}1{cor['limpa']}'))
                n3_colorido = (n3_str.replace('F', f'{cor['vermelho']}0{cor['limpa']}').replace
                           ('V', f'{cor['verde']}1{cor['limpa']}'))
                result_colorido = (result_str.replace('F', f'{cor['vermelho']}0{cor['limpa']}').replace
                               ('V', f'{cor['verde']}1{cor['limpa']}'))
                print(f'{cor['branco']}-{cor['limpa']}' * 25)
                processando = 'PROCESSANDO...'
                print(f'{cor['roxo']}{processando:^25}{cor['limpa']}')
                print(f'{cor['branco']}-{cor['limpa']}' * 25)
                sleep(3)
                print(f'{cor['verde']}RESULTADO{cor['limpa']}')
                print(f'{cor['branco']}A soma entre{cor['limpa']} {n1_colorido} {cor['branco']}+{cor['limpa']} '
                  f'{n2_colorido} {cor['branco']}+{cor['limpa']} {n3_colorido} '
                  f'{cor['branco']}é ={cor['limpa']} {result_colorido}')
            elif num == 3:
                print(f'{cor['verde']}CERTO. VAMOS REALIZAR AS OPERAÇÕES.{cor['limpa']}')
                n1_str = input(f'{cor['branco']}Primeira Parcela: {cor['limpa']}')
                n2_str = input(f'{cor['branco']}Segunda Parcela: {cor['limpa']}')
                n3_str = input(f'{cor['branco']}Terceira Parcela: {cor['limpa']}')
                n4_str = input(f'{cor['branco']}Quarta Parcela: {cor['limpa']}')
                n1_dec = int(n1_str, 2)
                n2_dec = int(n2_str, 2)
                n3_dec = int(n3_str, 2)
                n4_dec = int(n4_str, 2)
                soma_dec = n1_dec + n2_dec + n3_dec + n4_dec
                result_bin = bin(soma_dec)
                result_str = str(result_bin[2:])
                result_str = result_str.replace('1', 'V').replace('0', 'F')
                n1_str = n1_str.replace('1', 'V').replace('0', 'F')
                n2_str = n2_str.replace('1', 'V').replace('0', 'F')
                n3_str = n3_str.replace('1', 'V').replace('0', 'F')
                n4_str = n4_str.replace('1', 'V').replace('0', 'F')
                n1_colorido = (n1_str.replace('F', f'{cor['vermelho']}0{cor['limpa']}').replace
                               ('V', f'{cor['verde']}1{cor['limpa']}'))
                n2_colorido = (n2_str.replace('F', f'{cor['vermelho']}0{cor['limpa']}').replace
                               ('V', f'{cor['verde']}1{cor['limpa']}'))
                n3_colorido = (n3_str.replace('F', f'{cor['vermelho']}0{cor['limpa']}').replace
                               ('V', f'{cor['verde']}1{cor['limpa']}'))
                n4_colorido = (n4_str.replace('F', f'{cor['vermelho']}0{cor['limpa']}').replace
                               ('V', f'{cor['verde']}1{cor['limpa']}'))
                result_colorido = (result_str.replace('F', f'{cor['vermelho']}0{cor['limpa']}').replace
                                   ('V', f'{cor['verde']}1{cor['limpa']}'))
                print(f'{cor['branco']}-{cor['limpa']}' * 25)
                processando = 'PROCESSANDO...'
                print(f'{cor['roxo']}{processando:^25}{cor['limpa']}')
                print(f'{cor['branco']}-{cor['limpa']}' * 25)
                sleep(3)
                print(f'{cor['verde']}RESULTADO{cor['limpa']}')
                print(f'{cor['branco']}A soma entre{cor['limpa']} {n1_colorido} {cor['branco']}+{cor['limpa']} '
                      f'{n2_colorido} {cor['branco']}+{cor['limpa']} {n3_colorido} '
                      f'{cor['branco']}+{cor['limpa']} {n4_colorido}{cor['branco']} é ={cor['limpa']} {result_colorido}')
            else:
                 print(f'{cor['vermelho']}OPÇÃO {num} INVÁLIDA. TENTE NOVAMENTE.{cor['limpa']}')
        # Subtração
    elif escolha == 2:
            print(f'{cor['amarelo']}QUANTAS PARCELAS DESEJA:{cor['limpa']}')
            print(f'{cor['branco']}DIGITE{cor['limpa']} {cor['verde']}[1]{cor['limpa']} '
                  f'{cor['branco']}PARA DUAS PARCELAS{cor['limpa']}')
            print(f'{cor['branco']}DIGITE{cor['limpa']} {cor['verde']}[2]{cor['limpa']} '
                  f'{cor['branco']}PARA TRÊS PARCELAS{cor['limpa']}')
            print(f'{cor['branco']}DIGITE{cor['limpa']} {cor['verde']}[3]{cor['limpa']} '
                  f'{cor['branco']}PARA QUATRO PARCELAS{cor['limpa']}')
            print(f'{cor['branco']}-{cor['limpa']}' * 25)
            num = int(input(f'{cor['roxo']}DIGITE AQUI: {cor['limpa']}'))
            print(f'{cor['branco']}-{cor['limpa']}' * 25)
            if num == 1:
                print(f'{cor['verde']}CERTO. VAMOS REALIZAR A OPERAÇÃO.{cor['limpa']}')
                # Lendo o valor binário que o usuário escolheu
                n1_str = input(f'{cor['branco']}Primeira Parcela: {cor['limpa']}')
                n2_str = input(f'{cor['branco']}Segunda Parcela: {cor['limpa']}')
                n1_dec = int(n1_str, 2) # Transformando este valor de str para um valor inteiro
                n2_dec = int(n2_str, 2)
                somar_dec = n1_dec - n2_dec # Subtraindo o valores convertidos para inteiros
                result_bin = bin(somar_dec) # Resultado dos valores inteiros em binários
                result_str = str(result_bin[2:])
                result_str = result_str.replace('1', 'V').replace('0', 'F')
                n1_str = n1_str.replace('1', 'V').replace('0', 'F')
                n2_str = n2_str.replace('1', 'V').replace('0', 'F')
                n1_colorido = (n1_str.replace('F', f'{cor['vermelho']}0{cor['limpa']}').replace
                               ('V', f'{cor['verde']}1{cor['limpa']}'))
                n2_colorido = (n2_str.replace('F', f'{cor['vermelho']}0{cor['limpa']}').replace
                               ('V', f'{cor['verde']}1{cor['limpa']}'))
                result_colorido = (result_str.replace('F', f'{cor['vermelho']}0{cor['limpa']}').replace
                                   ('V', f'{cor['verde']}1{cor['limpa']}'))
                print(f'{cor['branco']}-{cor['limpa']}' * 25)
                processando = 'PROCESSANDO...'
                print(f'{cor['roxo']}{processando:^25}{cor['limpa']}')
                print(f'{cor['branco']}-{cor['limpa']}' * 25)
                sleep(3)
                print(f'{cor['verde']}RESULTADO{cor['limpa']}')
                if somar_dec < 0:
                    result_format = f'{result_bin[0] + result_bin[3:]}'
                    result_str = str(result_format)
                    result_str = result_str.replace('1', 'V').replace('0', 'F')
                    result_colorido1 = ((result_str.replace('-', f'{cor['vermelho']}-{cor['limpa']}').replace
                                       ('F', f'{cor['vermelho']}0{cor['limpa']}')).replace
                                       ('V', f'{cor['verde']}1{cor['limpa']}'))
                    print(f'A subtração entre {n1_colorido} - {n2_colorido} é = {result_colorido1}')
                else:
                    print(f'A subtração entre {n1_colorido} - {n2_colorido} é = {result_colorido}')
            elif num == 2:
                print(f'{cor['verde']}CERTO. VAMOS REALIZAR AS OPERAÇÕES.{cor['limpa']}')
                n1_str = input(f'{cor['branco']}Primeira Parcela: {cor['limpa']}')
                n2_str = input(f'{cor['branco']}Segunda Parcela: {cor['limpa']}')
                n3_str = input(f'{cor['branco']}Terceira Parcela: {cor['limpa']}')
                n1_dec = int(n1_str, 2)
                n2_dec = int(n2_str, 2)
                n3_dec = int(n3_str, 2)
                somar_dec = n1_dec - n2_dec - n3_dec
                somar_str = str(somar_dec)
                result_bin = bin(somar_dec)
                result_str = str(result_bin[2:])
                result_str = result_str.replace('1', 'V').replace('0', 'F')
                n1_str = n1_str.replace('1', 'V').replace('0', 'F')
                n2_str = n2_str.replace('1', 'V').replace('0', 'F')
                n3_str = n3_str.replace('1', 'V').replace('0', 'F')
                n1_colorido = (n1_str.replace('F', f'{cor['vermelho']}0{cor['limpa']}').replace
                               ('V', f'{cor['verde']}1{cor['limpa']}'))
                n2_colorido = (n2_str.replace('F', f'{cor['vermelho']}0{cor['limpa']}').replace
                               ('V', f'{cor['verde']}1{cor['limpa']}'))
                n3_colorido = (n3_str.replace('F', f'{cor['vermelho']}0{cor['limpa']}').replace
                               ('V', f'{cor['verde']}1{cor['limpa']}'))
                result_colorido = ((result_str.replace('F', f'{cor['vermelho']}0{cor['limpa']}')).replace
                                       ('V', f'{cor['verde']}1{cor['limpa']}'))
                print(f'{cor['branco']}-{cor['limpa']}' * 25)
                processando = 'PROCESSANDO...'
                print(f'{cor['roxo']}{processando:^25}{cor['limpa']}')
                print(f'{cor['branco']}-{cor['limpa']}' * 25)
                sleep(3)
                print(f'{cor['verde']}RESULTADO{cor['limpa']}')
                if somar_dec < 0:
                    result_format = f'{result_bin[0] + result_bin[3:]}'
                    result_str = str(result_format)
                    result_str = result_str.replace('1', 'V').replace('0', 'F')
                    result_colorido1 = ((result_str.replace('-', f'{cor['vermelho']}-{cor['limpa']}').replace
                                         ('F', f'{cor['vermelho']}0{cor['limpa']}')).replace
                                        ('V', f'{cor['verde']}1{cor['limpa']}'))
                    print(f'A subtração entre {n1_colorido} - {n2_colorido} - {n3_colorido} é = {result_colorido1}')
                else:
                    print(f'A subtração entr {n1_colorido} - {n2_colorido} - {n3_colorido} é = {result_colorido}')
            elif num == 3:
                print(f'{cor['verde']}CERTO. VAMOS REALIZAR AS OPERAÇÕES.{cor['limpa']}')
                n1_str = input(f'{cor['branco']}Primeira Parcela: {cor['limpa']}')
                n2_str = input(f'{cor['branco']}Segunda Parcela: {cor['limpa']}')
                n3_str = input(f'{cor['branco']}Terceira Parcela: {cor['limpa']}')
                n4_str = input(f'{cor['branco']}Terceira Parcela: {cor['limpa']}')
                n1_dec = int(n1_str, 2)
                n2_dec = int(n2_str, 2)
                n3_dec = int(n3_str, 2)
                n4_dec = int(n4_str, 2)
                somar_dec = n1_dec - n2_dec - n3_dec - n4_dec
                result_bin = bin(somar_dec)
                result_str = str(result_bin[2:])
                result_str = result_str.replace('1', 'V').replace('0', 'F')
                n1_str = n1_str.replace('1', 'V').replace('0', 'F')
                n2_str = n2_str.replace('1', 'V').replace('0', 'F')
                n3_str = n3_str.replace('1', 'V').replace('0', 'F')
                n4_str = n4_str.replace('1', 'V').replace('0', 'F')
                n1_colorido = (n1_str.replace('F', f'{cor['vermelho']}0{cor['limpa']}').replace
                               ('V', f'{cor['verde']}1{cor['limpa']}'))
                n2_colorido = (n2_str.replace('F', f'{cor['vermelho']}0{cor['limpa']}').replace
                               ('V', f'{cor['verde']}1{cor['limpa']}'))
                n3_colorido = (n3_str.replace('F', f'{cor['vermelho']}0{cor['limpa']}').replace
                               ('V', f'{cor['verde']}1{cor['limpa']}'))
                n4_colorido = (n4_str.replace('F', f'{cor['vermelho']}0{cor['limpa']}').replace
                               ('V', f'{cor['verde']}1{cor['limpa']}'))
                result_colorido = ((result_str.replace('F', f'{cor['vermelho']}0{cor['limpa']}')).replace
                                   ('V', f'{cor['verde']}1{cor['limpa']}'))
                print(f'{cor['branco']}-{cor['limpa']}' * 25)
                processando = 'PROCESSANDO...'
                print(f'{cor['roxo']}{processando:^25}{cor['limpa']}')
                print(f'{cor['branco']}-{cor['limpa']}' * 25)
                sleep(3)
                print(f'{cor['verde']}RESULTADO{cor['limpa']}')
                if somar_dec < 0:
                    result_format = f'{result_bin[0] + result_bin[3:]}'
                    result_str = str(result_format)
                    result_str = result_str.replace('1', 'V').replace('0', 'F')
                    result_colorido1 = ((result_str.replace('-', f'{cor['vermelho']}-{cor['limpa']}').replace
                                         ('F', f'{cor['vermelho']}0{cor['limpa']}')).replace
                                        ('V', f'{cor['verde']}1{cor['limpa']}'))
                    print(f'A subtração entre {n1_colorido} - {n2_colorido} - {n3_colorido} - {n4_colorido} '
                          f'é = {result_colorido1}')
                else:
                    print(f'A subtração entre {n1_colorido} - {n2_colorido} - {n3_colorido} - {n4_colorido} '
                          f'é = {result_colorido}')
            else:
                print(f'{cor['vermelho']}OPÇÃO {num} INVÁLIDA. TENTE NOVAMENTE.{cor['limpa']}')
    else:
        print(f'{cor['vermelho']}OPÇÃO {escolha} INVÁLIDA. TENTE NOVAMENTE.{cor['limpa']}')
elif escolhido == 4:
        print(f'{cor['branco']}-{cor['limpa']}' * 25)
        print(f'{cor['amarelo']}QUANTAS PROPOSIÇÕES DESEJA?{cor['limpa']}')
        print(f'{cor['verde']}[ 1 ]{cor['limpa']} {cor['branco']}PARA UMA PROPOSIÇÃO: ["a"]{cor['limpa']}')
        print(f'{cor['verde']}[ 2 ]{cor['limpa']} {cor['branco']}PARA DUAS PROPOSIÇÃO: ["a", "b"]{cor['limpa']}')
        print(f'{cor['verde']}[ 3 ]{cor['limpa']} {cor['branco']}PARA TRÊS PROPOSIÇÃO: ["a","b","c"]{cor['limpa']}')
        print(f'{cor['verde']}[ 4 ]{cor['limpa']} {cor['branco']}PARA QUATRO PROPOSIÇÃO: '
              f'["a","b","c","d"]{cor['limpa']}')
        escolha = int(input(f'{cor['roxo']}DIGITE AQUI: {cor['limpa']}'))
        if escolha == 1:
            tabela = ttg.Truths(['a'], ascending=True)
            tabela_str = str(tabela)
            tabela_str = tabela_str.replace('1', 'V').replace('0', 'F')
            tabela_colorida = (((((tabela_str.replace('F', f'{cor['vermelho']}0{cor['limpa']}').replace
                          ('V', f'{cor['verde']}1{cor['limpa']}')).replace
                          ('|', f'{cor['amarelo']}|{cor['limpa']}')).replace
                          ('+', f'{cor['amarelo']}+{cor['limpa']}')).replace
                          ('-', f'{cor['ciano']}-{cor['limpa']}')).replace
                          ('a', f'{cor['branco']}a{cor['limpa']}'))
            print(tabela_colorida)
        elif escolha == 2:
            tabela = ttg.Truths(['a', 'b'], ascending=True)
            tabela_str = str(tabela)
            tabela_str = tabela_str.replace('1', 'V').replace('0', 'F')
            tabela_colorida = (((((((tabela_str.replace('F', f'{cor['vermelho']}0{cor['limpa']}').replace
                            ('V', f'{cor['verde']}1{cor['limpa']}')).replace
                            ('|', f'{cor['amarelo']}|{cor['limpa']}')).replace
                            ('+', f'{cor['amarelo']}+{cor['limpa']}')).replace
                            ('-', f'{cor['ciano']}-{cor['limpa']}'))).replace
                            ('a', f'{cor['branco']}a{cor['limpa']}')).replace
                            ('b', f'{cor['branco']}b{cor['limpa']}'))
            print(tabela_colorida)
        elif escolha == 3:
            tabela = ttg. Truths(['a', 'b', 'c'], ascending=True)
            tabela_str = str(tabela)
            tabela_str = tabela_str.replace('1', 'V').replace('0', 'F')
            tabela_colorida = (((((((tabela_str.replace('F', f'{cor['vermelho']}0{cor['limpa']}').replace
                            ('V', f'{cor['verde']}1{cor['limpa']}')).replace
                            ('|', f'{cor['amarelo']}|{cor['limpa']}')).replace
                            ('+', f'{cor['amarelo']}+{cor['limpa']}')).replace
                            ('-', f'{cor['ciano']}-{cor['limpa']}')).replace
                            ('a', f'{cor['branco']}a{cor['limpa']}')).replace
                            ('b', f'{cor['branco']}b{cor['limpa']}')).replace
                            ('c', f'{cor['branco']}c{cor['limpa']}'))
            print(tabela_colorida)
        elif escolha == 4:
            tabela = ttg.Truths(['a', 'b', 'c', 'd'], ascending=True)
            tabela_str = str(tabela)
            tabela_str = tabela_str.replace('1', 'V').replace('0', 'F')
            tabela_colorida = ((((((((tabela_str.replace('F', f'{cor['vermelho']}0{cor['limpa']}').replace
                            ('V', f'{cor['verde']}1{cor['limpa']}')).replace
                            ('|', f'{cor['amarelo']}|{cor['limpa']}')).replace
                            ('+', f'{cor['amarelo']}+{cor['limpa']}')).replace
                            ('-', f'{cor['ciano']}-{cor['limpa']}')).replace
                            ('a', f'{cor['branco']}a{cor['limpa']}')).replace
                            ('b', f'{cor['branco']}b{cor['limpa']}')).replace
                            ('c', f'{cor['branco']}c{cor['limpa']}')).replace
                            ('d', f'{cor['branco']}d{cor['limpa']}'))
            print(tabela_colorida)
        else:
            print(f'{cor['vermelho']}OPÇÃO {escolha} INVÁLIDA. TENTE NOVAMENTE.{cor['limpa']}')

elif escolhido == 5:
        titulo = 'EXPRESSÕES BOOLEANAS'
        print(f'{cor['branco']}-{cor['limpa']}' * 25)
        print(f'{cor['ciano']}{titulo:^25}{cor['limpa']}')
        print(f'{cor['branco']}-{cor['limpa']}' * 25)
        valor1 = input(f'{cor['branco']}Primeira Proposição: {cor['limpa']}')
        valor2 = input(f'{cor['branco']}Segunda Proposição: {cor['limpa']}')
        funcao = input(f'{cor['branco']}Qual o Operador? {cor['limpa']}')
        if funcao == 'and' or funcao == 'or':
            neg = input(f'{cor['vermelho']}Esta Negativado? {cor['limpa']}').upper().strip()
            tabela = input(f'{cor['branco']}ATÉ QUE PROPOSIÇÃO DESEJA IR? {cor['limpa']}').lower()
            if neg == 'SIM':
                print(f'{cor['amarelo']}O QUE ESTA NEGATIVADO?{cor['limpa']}')
                print(f'{cor['branco']}OPÇÃO{cor ['limpa']} {cor['verde']}[1]{cor['limpa']}'
                      f'{cor['branco']}: "{cor['limpa']}'
                      f'{cor['vermelho']}not ({valor1}){cor['limpa']}{cor['branco']}"{cor['limpa']}')
                print(f'{cor['branco']}OPÇÃO{cor ['limpa']} {cor['verde']}[2]{cor['limpa']}'
                      f'{cor['branco']}: "{cor['limpa']}{cor['vermelho']}not ({valor2}){cor['limpa']}'
                      f'{cor['branco']}"{cor['limpa']}')
                print(f'{cor['branco']}OPÇÃO{cor ['limpa']} {cor['verde']}[3]{cor['limpa']}'
                      f'{cor['branco']}: "{cor['limpa']}{cor['vermelho']}'
                      f'not ({valor1} {funcao} {valor2}){cor['limpa']}{cor['branco']}"{cor['limpa']}')
                escolha = int(input(f'{cor['roxo']}DIGITE A OPÇÃO: {cor['limpa']}'))
                if escolha == 1 and tabela == 'b':
                    tabela = ttg.Truths(['a', 'b'], [f'(not {valor1}) {funcao} {valor2}'],
                                        ascending=True)
                    tabela_str = str(tabela)
                    tabela_str = tabela_str.replace('1', 'V').replace('0', 'F')
                    tabela_colorida = (((((((((((tabela_str.replace
                                ('F', f'{cor['vermelho']}0{cor['limpa']}').replace
                                ('V', f'{cor['verde']}1{cor['limpa']}')).replace
                                ('|', f'{cor['amarelo']}|{cor['limpa']}')).replace
                                ('+', f'{cor['amarelo']}+{cor['limpa']}')).replace
                                ('-', f'{cor['ciano']}-{cor['limpa']}')).replace
                                ('a', f'{cor['branco']}a{cor['limpa']}')).replace
                                ('b', f'{cor['branco']}b{cor['limpa']}')).replace
                                ('not', f'{cor['branco']}not{cor['limpa']}')).replace
                                ('or', f'{cor['branco']}or{cor['limpa']}')).replace
                                ('nd', f'{cor['branco']}nd{cor['limpa']}')).replace
                                ('(', f'{cor['branco']}({cor['limpa']}')).replace
                                (')', f'{cor['branco']}){cor['limpa']}'))
                    print(tabela_colorida)
                elif escolha == 2 and tabela == 'b':
                    tabela = ttg.Truths(['a', 'b'], [f'{valor1} {funcao} (not {valor2})'],
                                        ascending=True)
                    tabela_str = str(tabela)
                    tabela_str = tabela_str.replace('1', 'V').replace('0', 'F')
                    tabela_colorida = (((((((((((tabela_str.replace
                                ('F', f'{cor['vermelho']}0{cor['limpa']}').replace
                                ('V', f'{cor['verde']}1{cor['limpa']}')).replace
                                ('|', f'{cor['amarelo']}|{cor['limpa']}')).replace
                                ('+', f'{cor['amarelo']}+{cor['limpa']}')).replace
                                ('-', f'{cor['ciano']}-{cor['limpa']}')).replace
                                ('a', f'{cor['branco']}a{cor['limpa']}')).replace
                                ('b', f'{cor['branco']}b{cor['limpa']}')).replace
                                ('not', f'{cor['branco']}not{cor['limpa']}')).replace
                                ('or', f'{cor['branco']}or{cor['limpa']}')).replace
                                ('nd', f'{cor['branco']}nd{cor['limpa']}')).replace
                                ('(', f'{cor['branco']}({cor['limpa']}')).replace
                                (')', f'{cor['branco']}){cor['limpa']}'))
                    print(tabela_colorida)
                elif escolha == 3 and tabela == 'b':
                    tabela = ttg.Truths(['a', 'b'], [f'not ({valor1} {funcao} {valor2})'],
                                        ascending=True)
                    tabela_str = str(tabela)
                    tabela_str = tabela_str.replace('1', 'V').replace('0', 'F')
                    tabela_colorida = (((((((((((tabela_str.replace
                                ('F', f'{cor['vermelho']}0{cor['limpa']}').replace
                                ('V', f'{cor['verde']}1{cor['limpa']}')).replace
                                ('|', f'{cor['amarelo']}|{cor['limpa']}')).replace
                                ('+', f'{cor['amarelo']}+{cor['limpa']}')).replace
                                ('-', f'{cor['ciano']}-{cor['limpa']}')).replace
                                ('a', f'{cor['branco']}a{cor['limpa']}')).replace
                                ('b', f'{cor['branco']}b{cor['limpa']}')).replace
                                ('not', f'{cor['branco']}not{cor['limpa']}')).replace
                                ('or', f'{cor['branco']}or{cor['limpa']}')).replace
                                ('nd', f'{cor['branco']}nd{cor['limpa']}')).replace
                                ('(', f'{cor['branco']}({cor['limpa']}')).replace
                                (')', f'{cor['branco']}){cor['limpa']}'))
                    print(tabela_colorida)
                elif escolha == 1 and tabela == 'c':
                    tabela = ttg.Truths(['a', 'b', 'c'], [f'(not {valor1}) {funcao} {valor2}'],
                                        ascending=True)
                    tabela_str = str(tabela)
                    tabela_str = tabela_str.replace('1', 'V').replace('0', 'F')
                    tabela_colorida = ((((((((((((tabela_str.replace
                                ('F', f'{cor['vermelho']}0{cor['limpa']}').replace
                                ('V', f'{cor['verde']}1{cor['limpa']}')).replace
                                ('|', f'{cor['amarelo']}|{cor['limpa']}')).replace
                                ('+', f'{cor['amarelo']}+{cor['limpa']}')).replace
                                ('-', f'{cor['ciano']}-{cor['limpa']}')).replace
                                ('a', f'{cor['branco']}a{cor['limpa']}')).replace
                                ('b', f'{cor['branco']}b{cor['limpa']}')).replace
                                ('c', f'{cor['branco']}c{cor['limpa']}')).replace
                                ('not', f'{cor['branco']}not{cor['limpa']}')).replace
                                ('or', f'{cor['branco']}or{cor['limpa']}')).replace
                                ('nd', f'{cor['branco']}nd{cor['limpa']}')).replace
                                ('(', f'{cor['branco']}({cor['limpa']}')).replace
                                (')', f'{cor['branco']}){cor['limpa']}'))
                    print(tabela_colorida)
                elif escolha == 2 and tabela == 'c':
                    tabela = ttg.Truths(['a', 'b', 'c'], [f'{valor1} {funcao} (not {valor2})'],
                                        ascending=True)
                    tabela_str = str(tabela)
                    tabela_str = tabela_str.replace('1', 'V').replace('0', 'F')
                    tabela_colorida = ((((((((((((tabela_str.replace
                                ('F',f'{cor['vermelho']}0{cor['limpa']}').replace
                                ('V', f'{cor['verde']}1{cor['limpa']}')).replace
                                ('|', f'{cor['amarelo']}|{cor['limpa']}')).replace
                                ('+', f'{cor['amarelo']}+{cor['limpa']}')).replace
                                ('-', f'{cor['ciano']}-{cor['limpa']}')).replace
                                ('a', f'{cor['branco']}a{cor['limpa']}')).replace
                                ('b', f'{cor['branco']}b{cor['limpa']}')).replace
                                ('c', f'{cor['branco']}c{cor['limpa']}')).replace
                                ('not', f'{cor['branco']}not{cor['limpa']}')).replace
                                ('or', f'{cor['branco']}or{cor['limpa']}')).replace
                                ('nd', f'{cor['branco']}nd{cor['limpa']}')).replace
                                ('(', f'{cor['branco']}({cor['limpa']}')).replace
                                (')', f'{cor['branco']}){cor['limpa']}'))
                    print(tabela_colorida)
                elif escolha == 3 and tabela == 'c':
                    tabela = ttg.Truths(['a', 'b', 'c'], [f'not ({valor1} {funcao} {valor2})'],
                                        ascending=True)
                    tabela_str = str(tabela)
                    tabela_str = tabela_str.replace('1', 'V').replace('0', 'F')
                    tabela_colorida = ((((((((((((tabela_str.replace
                                ('F', f'{cor['vermelho']}0{cor['limpa']}').replace
                                ('V', f'{cor['verde']}1{cor['limpa']}')).replace
                                ('|', f'{cor['amarelo']}|{cor['limpa']}')).replace
                                ('+', f'{cor['amarelo']}+{cor['limpa']}')).replace
                                ('-', f'{cor['ciano']}-{cor['limpa']}')).replace
                                ('a', f'{cor['branco']}a{cor['limpa']}')).replace
                                ('b', f'{cor['branco']}b{cor['limpa']}')).replace
                                ('c', f'{cor['branco']}c{cor['limpa']}')).replace
                                ('not', f'{cor['branco']}not{cor['limpa']}')).replace
                                ('or', f'{cor['branco']}or{cor['limpa']}')).replace
                                ('nd', f'{cor['branco']}nd{cor['limpa']}')).replace
                                ('(', f'{cor['branco']}({cor['limpa']}')).replace
                                (')', f'{cor['branco']}){cor['limpa']}'))
                    print(tabela_colorida)
                elif escolha == 1 and tabela == 'd':
                    tabela = ttg.Truths(['a', 'b', 'c', 'd'], [f'(not {valor1}) {funcao} {valor2}'],
                                    ascending=True)
                    tabela_str = str(tabela)
                    tabela_str = tabela_str.replace('1', 'V').replace('0', 'F')
                    tabela_colorida = (((((((((((((tabela_str.replace
                                ('F', f'{cor['vermelho']}0{cor['limpa']}').replace
                                ('V', f'{cor['verde']}1{cor['limpa']}')).replace
                                ('|', f'{cor['amarelo']}|{cor['limpa']}')).replace
                                ('+', f'{cor['amarelo']}+{cor['limpa']}')).replace
                                ('-', f'{cor['ciano']}-{cor['limpa']}')).replace
                                ('a', f'{cor['branco']}a{cor['limpa']}')).replace
                                ('b', f'{cor['branco']}b{cor['limpa']}')).replace
                                ('c', f'{cor['branco']}c{cor['limpa']}')).replace
                                ('d', f'{cor['branco']}d{cor['limpa']}')).replace
                                ('ot', f'{cor['branco']}ot{cor['limpa']}')).replace
                                ('or', f'{cor['branco']}or{cor['limpa']}')).replace
                                ('n', f'{cor['branco']}n{cor['limpa']}')).replace
                                ('(', f'{cor['branco']}({cor['limpa']}')).replace
                                (')', f'{cor['branco']}){cor['limpa']}'))
                    print(tabela_colorida)
                elif escolha == 2 and tabela == 'd':
                    tabela = ttg.Truths(['a', 'b', 'c', 'd'], [f'{valor1} {funcao} (not {valor2})'],
                                    ascending=True)
                    tabela_str = str(tabela)
                    tabela_str = tabela_str.replace('1', 'V').replace('0', 'F')
                    tabela_colorida = (((((((((((((tabela_str.replace
                                ('F', f'{cor['vermelho']}0{cor['limpa']}').replace
                                ('V', f'{cor['verde']}1{cor['limpa']}')).replace
                                ('|', f'{cor['amarelo']}|{cor['limpa']}')).replace
                                ('+', f'{cor['amarelo']}+{cor['limpa']}')).replace
                                ('-', f'{cor['ciano']}-{cor['limpa']}')).replace
                                ('a', f'{cor['branco']}a{cor['limpa']}')).replace
                                ('b', f'{cor['branco']}b{cor['limpa']}')).replace
                                ('c', f'{cor['branco']}c{cor['limpa']}')).replace
                                ('d', f'{cor['branco']}d{cor['limpa']}')).replace
                                ('ot', f'{cor['branco']}ot{cor['limpa']}')).replace
                                ('or', f'{cor['branco']}or{cor['limpa']}')).replace
                                ('n', f'{cor['branco']}n{cor['limpa']}')).replace
                                ('(', f'{cor['branco']}({cor['limpa']}')).replace
                                (')', f'{cor['branco']}){cor['limpa']}'))
                    print(tabela_colorida)
                elif escolha == 3 and tabela == 'd':
                    tabela = ttg.Truths(['a', 'b', 'c', 'd'], [f'not ({valor1} {funcao} {valor2})'],
                                    ascending=True)
                    tabela_str = str(tabela)
                    tabela_str = tabela_str.replace('1', 'V').replace('0', 'F')
                    tabela_colorida = (((((((((((((tabela_str.replace
                                ('F', f'{cor['vermelho']}0{cor['limpa']}').replace
                                ('V', f'{cor['verde']}1{cor['limpa']}')).replace
                                ('|', f'{cor['amarelo']}|{cor['limpa']}')).replace
                                ('+', f'{cor['amarelo']}+{cor['limpa']}')).replace
                                ('-', f'{cor['ciano']}-{cor['limpa']}')).replace
                                ('a', f'{cor['branco']}a{cor['limpa']}')).replace
                                ('b', f'{cor['branco']}b{cor['limpa']}')).replace
                                ('c', f'{cor['branco']}c{cor['limpa']}')).replace
                                ('d', f'{cor['branco']}d{cor['limpa']}')).replace
                                ('ot', f'{cor['branco']}ot{cor['limpa']}')).replace
                                ('or', f'{cor['branco']}or{cor['limpa']}')).replace
                                ('n', f'{cor['branco']}n{cor['limpa']}')).replace
                                ('(', f'{cor['branco']}({cor['limpa']}')).replace
                                (')', f'{cor['branco']}){cor['limpa']}'))
                    print(tabela_colorida)
                else:
                    print(f'{cor['vermelho']}OPÇÃO {tabela} INVÁLIDA. TENTE NOVAMENTE.{cor['limpa']}')
            else:
                if tabela == 'b':
                    tabela = ttg.Truths(['a', 'b'], [f'{valor1} {funcao} {valor2}'],
                                        ascending=True)
                    tabela_str = str(tabela)
                    tabela_str = tabela_str.replace('1', 'V').replace('0', 'F')
                    tabela_colorida = ((((((((((tabela_str.replace
                                ('F', f'{cor['vermelho']}0{cor['limpa']}').replace
                                ('V', f'{cor['verde']}1{cor['limpa']}')).replace
                                ('|', f'{cor['amarelo']}|{cor['limpa']}')).replace
                                ('+', f'{cor['amarelo']}+{cor['limpa']}')).replace
                                ('-', f'{cor['ciano']}-{cor['limpa']}')).replace
                                ('a', f'{cor['branco']}a{cor['limpa']}')).replace
                                ('b', f'{cor['branco']}b{cor['limpa']}')).replace
                                ('or', f'{cor['branco']}or{cor['limpa']}')).replace
                                ('nd', f'{cor['branco']}nd{cor['limpa']}')).replace
                                ('(', f'{cor['branco']}({cor['limpa']}')).replace
                                (')', f'{cor['branco']}){cor['limpa']}'))
                    print(tabela_colorida)
                elif tabela == 'c':
                    tabela = ttg.Truths(['a', 'b', 'c'], [f'{valor1} {funcao} {valor2}'],
                                        ascending=True)
                    tabela_str = str(tabela)
                    tabela_str = tabela_str.replace('1', 'V').replace('0', 'F')
                    tabela_colorida = (((((((((((tabela_str.replace
                                ('F', f'{cor['vermelho']}0{cor['limpa']}').replace
                                ('V', f'{cor['verde']}1{cor['limpa']}')).replace
                                ('|', f'{cor['amarelo']}|{cor['limpa']}')).replace
                                ('+', f'{cor['amarelo']}+{cor['limpa']}')).replace
                                ('-', f'{cor['ciano']}-{cor['limpa']}')).replace
                                ('a', f'{cor['branco']}a{cor['limpa']}')).replace
                                ('b', f'{cor['branco']}b{cor['limpa']}')).replace
                                ('c', f'{cor['branco']}c{cor['limpa']}')).replace
                                ('or', f'{cor['branco']}or{cor['limpa']}')).replace
                                ('nd', f'{cor['branco']}nd{cor['limpa']}')).replace
                                ('(', f'{cor['branco']}({cor['limpa']}')).replace
                                (')', f'{cor['branco']}){cor['limpa']}'))
                    print(tabela_colorida)
                elif tabela == 'd':
                    tabela = ttg.Truths(['a', 'b', 'c', 'd'], [f'{valor1} {funcao} {valor2}'],
                                        ascending=True)
                    tabela_str = str(tabela)
                    tabela_str = tabela_str.replace('1', 'V').replace('0', 'F')
                    tabela_colorida = ((((((((((((tabela_str.replace
                                ('F', f'{cor['vermelho']}0{cor['limpa']}').replace
                                ('V', f'{cor['verde']}1{cor['limpa']}')).replace
                                ('|', f'{cor['amarelo']}|{cor['limpa']}')).replace
                                ('+', f'{cor['amarelo']}+{cor['limpa']}')).replace
                                ('-', f'{cor['ciano']}-{cor['limpa']}')).replace
                                ('a', f'{cor['branco']}a{cor['limpa']}')).replace
                                ('b', f'{cor['branco']}b{cor['limpa']}')).replace
                                ('c', f'{cor['branco']}c{cor['limpa']}')).replace
                                ('d', f'{cor['branco']}d{cor['limpa']}')).replace
                                ('or', f'{cor['branco']}or{cor['limpa']}')).replace
                                ('n', f'{cor['branco']}n{cor['limpa']}')).replace
                                ('(', f'{cor['branco']}({cor['limpa']}')).replace
                                (')', f'{cor['branco']}){cor['limpa']}'))
                    print(tabela_colorida)
                else:
                    print(f'{cor['vermelho']}OPÇÃO {tabela} INVÁLIDA. TENTE NOVAMENTE.{cor['limpa']}')
        else:
            print(f'{cor['vermelho']}OPÇÃO {funcao} INVÁLIDA. TENTE NOVAMENTE.{cor['limpa']}')
else:
    print(f'{cor['vermelho']}OPÇÃO {escolhido} {cor['vermelho']}INVÁLIDA. TENTE NOVAMENTE.{cor['limpa']}')
