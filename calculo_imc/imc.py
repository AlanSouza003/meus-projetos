from time import sleep

from orca.messages import percentage

# Tabela de cores

cor = {'limpa':'\033[0m', 'amarelo':'\033[1;93m', 'ciano':'\033[1;96m',
        'branco':'\033[1;97m', 'roxo':'\033[1;95m', 'vermelho':'\033[1;91m',
        'verde':'\033[1;92m'}

# Variáveis de controle

cal_format  = 'CALUCULO IMC'
maior_imc_titulo = 'MAIOR IMC'
menor_imc_titulo = 'MENOR IMC'
nome_maior = ''
nome_menor = ''
peso_format = ''
peso_maior = 0
peso_menor = 0
peso_maior_str = ''
peso_menor_str = ''
altura_maior = 0
altura_menor = 0
altura_format = ''
altura_maior_str = ''
altura_menor_str = ''
idade_maior = 0
idade_menor = 0
imc_maior = 0
imc_maior_str = ''
imc_menor = 0
imc_menor_str = ''
media_imc = 0
media_format = ''
cont_grup = 0
cont_masc = 0
cont_femi = 0
cont_pesoideal = 0
cont_sobrepeso = 0
cont_obesidade = 0
porcent_pesoideal = 0
porcent_sobrepeso = 0
porcent_obesidade = 0

# Titulo

print(f'{cor['branco']}-={cor['limpa']}'*11)
print(f'{cor['ciano']}{'{:^20}'.format(cal_format)}{cor['limpa']}')
print(f'{cor['branco']}-={cor['limpa']}'*11)

# Estrutura de repetição para ler o IMC de cada pessoa.

for p in range(1, 5):

    print(f'{cor['roxo']}====== {p}º PESSOA ======{cor['limpa']}')
    # nome = input(f'{cor['branco']}Digite seu nome: {cor['limpa']}')
    # idade = int(input(f'{cor['branco']}Digite sua idade: {cor['limpa']}'))
    # sexo = str(input('Sexo [M/F]: ')).upper()
    peso_input = input(f'{cor['branco']}Informe o peso: {cor["limpa"]}')
    peso = float(peso_input.replace(',','.'))
    altura_input = input(f'{cor['branco']}Informe a altura: {cor['limpa']}')
    altura = float(altura_input.replace(',','.'))
    imc = peso / (altura ** 2) # Calculando o IMC
    media_imc += imc / 4 # Calculando a média do grupo
    media_format = f'{media_imc:.2f}'
    peso_format = peso_input
    altura_format = altura_input
    cont_grup += 1

    # Estrutura condicional composta para saber o maior IMC.

    # if p == 1:
    #     imc_maior = imc
    #     nome_maior = nome
    #     idade_maior = idade
    #     altura_maior = altura
    #     peso_maior = peso
    # else:
    #     if imc > imc_maior:
    #         imc_maior = imc
    #         nome_maior = nome
    #         idade_maior = idade
    #         altura_maior = altura
    #         peso_maior = peso

    # Estrutura condicional composta para saber o menor IMC.

    # if p == 1:
    #     imc_menor = imc
    #     nome_menor = nome
    #     idade_menor = idade
    #     altura_menor = altura
    #     peso_menor = peso
    # else:
    #     if imc < imc_menor:
    #         imc_menor = imc
    #         nome_menor = nome
    #         idade_menor = idade
    #         altura_menor = altura
    #         peso_menor = peso

    # Contador seperado por sexo.

    # if sexo == 'M':
    #     cont_masc  += 1
    # else:
    #     cont_femi += 1

    if imc <= 24.9:
        cont_pesoideal += 1
        porcent_pesoideal = cont_pesoideal / cont_grup * 100
    elif imc <= 29.9:
        cont_sobrepeso += 1
        porcent_sobrepeso = cont_sobrepeso / cont_grup * 100
    else:
        cont_obesidade += 1
        porcent_obesidade = cont_obesidade / cont_grup * 100

# Transforamando o imc_maior em "string".

imc_maior_str = str(f'{imc_maior:.1f}')
imc_menor_str = str(f'{imc_menor:.1f}')
altura_maior_str = str(f'{altura_maior}')
altura_menor_str = str(f'{altura_menor}')
peso_maior_str = str(f'{peso_maior}')
peso_menor_str = str(f'{peso_menor}')

# Estrutura condicional simples para colocar a vírgula no lugar do ponto quando escrito com a vírgula.

if ',' in peso_format or ',' in altura_format:

    media_format = media_format.replace('.', ',')
    imc_maior_str = imc_maior_str.replace('.', ',')
    imc_menor_str = imc_menor_str.replace('.', ',')
    peso_maior_str = peso_maior_str.replace('.', ',')
    peso_menor_str = peso_menor_str.replace('.', ',')
    altura_maior_str = altura_maior_str.replace('.', ',')
    altura_menor_str = altura_menor_str.replace('.', ',')

print(f'A média do IMC total do grupo é {media_format}!')

print(f'{cor['roxo']}PROCESSANDO{cor["limpa"]}', end='')
for c in range(1, 4):
    print(f'{cor['branco']}.{cor['limpa']}', end='')
    sleep(1)

print()

# Dados do grupo.

print(f'{cor['branco']}-{cor['limpa']}'*20)
print(f'{cor['ciano']}{'DADOS DO GRUPO':^20}{cor["limpa"]}')
print(f'{cor['branco']}-{cor['limpa']}'*20)
print(f'TOTAL DE USUÁRIO: {cont_grup}')
print(f'TOTAL MASCULINO: {cont_masc}')
print(f'TOTAL FEMININO: {cont_femi}')
print(f'MÉDIA DO GRUPO IMC: {media_imc}')
print(f'CLASSIFICAÇÃO DO GRUPO: ',end='')

