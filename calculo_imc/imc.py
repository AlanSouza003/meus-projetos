from time import sleep
cor = {'limpa':'\033[0m', 'amarelo':'\033[1;93m', 'ciano':'\033[1;96m',
       'branco':'\033[1;97m', 'roxo':'\033[1;95m', 'vermelho':'\033[1;91m',
       'verde':'\033[1;92m'}
cal_format  = 'CALUCULO IMC'
resu_format = 'RESULTADO'
print(f'{cor['branco']}-={cor['limpa']}'*11)
print(f'{cor['ciano']}{'{:^20}'.format(cal_format)}{cor['limpa']}')
print(f'{cor['branco']}-={cor['limpa']}'*11)
nome = input(f'{cor['branco']}Digite seu nome: {cor['limpa']}')
idade = int(input(f'{cor['branco']}Digite sua idade: {cor['limpa']}'))
peso = float(input(f'{cor['branco']}Informe o peso: {cor["limpa"]}'))
altura = float(input(f'{cor['branco']}Informe a altura: {cor['limpa']}'))
imc = peso / (altura ** 2)
print(f'{cor['roxo']}PROCESSANDO...{cor["limpa"]}')
sleep(3)
print(f'{cor['branco']}-{cor['limpa']}'*20)
print(f'{cor['ciano']}{'{:^20}'.format(resu_format)}{cor["limpa"]}')
print(f'{cor['branco']}-{cor['limpa']}'*20)
print(f'{cor['branco']}NOME: {nome}{cor['limpa']}')
print(f'{cor['branco']}IDADE: {idade}{cor['limpa']}')
print(f'{cor['branco']}PESO: {peso}KG{cor['limpa']}')
print(f'{cor['branco']}ALTURA: {altura}M{cor['limpa']}')
print(f'{cor['branco']}IMC: {imc:.2f}{cor['limpa']}')
print(f'{cor['branco']}VOCÊ ESTÁ: {cor['limpa']}',end='')
#ADULTO
if idade >= 13:
    if imc < 18.5:
        print(f'{cor['vermelho']}ABAIXO DO PESO{cor["limpa"]}')
    elif imc < 18.5 or imc <= 25:
        print(f'{cor['verde']}PESO IDEAL{cor["limpa"]}')
    elif imc > 25 or imc <= 30:
        print(f'{cor['amarelo']}SOBREPESO{cor["limpa"]}')
    elif imc > 30 or imc <= 40:
        print(f'{cor['vermelho']}OBESIDADE{cor["limpa"]}')
    elif imc > 40:
        print(f'{cor['vermelho']}OBESIDADE MORBIDA{cor["limpa"]}')
else:
    #CRIANÇA
    if idade >= 1 or idade < 12:
        if imc < 5:
            print(f'{cor['vermelho']}BAIXO PESO (SUBNUTRIÇÃO){cor["limpa"]}')
        elif imc < 5 or imc <= 85:
            print(f'{cor['verde']}PESO SAUDÁVEL(ADEQUADO){cor["limpa"]}')
        elif imc > 85 or imc <= 95:
            print(f'{cor['amarelo']}SOBREPESO{cor["limpa"]}')
        elif imc > 95:
            print(f'{cor['vermelho']}OBESIDADE MORBIDA{cor["limpa"]}')