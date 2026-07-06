from time import sleep
from funcoes.funcoes import limpatela, perguntar_continuar

neg = '\u0305'

def n(l):
    return l + neg

A, B, C, D = 'A', 'B', 'C', 'D'
An, Bn, Cn, Dn = n(A), n(B), n(C), n(D)

CONFIGURACOES = {
    2: {
        "cab_lin": ["A"],
        "cab_col": ["B"],
        "col_vars": [[Bn], [B]],          
        "lin_vars": [[An], [A]],         
        "linhas": 2, "colunas": 2,
    },
    3: {
        "cab_lin": ["A"],
        "cab_col": ["B", "C"],
        "col_vars": [[Bn,Cn],[Bn,C],[B,C],[B,Cn]],
        "lin_vars": [[An], [A]], 
        "linhas": 2, "colunas": 4,
    },
    4: {
        "cab_lin": ["A", "B"],
        "cab_col": ["C", "D"],
        "col_vars": [[Cn,Dn],[Cn,D],[C,D],[C,Dn]],
        "lin_vars": [[An,Bn],[An,B],[A,B],[A,Bn]],
        "linhas": 4, "colunas": 4,
    },
}

def exibir_mapa(k_mapa, cfg, cor):
    col_vars  = cfg["col_vars"]
    lin_vars  = cfg["lin_vars"]
    num_lin   = cfg["linhas"]
    num_col   = cfg["colunas"]
    num_vc    = len(cfg["cab_col"])

    cel      = 5
    larg_var = 4
    offset   = larg_var + 2   

    vi_topo = [0] if num_vc > 0 else []
    for vi in vi_topo:
        linha = ' ' * offset
        for labels in col_vars:
            val = labels[vi] if vi < len(labels) else ''
            tam_real = len(val.replace('\u0305', ''))
            celula = f' {val:^{cel}}'
            celula_colorida = celula.replace(val, f'{cor["roxo"]}{val}{cor["limpa"]}')
            linha += celula_colorida
        print(linha)
    sep_top = ' ' * (offset - 1) + f'{cor["amarelo"]}┌{cor["limpa"]}'
    for k in range(num_col):
        sep_top += '─' * cel
        sep_top += f'{cor["amarelo"]}{"┬" if k < num_col - 1 else "┐"}{cor["limpa"]}'
    print(sep_top)
    for i in range(num_lin):
        labels = lin_vars[i]
        linha = ''
        val_esq = labels[0] if len(labels) > 0 else ''
        tam_real_esq = len(val_esq.replace('\u0305', ''))
        celula_esq = f'{val_esq:^{larg_var + (len(val_esq) - tam_real_esq)}}'
        celula_esq_colorida = celula_esq.replace(val_esq, f'{cor["roxo"]}{val_esq}{cor["limpa"]}')
        linha += celula_esq_colorida
        linha += f' {cor["amarelo"]}│{cor["limpa"]}'
        for j in range(num_col):
            v = k_mapa[i][j]
            cv = cor["verde"] if v == "1" else cor["vermelho"]
            val_centralizado = f'{v:^{cel}}'.replace(v, f'{cv}{v}{cor["limpa"]}')
            linha += val_centralizado
            linha += f'{cor["amarelo"]}│{cor["limpa"]}'
        if len(labels) > 1:
            val_dir = labels[1]
            linha += f' {cor["ciano"]}{val_dir}{cor["limpa"]}'
        print(linha)
        if i < num_lin - 1:
            sep = ' ' * (offset - 1) + f'{cor["amarelo"]}┼{cor["limpa"]}'
            for k in range(num_col):
                sep += '─' * cel
                sep += f'{cor["amarelo"]}{"┼" if k < num_col - 1 else "┤"}{cor["limpa"]}'
            print(sep)
    fim = ' ' * (offset - 1) + f'{cor["amarelo"]}└{cor["limpa"]}'
    for k in range(num_col):
        fim += '─' * cel
        fim += f'{cor["amarelo"]}{"┴" if k < num_col - 1 else "┘"}{cor["limpa"]}'
    print(fim)
    vi_baixo = [1] if num_vc > 1 else []
    for vi in vi_baixo:
        linha = ' ' * offset
        for labels in col_vars:
            val = labels[vi] if vi < len(labels) else ''
            celula = f' {val:^{cel}}'
            celula_colorida = celula.replace(val, f'{cor["roxo"]}{val}{cor["limpa"]}')
            linha += celula_colorida
        print(linha)