# Classificação do grupo

if media_imc < 18.5:
    print(f'{cor['vermelho']}ABAIXO DO PESO{cor["limpa"]}')
elif media_imc <= 25.5:
    print(f'{cor['verde']}PESO IDEAL{cor["limpa"]}')
elif media_imc <= 30.5:
    print(f'{cor['amarelo']}SOBREPESO{cor["limpa"]}')
elif media_imc <= 35.5:
    print(f'{cor['vermelho']}OBESIDADE GRAU I{cor["limpa"]}')
elif media_imc <= 40.5:
    print(f'{cor['vermelho']}OBESIDADE GRAU II{cor["limpa"]}')
elif media_imc > 40.5:
    print(f'{cor['vermelho']}OBESIDADE GRAU III{cor["limpa"]}')

# Porcentagem do grupo

print(f'DIAGNOSTICO DO IMC DO GRUPO')
print(f'PESO IDEAL: {porcent_pesoideal}% do grupo ({cont_pesoideal} pessoa)')
print(f'SOBREPESO: {porcent_sobrepeso}% do grupo ({cont_sobrepeso} pessoa)')
print(f'OBESIDADE: {porcent_obesidade}% do grupo ({cont_obesidade} pessoa)')

# Maior IMC.

print(f'{cor['branco']}-{cor['limpa']}'*20)
print(f'{cor['ciano']}{maior_imc_titulo:^20}{cor["limpa"]}')
print(f'{cor['branco']}-{cor['limpa']}'*20)
print(f'{cor['branco']}{f'NOME: {nome_maior}'.upper()}{cor['limpa']}')
print(f'{cor['branco']}IDADE: {idade_maior}{cor['limpa']}')
print(f'{cor['branco']}PESO: {peso_maior_str}KG{cor['limpa']}')
print(f'{cor['branco']}ALTURA: {altura_maior_str}M{cor['limpa']}')
print(f'{cor['branco']}IMC: {imc_maior_str}{cor['limpa']}')

#ADULTO.

if idade_maior >= 12:
    print(f'{cor['branco']}VOCÊ ESTA: {cor['limpa']}', end='')
    if imc_maior < 18.5:
        print(f'{cor['vermelho']}ABAIXO DO PESO{cor["limpa"]}')
    elif imc_maior <= 25.5:
        print(f'{cor['verde']}PESO IDEAL{cor["limpa"]}')
    elif imc_maior <= 30.5:
        print(f'{cor['amarelo']}SOBREPESO{cor["limpa"]}')
    elif imc_maior <= 35.5:
        print(f'{cor['vermelho']}OBESIDADE GRAU I{cor["limpa"]}')
    elif imc_maior <= 40.5:
        print(f'{cor['vermelho']}OBESIDADE GRAU II{cor["limpa"]}')
    elif imc_maior > 40.5:
        print(f'{cor['vermelho']}OBESIDADE GRAU III{cor["limpa"]}')

# Menor IMC

print(f'{cor['branco']}-{cor['limpa']}'*20)
print(f'{cor['ciano']}{menor_imc_titulo:^20}{cor["limpa"]}')
print(f'{cor['branco']}-{cor['limpa']}'*20)
print(f'{cor['branco']}{f'NOME: {nome_menor}'.upper()}{cor['limpa']}')
print(f'{cor['branco']}IDADE: {idade_menor}{cor['limpa']}')
print(f'{cor['branco']}PESO: {peso_menor_str}KG{cor['limpa']}')
print(f'{cor['branco']}ALTURA: {altura_menor_str}M{cor['limpa']}')
print(f'{cor['branco']}IMC: {imc_menor_str}{cor['limpa']}')

# ADULTO

if idade_menor >= 12:
    print(f'{cor['branco']}VOCÊ ESTA: {cor['limpa']}', end='')
    if imc_menor < 18.5:
        print(f'{cor['vermelho']}ABAIXO DO PESO{cor["limpa"]}')
    elif imc_menor <= 25.5:
        print(f'{cor['verde']}PESO IDEAL{cor["limpa"]}')
    elif imc_menor <= 30.5:
        print(f'{cor['amarelo']}SOBREPESO{cor["limpa"]}')
    elif imc_menor <= 35.5:
        print(f'{cor['vermelho']}OBESIDADE GRAU I{cor["limpa"]}')
    elif imc_menor <= 40.5:
        print(f'{cor['vermelho']}OBESIDADE GRAU II{cor["limpa"]}')
    elif imc_menor > 40.5:
        print(f'{cor['vermelho']}OBESIDADE GRAU III{cor["limpa"]}')

# # CRIANÇA
# else:
#     if idade >= 1 or idade < 11:
#         print(f'{cor['branco']}PERCENTIL: {imc_format}{cor['limpa']}')
#         print(f'{cor['branco']}VOCÊ ESTA: {cor['limpa']}', end='')
#         if imc < 5:
#             print(f'{cor['vermelho']}BAIXO PESO (SUBNUTRIÇÃO){cor["limpa"]}')
#         elif imc < 5 or imc <= 85:
#             print(f'{cor['verde']}PESO SAUDÁVEL(ADEQUADO){cor["limpa"]}')
#         elif imc < 85 or imc <= 95:
#             print(f'{cor['amarelo']}SOBREPESO{cor["limpa"]}')
#         elif imc > 95:
#             print(f'{cor['vermelho']}OBESIDADE MORBIDA{cor["limpa"]}')