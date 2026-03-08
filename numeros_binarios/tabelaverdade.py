import ttg
from time import sleep
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
    print('''ESCOLHA UMA DAS OPÇÕES ABAIXO:
[ 1 ] ADIÇÃO
[ 2 ] SUBTRAÇÃO''')
    escolha = int(input('Digite o valor: '))
    if escolha == 1:
         num = int(input('DIGITE QUANTAS ADIÇÕES DESEJA: '))
         if num == 1:
            print(f'CERTO. VAMOS REALIZAR {num} ADIÇÃO.')
            n1_str = input('Primeiro valor binario: ')
            n2_str = input('Segundo valor binario: ')
            n1_dec = int(n1_str, 2)
            n2_dec = int(n2_str, 2)
            somar_dec = n1_dec + n2_dec
            result_bin = bin(somar_dec)
            print('PROCESSANDO...')
            sleep(3)
            print('RESULTADO')
            print(f'A soma entre {n1_str} + {n2_str} é = {result_bin[2:]}')
         elif num == 2:
            print(f'CERTO. VAMOS REALIZAR {num} ADIÇÃO.')
            n1_str = input('Primeiro valor binário: ')
            n2_str = input('Segundo valor binário: ')
            n3_str = input('Terceiro valor binário: ')
            n1_dec = int(n1_str, 2)
            n2_dec = int(n2_str, 2)
            n3_dec = int(n3_str, 2)
            somar_dec = n1_dec + n2_dec + n3_dec
            resut_bin = bin(somar_dec)
            print('PROCESSANDO...')
            sleep(3)
            print('RESULTADO')
            print(f'A soma entre {n1_str} + {n2_str} + é = {resut_bin[2:]}')
# elif escolhido == 4:
# elif escolhido == 5:
# else:
#     print(f'OPÇÃO {escolhido} INVÁLIDA. TENTE NOVAMENTE.')
#
#
# num2 = input('Digite um numero binario: ')
#
# decimal = int(num2, 2)
# a = True
# b = False
# result = not(a and b) # Altera o resultado
# result2 = not b, not a # Altera as entradas
#                           #Entradas          #Saidas
# tabela = ttg.Truths(['a', 'b'], ascending=True) # Aqui vai imprimir a tabela verdade e as somas
# print(decimal)

# n1_str = input('Digite o primeiro valor binario ')
# n2_str = input('Digite o segundo valor binario ')
# # n3_str = input('Digite o terceiro valor binario ')
# # n4_str = input('Digite o quarto valor binario ')
# n1_dec = int(n1_str, 2)
# n2_dec = int(n2_str, 2)
# # n3_dec = int(n3_str, 2)
# # n4_dec = int(n4_str, 2)
# somar_dec = n1_dec - n2_dec #n3_dec + n4_dec
# result_bin = bin(somar_dec)
# print(result_bin)
# n1_str = input('Digite o primeiro valor binario ')
# n2_str = input('Digite o segundo valor binario ')
# # n3_str = input('Digite o terceiro valor binario ')
# # n4_str = input('Digite o quarto valor binario ')
# n1_dec = int(n1_str, 2)
# n2_dec = int(n2_str, 2)
# # n3_dec = int(n3_str, 2)
# # n4_dec = int(n4_str, 2)
# somar_dec = n1_dec + n2_dec + #n3_dec + n4_dec
# result_bin = bin(somar_dec)
# print(result_bin)