def mapa_karnaugh(cor, data_formatada):
    titulo_mapa = (
        f'{cor["branco"]}╔══════════════════════════╗{cor["limpa"]}\n'
        f'{cor["ciano"]}║    MAPA DE KARNAUGH     ║{cor["limpa"]}\n'
        f'{cor["branco"]}╚══════════════════════════╝{cor["limpa"]}'
    )

    while True:
        while True:
            limpatela()
            print(data_formatada)
            print()
            print(titulo_mapa)
            print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
            print(f'{cor["verde"]}[ 2 ]{cor["limpa"]} {cor["branco"]}Duas variáveis   (A, B){cor["limpa"]}')
            print(f'{cor["verde"]}[ 3 ]{cor["limpa"]} {cor["branco"]}Três variáveis   (A, B, C){cor["limpa"]}')
            print(f'{cor["verde"]}[ 4 ]{cor["limpa"]} {cor["branco"]}Quatro variáveis (A, B, C, D){cor["limpa"]}')
            print(f'{cor["vermelho"]}[ 0 ]{cor["limpa"]} {cor["branco"]}VOLTAR AO MENU ANTERIOR{cor["limpa"]}')
            print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
            escolha_str = input(f'{cor["roxo"]}QUANTAS VARIÁVEIS? {cor["limpa"]}').strip()

            if not escolha_str.isdigit():
                print(f'{cor["vermelho"]}INVÁLIDO! DIGITE APENAS NÚMEROS.{cor["limpa"]}')
                input(f'{cor["branco"]}PRESSIONE ENTER PARA CONTINUAR...{cor["limpa"]}')
                continue

            num_variaveis = int(escolha_str)
            if num_variaveis == 0:
                return
            elif num_variaveis in [2, 3, 4]:
                break
            else:
                print(f'{cor["vermelho"]}INVÁLIDO! ESCOLHA 2, 3 OU 4.{cor["limpa"]}')
                input(f'{cor["branco"]}PRESSIONE ENTER PARA CONTINUAR...{cor["limpa"]}')
                continue

        cfg     = CONFIGURACOES[num_variaveis]
        lin_vars = cfg["lin_vars"]
        col_vars = cfg["col_vars"]
        cab_lin  = cfg["cab_lin"]
        cab_col  = cfg["cab_col"]
        linhas   = cfg["linhas"]
        colunas  = cfg["colunas"]

        while True:
            limpatela()
            print(data_formatada)
            print()
            print(titulo_mapa)
            print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
            print(f'{cor["amarelo"]}PREENCHA O MAPA ({num_variaveis} VARIÁVEIS):{cor["limpa"]}')
            print(f'{cor["branco"]}─{cor["limpa"]}' * 25)

            k_mapa = [[' ' for _ in range(colunas)] for _ in range(linhas)]

            for i in range(linhas):
                for j in range(colunas):
                    lin_str = ''.join(lin_vars[i])
                    col_str = ''.join(col_vars[j])
                    while True:
                        valor = input(
                            f'  {cor["branco"]}{lin_str}, {col_str}: {cor["limpa"]}'
                        ).strip()
                        if valor in ['0', '1']:
                            k_mapa[i][j] = valor
                            break
                        print(f'{cor["vermelho"]}DIGITE APENAS 0 OU 1!{cor["limpa"]}')
                        input(f'{cor["branco"]}PRESSIONE ENTER PARA CONTINUAR...{cor["limpa"]}')
                        print("\033[3A\033[J", end="")
                        continue

            print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
            for c in range(4):
                print(f'\r\033[1;95m{"PROCESSANDO" + "." * c:^25}\033[0m', end='', flush=True)
                sleep(1.5)
            print()
            print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
            print(f'{cor["verde"]}RESULTADO{cor["limpa"]}')
            print()
            exibir_mapa(k_mapa, cfg, cor)
            print(f'{cor["branco"]}─{cor["limpa"]}' * 25)

            if not perguntar_continuar(cor, data_formatada, 'DESEJA PREENCHER OUTRO MAPA?', 'SAINDO DO MAPA'):
                break
        limpatela()
        print(data_formatada)
        if not perguntar_continuar(cor, data_formatada, 'DESEJA ESCOLHER OUTRA QUANTIDADE DE VARIÁVEIS?', 'SAINDO DO MAPA DE KARNAUGH'):
            break