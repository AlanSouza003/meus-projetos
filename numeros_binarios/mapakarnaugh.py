num_variaveis = int(input('Deseja um mapa de Karnaugh para quantas variáveis? (2, 3 ou 4): '))

if num_variaveis == 2:
    rotulos_linhas = ['0', '1']
    rotulos_colunas = ['0', '1']
    texto_cabeçalho = 'A \\ B'
    linhas, colunas = 2, 2
elif num_variaveis == 3:
    rotulos_linhas = ['0', '1']
    rotulos_colunas = ['00', '01', '11', '10']
    texto_cabeçalho = 'A \\ BC'
    linhas, colunas = 2, 4
elif num_variaveis == 4:
    rotulos_linhas = ['00', '01', '11', '10']
    rotulos_colunas = ['00', '01', '11', '10']
    texto_cabeçalho = 'AB \\ CD'
    linhas, colunas = 4, 4
else:
    print('Quantidade invalida! Por favor, escolha entre 2, 3 ou 4.')
    exit()

k_mapa = []
for i in range(linhas):
    linha_vazia = []
    for j in range(colunas):
        linha_vazia.append(' ')
    k_mapa.append(linha_vazia)

print(f'\nPreencha o mapa para {num_variaveis} variáveis (Digite 0 ou 1): ')
for i in range(linhas):
    for j in range(colunas):
        valor = input(f'Valor para [{rotulos_linhas[i]}] e [{rotulos_colunas[j]}]: ')
        k_mapa[i][j] = valor

print(f'\nMapa de Karnaugh ({num_variaveis} variáveis)')
print(f'{texto_cabeçalho} |', end="")
for col in rotulos_colunas:
    print(f'  {col}  |', end="")
print()
print('-' * (12 + colunas * 7))

for i in range(linhas):
    print(f' {rotulos_linhas[i]} |', end="")
    for j in range(colunas):
        print(f'  {k_mapa[i][j]}  |', end="")
    print()
    print('-' * (10 + colunas * 7))