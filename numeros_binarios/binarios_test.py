import ttg
from time import sleep
from datetime import date

cor = {'limpa': '\033[0m', 'vermelho': '\033[1;91m', 'verde': '\033[1;92m', 'ciano': '\033[1;96m',
       'amarelo': '\033[1;93m', 'branco': '\033[1;97m', 'roxo': '\033[1;95m', 'azul': '\033[1;94m'}
data = date.today().day
mes = date.today().month
ano = date.today().year
print(f'{cor["amarelo"]}DATA: {data:02d}/{mes:02d}/{ano}{cor["limpa"]}')
print(f'{cor["branco"]}-={cor["limpa"]}' * 12)
print(f'{cor["ciano"]}{"NÚMEROS BINÁRIOS":^25}{cor["limpa"]}')
print(f'{cor["branco"]}-={cor["limpa"]}' * 12)
print(f'''{cor["amarelo"]}ESCOLHA A OPÇÃO DESEJADA:{cor["limpa"]}
{cor["verde"]}[ 1 ]{cor["limpa"]} {cor["branco"]}CONVERSÃO DE DÉCIMAL PARA BINÁRIO{cor["limpa"]}
{cor["verde"]}[ 2 ]{cor["limpa"]} {cor["branco"]}CONVERSÃO DE BINÁRIO PARA DÉCIMAL{cor["limpa"]}
{cor["verde"]}[ 3 ]{cor["limpa"]} {cor["branco"]}SOMANDO NÚMEROS BINÁRIOS{cor["limpa"]}
{cor["verde"]}[ 4 ]{cor["limpa"]} {cor["branco"]}VISUALIZAR A TABELA VERDADE{cor["limpa"]}
{cor["verde"]}[ 5 ]{cor["limpa"]} {cor["branco"]}REALIZAR CALCULOS EXPRESSÕES BOOLEANAS{cor["limpa"]}
{cor["verde"]}[ 0 ]{cor["limpa"]} {cor["branco"]}SAIR{cor["limpa"]}''')
print(f'{cor["branco"]}─{cor["limpa"]}' * 25)

escolhido = 0

while True:
    escolhido_str = str(
        input(f'{cor["roxo"]}DIGITE O NÚMERO DA SUA OPÇÃO [DIGITE 0 PARA SAIR]: {cor["limpa"]}'))
    if escolhido_str.isdigit():
        escolhido = int(escolhido_str)
        if escolhido == 0:
            break
        elif 1 <= escolhido <= 5:
            break
        else:
            print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
            print(
                f'{cor["vermelho"]}VALOR INVÁLIDO! UTILIZE VALORES DE:{cor["limpa"]} '
                f'{cor["branco"]}1 ATE 5 [OU 0 PARA ENCERRAR].{cor["limpa"]}'
            )
            print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
    elif escolhido_str.isalpha():
        print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
        print(
            f'{cor["vermelho"]}UTILIZE NÚMEROS.{cor["limpa"]} '
        )
        print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
    else:
        print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
        print(
            f'{cor["vermelho"]}UTILIZE APENAS NÚMEROS.{cor["limpa"]} '
        )
        print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
if 1 <= escolhido <= 5:
    if escolhido == 1:
        print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
        print(f'{cor["ciano"]}{"CONVERSOR DE DECIMAL":^25}\n'
              f'{"PARA BINÁRIO":^25}{cor["limpa"]}')
        print(f'{cor["branco"]}─{cor["limpa"]}' * 25)

        while True:
            valor_str = str(
                input(f'{cor["branco"]}Digite um valor inteiro: {cor["limpa"]}'))

            if valor_str.isdigit():
                valor = int(valor_str)
                binario = bin(valor)
                binario_str = str(binario[2:])
                binario_str = binario_str.replace('1', 'V').replace('0', 'F')
                binario_colorido = (binario_str
                                    .replace('F', f'{cor["vermelho"]}0{cor["limpa"]}')
                                    .replace('V', f'{cor["verde"]}1{cor["limpa"]}'))

                print(f'{cor["verde"]}VALOR INTEIRO{cor["limpa"]}{cor["branco"]}: {valor}{cor["limpa"]}\n'
                      f'{cor["verde"]}VALOR BINÁRIO:{cor["limpa"]} {binario_colorido}')
                print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                continuar = ''
                while True:
                    continuar = input(
                        f'{cor["amarelo"]}Deseja converter outro valor? (S/N): {cor["limpa"]}').upper().strip()
                    print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                    if continuar in ['S', 'SIM']:
                        break
                    elif continuar in ['NÃO', 'NAO', 'N']:
                        print(
                            f'{cor["ciano"]}SAINDO DA CONVERSÃO{cor["limpa"]}', end='')
                        for c in range(3):
                            print(f'{cor["ciano"]}.{cor["limpa"]}',
                                  end='', flush=True)
                            sleep(1)
                        break
                    elif continuar not in ['SIM', 'S']:
                        print(
                            f'{cor["vermelho"]}OPÇÃO INVALIDA! TENTE NOVAMENTE.{cor["limpa"]}'
                        )
                        print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                if continuar in ['NÃO', 'NAO', 'N']:
                    break
            else:
                print(
                    f'{cor["vermelho"]}OPÇÃO INVALIDA! TENTE NOVAMENTE.{cor["limpa"]}'
                )
                print(f'{cor["branco"]}─{cor["limpa"]}' * 25)

    elif escolhido == 2:
        titulo = 'CONVERSOR DE BINÁRIO'
        titulo2 = 'PARA DÉCIMAL'
        print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
        print(f'{cor["ciano"]}{titulo:^25}{cor["limpa"]}')
        print(f'{cor["ciano"]}{titulo2:^25}{cor["limpa"]}')
        print(f'{cor["branco"]}─{cor["limpa"]}' * 25)

        while True:
            binario = input(
                f'{cor["branco"]}Digite um valor em binário: {cor["limpa"]}')
            if all(c in '01' for c in binario):
                decimal = int(binario, 2)
                binario_str = str(binario)
                binario_str = binario_str.replace('1', 'V').replace('0', 'F')
                binario_colorido = (binario_str
                                    .replace('F', f'{cor["vermelho"]}0{cor["limpa"]}')
                                    .replace('V', f'{cor["verde"]}1{cor["limpa"]}'))

                print(f'{cor["verde"]}VALOR BINÁRIO{cor["limpa"]}: {binario_colorido}\n'
                      f'{cor["verde"]}VALOR INTEIRO{cor["limpa"]}{cor["branco"]}: {decimal}{cor["limpa"]}')
                print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                continuar = ''
                while True:
                    continuar = input(
                        f'{cor["amarelo"]}Deseja converter outro valor? (S/N): {cor["limpa"]}').upper().strip()
                    print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                    if continuar in ['S', 'SIM']:
                        break
                    elif continuar in ['NÃO', 'NAO', 'N']:
                        print(
                            f'{cor["ciano"]}SAINDO DA CONVERSÃO{cor["limpa"]}', end='')
                        for c in range(3):
                            print(f'{cor["ciano"]}.{cor["limpa"]}',
                                  end='', flush=True)
                            sleep(1)
                        break
                    elif continuar not in ['SIM', 'S']:
                        print(
                            f'{cor["vermelho"]}OPÇÃO INVALIDA! TENTE NOVAMENTE.{cor["limpa"]}'
                        )
                        print(f'{cor["branco"]}─{cor["limpa"]}' * 25)

                if continuar in ['NÃO', 'NAO', 'N']:
                    break
            else:
                print(
                    f'{cor["vermelho"]}OPÇÃO INVALIDA! TENTE NOVAMENTE.{cor["limpa"]}'
                )
                print(f'{cor["branco"]}─{cor["limpa"]}' * 25)

    elif escolhido == 3:
        titulo = 'SOMANDO NÚMEROS'
        titulo2 = 'BINÁRIOS'
        print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
        print(f'{cor["ciano"]}{titulo:^25}\n'
              f'{titulo2:^25}{cor["limpa"]}')
        print(f'{cor["branco"]}─{cor["limpa"]}' * 25)

        while True:
            print(
                f'{cor["amarelo"]}ESCOLHA UMA DAS OPÇÕES ABAIXO:{cor["limpa"]}')
            print(
                f'{cor["verde"]}[ 1 ]{cor["limpa"]} {cor["branco"]}ADIÇÃO{cor["limpa"]}')
            print(
                f'{cor["verde"]}[ 2 ]{cor["limpa"]} {cor["branco"]}SUBTRAÇÃO{cor["limpa"]}')
            print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
            escolha_str = str(
                input(f'{cor["roxo"]}DIGITE A OPÇÃO: {cor["limpa"]}'))
            print(f'{cor["branco"]}─{cor["limpa"]}' * 25)

            if escolha_str not in ['1', '2']:
                print(
                    f'{cor["vermelho"]}OPÇÃO INVÁLIDA! TENTE NOVAMENTE.{cor["limpa"]}'
                )
                print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
            else:
                break

        escolha = int(escolha_str)

        # ── ADIÇÃO ──────────────────────────────
        if escolha == 1:
            while True:
                print(f'{cor["amarelo"]}QUANTAS PARCELAS DESEJA:{cor["limpa"]}')
                print(
                    f'{cor["branco"]}DIGITE{cor["limpa"]} {cor["verde"]}[1]{cor["limpa"]} {cor["branco"]}PARA DUAS PARCELAS{cor["limpa"]}')
                print(
                    f'{cor["branco"]}DIGITE{cor["limpa"]} {cor["verde"]}[2]{cor["limpa"]} {cor["branco"]}PARA TRÊS PARCELAS{cor["limpa"]}')
                print(
                    f'{cor["branco"]}DIGITE{cor["limpa"]} {cor["verde"]}[3]{cor["limpa"]} {cor["branco"]}PARA QUATRO PARCELAS{cor["limpa"]}')
                print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                num_str = str(
                    input(f'{cor["roxo"]}DIGITE AQUI: {cor["limpa"]}'))
                print(f'{cor["branco"]}─{cor["limpa"]}' * 25)

                num = 0
                if num_str.isdigit():
                    num = int(num_str)
                if 1 <= num <= 3:
                    break
                elif num_str.isdigit():
                    print(
                        f'{cor["vermelho"]}OPÇÃO INVÁLIDA! DIGITE OS VALORES DE 1 ATÉ 3.{cor["limpa"]}'
                    )
                    print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                else:
                    print(
                        f'{cor["vermelho"]}OPÇÃO INVÁLIDA! DIGITE SOMENTE NÚMEROS.{cor["limpa"]}'
                    )
                    print(f'{cor["branco"]}─{cor["limpa"]}' * 25)

            if num == 1:
                print(
                    f'{cor["verde"]}CERTO. VAMOS REALIZAR A OPERAÇÃO.{cor["limpa"]}')
                print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                while True:
                    n1_str = str(input(
                        f'{cor["branco"]}Primeira Parcela: {cor["limpa"]}'))
                    n2_str = str(input(
                        f'{cor["branco"]}Segunda Parcela: {cor["limpa"]}'))
                    if all(c in '01' for c in n1_str) and all(c in '01' for c in n2_str):
                        n1_dec = int(n1_str, 2)
                        n2_dec = int(n2_str, 2)
                        somar_dec = n1_dec + n2_dec
                        result_bin = bin(somar_dec)
                        result_str = str(result_bin[2:]).replace(
                            '1', 'V').replace('0', 'F')
                        n1_c = n1_str.replace('1', 'V').replace('0', 'F')
                        n2_c = n2_str.replace('1', 'V').replace('0', 'F')
                        n1_colorido = n1_c.replace('F', f'{cor["vermelho"]}0{cor["limpa"]}').replace(
                            'V', f'{cor["verde"]}1{cor["limpa"]}')
                        n2_colorido = n2_c.replace('F', f'{cor["vermelho"]}0{cor["limpa"]}').replace(
                            'V', f'{cor["verde"]}1{cor["limpa"]}')
                        result_colorido = result_str.replace('F', f'{cor["vermelho"]}0{cor["limpa"]}').replace(
                            'V', f'{cor["verde"]}1{cor["limpa"]}')
                        print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                        for c in range(4):
                            ponto = f'.' * c
                            print(
                                f'\r\033[1;95m{"PROCESSANDO" + ponto:^25}\033[0m', end='', flush=True)
                            sleep(1.5)
                        print()
                        print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                        print(f'{cor["verde"]}RESULTADO{cor["limpa"]}')
                        print(f'{cor["branco"]}A soma entre{cor["limpa"]} {n1_colorido} {cor["branco"]}+{cor["limpa"]} '
                              f'{n2_colorido} {cor["branco"]}é ={cor["limpa"]} {result_colorido}')
                        continuar = ''
                        while True:
                            continuar = input(
                                f'{cor["amarelo"]}Deseja converter outro valor? (S/N): {cor["limpa"]}').upper().strip()
                            print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                            if continuar in ['S', 'SIM']:
                                break
                            elif continuar in ['NÃO', 'NAO', 'N']:
                                print(
                                    f'{cor["ciano"]}SAINDO DO CALCULO{cor["limpa"]}', end='')
                                for c in range(3):
                                    print(f'{cor["ciano"]}.{cor["limpa"]}',
                                          end='', flush=True)
                                    sleep(1)
                                break
                            elif continuar not in ['SIM', 'S']:
                                print(
                                    f'{cor["vermelho"]}OPÇÃO INVALIDA! TENTE NOVAMENTE.{cor["limpa"]}'
                                )
                                print(f'{cor["branco"]}─{cor["limpa"]}' * 25)

                        if continuar in ['NÃO', 'NAO', 'N']:
                            break
                    else:
                        print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                        print(
                            f'{cor["vermelho"]}OPERAÇÃO INVÁLIDA! UTILIZE APENAS: {cor["limpa"]}'
                            f'{cor["verde"]}1s{cor["limpa"]} {cor["branco"]}E{cor["limpa"]} {cor["vermelho"]}0s{cor["limpa"]}'
                            f'{cor["branco"]}.{cor["limpa"]}'
                        )
                        print(f'{cor["branco"]}─{cor["limpa"]}' * 25)

            elif num == 2:
                print(
                    f'{cor["verde"]}CERTO. VAMOS REALIZAR AS OPERAÇÕES.{cor["limpa"]}')
                print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                while True:
                    n1_str = input(
                        f'{cor["branco"]}Primeira Parcela: {cor["limpa"]}')
                    n2_str = input(
                        f'{cor["branco"]}Segunda Parcela: {cor["limpa"]}')
                    n3_str = input(
                        f'{cor["branco"]}Terceira Parcela: {cor["limpa"]}')
                    if all(c in '01' for c in n1_str) and all(c in '01' for c in n2_str) and all(c in '01' for c in n3_str):
                        n1_dec = int(n1_str, 2)
                        n2_dec = int(n2_str, 2)
                        n3_dec = int(n3_str, 2)
                        somar_dec = n1_dec + n2_dec + n3_dec
                        result_bin = bin(somar_dec)
                        result_str = str(result_bin[2:]).replace(
                            '1', 'V').replace('0', 'F')
                        n1_c = n1_str.replace('1', 'V').replace('0', 'F')
                        n2_c = n2_str.replace('1', 'V').replace('0', 'F')
                        n3_c = n3_str.replace('1', 'V').replace('0', 'F')
                        n1_colorido = n1_c.replace('F', f'{cor["vermelho"]}0{cor["limpa"]}').replace(
                            'V', f'{cor["verde"]}1{cor["limpa"]}')
                        n2_colorido = n2_c.replace('F', f'{cor["vermelho"]}0{cor["limpa"]}').replace(
                            'V', f'{cor["verde"]}1{cor["limpa"]}')
                        n3_colorido = n3_c.replace('F', f'{cor["vermelho"]}0{cor["limpa"]}').replace(
                            'V', f'{cor["verde"]}1{cor["limpa"]}')
                        result_colorido = result_str.replace('F', f'{cor["vermelho"]}0{cor["limpa"]}').replace(
                            'V', f'{cor["verde"]}1{cor["limpa"]}')
                        print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                        for c in range(4):
                            ponto = f'.' * c
                            print(
                                f'\r\033[1;95m{"PROCESSANDO" + ponto:^25}\033[0m', end='', flush=True)
                            sleep(1.5)
                        print()
                        print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                        print(f'{cor["verde"]}RESULTADO{cor["limpa"]}')
                        print(f'{cor["branco"]}A soma entre{cor["limpa"]} {n1_colorido} {cor["branco"]}+{cor["limpa"]} '
                              f'{n2_colorido} {cor["branco"]}+{cor["limpa"]} {n3_colorido} '
                              f'{cor["branco"]}é ={cor["limpa"]} {result_colorido}')
                        continuar = ''
                        while True:
                            continuar = input(
                                f'{cor["amarelo"]}Deseja converter outro valor? (S/N): {cor["limpa"]}').upper().strip()
                            print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                            if continuar in ['S', 'SIM']:
                                break
                            elif continuar in ['NÃO', 'NAO', 'N']:
                                print(
                                    f'{cor["ciano"]}SAINDO DO CALCULO{cor["limpa"]}', end='')
                                for c in range(3):
                                    print(f'{cor["ciano"]}.{cor["limpa"]}',
                                          end='', flush=True)
                                    sleep(1)
                                break
                            elif continuar not in ['SIM', 'S']:
                                print(
                                    f'{cor["vermelho"]}OPÇÃO INVALIDA! TENTE NOVAMENTE.{cor["limpa"]}'
                                )
                                print(f'{cor["branco"]}─{cor["limpa"]}' * 25)

                        if continuar in ['NÃO', 'NAO', 'N']:
                            break
                    else:
                        print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                        print(
                            f'{cor["vermelho"]}OPERAÇÃO INVÁLIDA! UTILIZE APENAS: {cor["limpa"]}'
                            f'{cor["verde"]}1s{cor["limpa"]} {cor["branco"]}E{cor["limpa"]} {cor["vermelho"]}0s{cor["limpa"]}'
                            f'{cor["branco"]}.{cor["limpa"]}'
                        )
                        print(f'{cor["branco"]}─{cor["limpa"]}' * 25)

            elif num == 3:
                print(
                    f'{cor["verde"]}CERTO. VAMOS REALIZAR AS OPERAÇÕES.{cor["limpa"]}')
                print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                while True:
                    print(
                        f'{cor["verde"]}CERTO. VAMOS REALIZAR AS OPERAÇÕES.{cor["limpa"]}')
                    n1_str = input(
                        f'{cor["branco"]}Primeira Parcela: {cor["limpa"]}')
                    n2_str = input(
                        f'{cor["branco"]}Segunda Parcela: {cor["limpa"]}')
                    n3_str = input(
                        f'{cor["branco"]}Terceira Parcela: {cor["limpa"]}')
                    n4_str = input(
                        f'{cor["branco"]}Quarta Parcela: {cor["limpa"]}')
                    if all(c in '01' for c in n1_str) and all(c in '01' for c in n2_str) and all(c in '01' for c in n3_str) and all(c in '01' for c in n4_str):
                        n1_dec = int(n1_str, 2)
                        n2_dec = int(n2_str, 2)
                        n3_dec = int(n3_str, 2)
                        n4_dec = int(n4_str, 2)
                        soma_dec = n1_dec + n2_dec + n3_dec + n4_dec
                        result_bin = bin(soma_dec)
                        result_str = str(result_bin[2:]).replace(
                            '1', 'V').replace('0', 'F')
                        n1_c = n1_str.replace('1', 'V').replace('0', 'F')
                        n2_c = n2_str.replace('1', 'V').replace('0', 'F')
                        n3_c = n3_str.replace('1', 'V').replace('0', 'F')
                        n4_c = n4_str.replace('1', 'V').replace('0', 'F')
                        n1_colorido = n1_c.replace('F', f'{cor["vermelho"]}0{cor["limpa"]}').replace(
                            'V', f'{cor["verde"]}1{cor["limpa"]}')
                        n2_colorido = n2_c.replace('F', f'{cor["vermelho"]}0{cor["limpa"]}').replace(
                            'V', f'{cor["verde"]}1{cor["limpa"]}')
                        n3_colorido = n3_c.replace('F', f'{cor["vermelho"]}0{cor["limpa"]}').replace(
                            'V', f'{cor["verde"]}1{cor["limpa"]}')
                        n4_colorido = n4_c.replace('F', f'{cor["vermelho"]}0{cor["limpa"]}').replace(
                            'V', f'{cor["verde"]}1{cor["limpa"]}')
                        result_colorido = result_str.replace('F', f'{cor["vermelho"]}0{cor["limpa"]}').replace(
                            'V', f'{cor["verde"]}1{cor["limpa"]}')
                        print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                        for c in range(4):
                            ponto = f'.' * c
                            print(
                                f'\r\033[1;95m{"PROCESSANDO" + ponto:^25}\033[0m', end='', flush=True)
                            sleep(1.5)
                        print()
                        print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                        print(f'{cor["verde"]}RESULTADO{cor["limpa"]}')
                        print(f'{cor["branco"]}A soma entre{cor["limpa"]} {n1_colorido} {cor["branco"]}+{cor["limpa"]} '
                              f'{n2_colorido} {cor["branco"]}+{cor["limpa"]} {n3_colorido} '
                              f'{cor["branco"]}+{cor["limpa"]} {n4_colorido}{cor["branco"]} é ={cor["limpa"]} {result_colorido}')
                        continuar = ''
                        while True:
                            continuar = input(
                                f'{cor["amarelo"]}Deseja converter outro valor? (S/N): {cor["limpa"]}').upper().strip()
                            print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                            if continuar in ['S', 'SIM']:
                                break
                            elif continuar in ['NÃO', 'NAO', 'N']:
                                print(
                                    f'{cor["ciano"]}SAINDO DO CALCULO{cor["limpa"]}', end='')
                                for c in range(3):
                                    print(f'{cor["ciano"]}.{cor["limpa"]}',
                                          end='', flush=True)
                                    sleep(1)
                                break
                            elif continuar not in ['SIM', 'S']:
                                print(
                                    f'{cor["vermelho"]}OPÇÃO INVALIDA! TENTE NOVAMENTE.{cor["limpa"]}'
                                )
                                print(f'{cor["branco"]}─{cor["limpa"]}' * 25)

                        if continuar in ['NÃO', 'NAO', 'N']:
                            break
                    else:
                        print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                        print(
                            f'{cor["vermelho"]}OPERAÇÃO INVÁLIDA! UTILIZE APENAS: {cor["limpa"]}'
                            f'{cor["verde"]}1s{cor["limpa"]} {cor["branco"]}E{cor["limpa"]} {cor["vermelho"]}0s{cor["limpa"]}'
                            f'{cor["branco"]}.{cor["limpa"]}'
                        )
                        print(f'{cor["branco"]}─{cor["limpa"]}' * 25)

        # ── SUBTRAÇÃO ───────────────────────────
        elif escolha == 2:
            while True:
                print(f'{cor["amarelo"]}QUANTAS PARCELAS DESEJA:{cor["limpa"]}')
                print(
                    f'{cor["branco"]}DIGITE{cor["limpa"]} {cor["verde"]}[1]{cor["limpa"]} {cor["branco"]}PARA DUAS PARCELAS{cor["limpa"]}')
                print(
                    f'{cor["branco"]}DIGITE{cor["limpa"]} {cor["verde"]}[2]{cor["limpa"]} {cor["branco"]}PARA TRÊS PARCELAS{cor["limpa"]}')
                print(
                    f'{cor["branco"]}DIGITE{cor["limpa"]} {cor["verde"]}[3]{cor["limpa"]} {cor["branco"]}PARA QUATRO PARCELAS{cor["limpa"]}')
                print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                num_str = str(
                    input(f'{cor["roxo"]}DIGITE AQUI: {cor["limpa"]}'))
                print(f'{cor["branco"]}─{cor["limpa"]}' * 25)

                num = 0
                if num_str.isdigit():
                    num = int(num_str)
                if 1 <= num <= 3:
                    break
                elif num_str.isdigit():
                    print(
                        f'{cor["vermelho"]}OPÇÃO INVÁLIDA! DIGITE OS VALORES: "1", "2" OU "3".{cor["limpa"]}'
                    )
                    print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                else:
                    print(
                        f'{cor["vermelho"]}OPÇÃO INVÁLIDA! DIGITE SOMENTE NÚMEROS.{cor["limpa"]}'
                    )
                    print(f'{cor["branco"]}─{cor["limpa"]}' * 25)

            if num == 1:
                print(
                    f'{cor["verde"]}CERTO. VAMOS REALIZAR A OPERAÇÃO.{cor["limpa"]}')
                print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                while True:
                    n1_str = input(
                        f'{cor["branco"]}Primeira Parcela: {cor["limpa"]}')
                    n2_str = input(
                        f'{cor["branco"]}Segunda Parcela: {cor["limpa"]}')
                    if all(c in '01' for c in n1_str) and all(c in '01' for c in n2_str):
                        n1_dec = int(n1_str, 2)
                        n2_dec = int(n2_str, 2)
                        somar_dec = n1_dec - n2_dec
                        result_bin = bin(somar_dec)
                        result_str = str(result_bin[2:]).replace(
                            '1', 'V').replace('0', 'F')
                        n1_c = n1_str.replace('1', 'V').replace('0', 'F')
                        n2_c = n2_str.replace('1', 'V').replace('0', 'F')
                        n1_colorido = n1_c.replace('F', f'{cor["vermelho"]}0{cor["limpa"]}').replace(
                            'V', f'{cor["verde"]}1{cor["limpa"]}')
                        n2_colorido = n2_c.replace('F', f'{cor["vermelho"]}0{cor["limpa"]}').replace(
                            'V', f'{cor["verde"]}1{cor["limpa"]}')
                        result_colorido = result_str.replace('F', f'{cor["vermelho"]}0{cor["limpa"]}').replace(
                            'V', f'{cor["verde"]}1{cor["limpa"]}')
                        print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                        for c in range(4):
                            ponto = f'.' * c
                            print(
                                f'\r\033[1;95m{"PROCESSANDO" + ponto:^25}\033[0m', end='', flush=True)
                            sleep(1.5)
                        print()
                        print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                        print(f'{cor["verde"]}RESULTADO{cor["limpa"]}')
                        if somar_dec < 0:
                            result_format = f'{result_bin[0] + result_bin[3:]}'
                            result_str2 = str(result_format).replace(
                                '1', 'V').replace('0', 'F')
                            result_colorido1 = (result_str2
                                                .replace('-', f'{cor["vermelho"]}-{cor["limpa"]}')
                                                .replace('F', f'{cor["vermelho"]}0{cor["limpa"]}')
                                                .replace('V', f'{cor["verde"]}1{cor["limpa"]}'))
                            print(
                                f'A subtração entre {n1_colorido} - {n2_colorido} é = {result_colorido1}')
                        else:
                            print(
                                f'A subtração entre {n1_colorido} - {n2_colorido} é = {result_colorido}')
                        continuar = ''
                        while True:
                            continuar = input(
                                f'{cor["amarelo"]}Deseja converter outro valor? (S/N): {cor["limpa"]}').upper().strip()
                            print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                            if continuar in ['S', 'SIM']:
                                break
                            elif continuar in ['NÃO', 'NAO', 'N']:
                                print(
                                    f'{cor["ciano"]}SAINDO DO CALCULO{cor["limpa"]}', end='')
                                for c in range(3):
                                    print(f'{cor["ciano"]}.{cor["limpa"]}',
                                          end='', flush=True)
                                    sleep(1)
                                break
                            elif continuar not in ['SIM', 'S']:
                                print(
                                    f'{cor["vermelho"]}OPÇÃO INVALIDA! TENTE NOVAMENTE.{cor["limpa"]}'
                                )
                                print(f'{cor["branco"]}─{cor["limpa"]}' * 25)

                        if continuar in ['NÃO', 'NAO', 'N']:
                            break
                    else:
                        print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                        print(
                            f'{cor["vermelho"]}OPERAÇÃO INVÁLIDA! UTILIZE APENAS: {cor["limpa"]}'
                            f'{cor["verde"]}1s{cor["limpa"]} {cor["branco"]}E{cor["limpa"]} {cor["vermelho"]}0s{cor["limpa"]}'
                            f'{cor["branco"]}.{cor["limpa"]}'
                        )
                        print(f'{cor["branco"]}─{cor["limpa"]}' * 25)

            elif num == 2:
                print(
                    f'{cor["verde"]}CERTO. VAMOS REALIZAR AS OPERAÇÕES.{cor["limpa"]}')
                print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                while True:
                    n1_str = input(
                        f'{cor["branco"]}Primeira Parcela: {cor["limpa"]}')
                    n2_str = input(
                        f'{cor["branco"]}Segunda Parcela: {cor["limpa"]}')
                    n3_str = input(
                        f'{cor["branco"]}Terceira Parcela: {cor["limpa"]}')
                    if all(c in '01' for c in n1_str) and all(c in '01' for c in n2_str) and all(c in '01' for c in n3_str):
                        n1_dec = int(n1_str, 2)
                        n2_dec = int(n2_str, 2)
                        n3_dec = int(n3_str, 2)
                        somar_dec = n1_dec - n2_dec - n3_dec
                        result_bin = bin(somar_dec)
                        result_str = str(result_bin[2:]).replace(
                            '1', 'V').replace('0', 'F')
                        n1_c = n1_str.replace('1', 'V').replace('0', 'F')
                        n2_c = n2_str.replace('1', 'V').replace('0', 'F')
                        n3_c = n3_str.replace('1', 'V').replace('0', 'F')
                        n1_colorido = n1_c.replace('F', f'{cor["vermelho"]}0{cor["limpa"]}').replace(
                            'V', f'{cor["verde"]}1{cor["limpa"]}')
                        n2_colorido = n2_c.replace('F', f'{cor["vermelho"]}0{cor["limpa"]}').replace(
                            'V', f'{cor["verde"]}1{cor["limpa"]}')
                        n3_colorido = n3_c.replace('F', f'{cor["vermelho"]}0{cor["limpa"]}').replace(
                            'V', f'{cor["verde"]}1{cor["limpa"]}')
                        result_colorido = result_str.replace(
                            'F', f'{cor["vermelho"]}0{cor["limpa"]}')
                        print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                        for c in range(4):
                            ponto = f'.' * c
                            print(
                                f'\r\033[1;95m{"PROCESSANDO" + ponto:^25}\033[0m', end='', flush=True)
                            sleep(1.5)
                        print()
                        print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                        print(f'{cor["verde"]}RESULTADO{cor["limpa"]}')
                        if somar_dec < 0:
                            result_format = f'{result_bin[0] + result_bin[3:]}'
                            result_str2 = str(result_format).replace(
                                '1', 'V').replace('0', 'F')
                            result_colorido1 = (result_str2
                                                .replace('-', f'{cor["vermelho"]}-{cor["limpa"]}')
                                                .replace('F', f'{cor["vermelho"]}0{cor["limpa"]}')
                                                .replace('V', f'{cor["verde"]}1{cor["limpa"]}'))
                            print(
                                f'A subtração entre {n1_colorido} - {n2_colorido} - {n3_colorido} é = {result_colorido1}')
                        else:
                            print(
                                f'A subtração entre {n1_colorido} - {n2_colorido} - {n3_colorido} é = {result_colorido}')
                        continuar = ''
                        while True:
                            continuar = input(
                                f'{cor["amarelo"]}Deseja converter outro valor? (S/N): {cor["limpa"]}').upper().strip()
                            print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                            if continuar in ['S', 'SIM']:
                                break
                            elif continuar in ['NÃO', 'NAO', 'N']:
                                print(
                                    f'{cor["ciano"]}SAINDO DO CALCULO{cor["limpa"]}', end='')
                                for c in range(3):
                                    print(f'{cor["ciano"]}.{cor["limpa"]}',
                                          end='', flush=True)
                                    sleep(1)
                                break
                            elif continuar not in ['SIM', 'S']:
                                print(
                                    f'{cor["vermelho"]}OPÇÃO INVALIDA! TENTE NOVAMENTE.{cor["limpa"]}'
                                )
                                print(f'{cor["branco"]}─{cor["limpa"]}' * 25)

                        if continuar in ['NÃO', 'NAO', 'N']:
                            break
                    else:
                        print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                        print(
                            f'{cor["vermelho"]}OPERAÇÃO INVÁLIDA! UTILIZE APENAS: {cor["limpa"]}'
                            f'{cor["verde"]}1s{cor["limpa"]} {cor["branco"]}E{cor["limpa"]} {cor["vermelho"]}0s{cor["limpa"]}'
                            f'{cor["branco"]}.{cor["limpa"]}'
                        )
                        print(f'{cor["branco"]}─{cor["limpa"]}' * 25)

            elif num == 3:
                print(
                    f'{cor["verde"]}CERTO. VAMOS REALIZAR AS OPERAÇÕES.{cor["limpa"]}')
                print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                while True:
                    n1_str = input(
                        f'{cor["branco"]}Primeira Parcela: {cor["limpa"]}')
                    n2_str = input(
                        f'{cor["branco"]}Segunda Parcela: {cor["limpa"]}')
                    n3_str = input(
                        f'{cor["branco"]}Terceira Parcela: {cor["limpa"]}')
                    n4_str = input(
                        f'{cor["branco"]}Quarta Parcela: {cor["limpa"]}')
                    if all(c in '01' for c in n1_str) and all(c in '01' for c in n2_str) and all(c in '01' for c in n3_str) and all(c in '01' for c in n4_str):
                        n1_dec = int(n1_str, 2)
                        n2_dec = int(n2_str, 2)
                        n3_dec = int(n3_str, 2)
                        n4_dec = int(n4_str, 2)
                        somar_dec = n1_dec - n2_dec - n3_dec - n4_dec
                        result_bin = bin(somar_dec)
                        result_str = str(result_bin[2:]).replace(
                            '1', 'V').replace('0', 'F')
                        n1_c = n1_str.replace('1', 'V').replace('0', 'F')
                        n2_c = n2_str.replace('1', 'V').replace('0', 'F')
                        n3_c = n3_str.replace('1', 'V').replace('0', 'F')
                        n4_c = n4_str.replace('1', 'V').replace('0', 'F')
                        n1_colorido = n1_c.replace('F', f'{cor["vermelho"]}0{cor["limpa"]}').replace(
                            'V', f'{cor["verde"]}1{cor["limpa"]}')
                        n2_colorido = n2_c.replace('F', f'{cor["vermelho"]}0{cor["limpa"]}').replace(
                            'V', f'{cor["verde"]}1{cor["limpa"]}')
                        n3_colorido = n3_c.replace('F', f'{cor["vermelho"]}0{cor["limpa"]}').replace(
                            'V', f'{cor["verde"]}1{cor["limpa"]}')
                        n4_colorido = n4_c.replace('F', f'{cor["vermelho"]}0{cor["limpa"]}').replace(
                            'V', f'{cor["verde"]}1{cor["limpa"]}')
                        result_colorido = result_str.replace('F', f'{cor["vermelho"]}0{cor["limpa"]}').replace(
                            'V', f'{cor["verde"]}1{cor["limpa"]}')
                        print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                        for c in range(4):
                            ponto = f'.' * c
                            print(
                                f'\r\033[1;95m{"PROCESSANDO" + ponto:^25}\033[0m', end='', flush=True)
                            sleep(1.5)
                        print()
                        print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                        print(f'{cor["verde"]}RESULTADO{cor["limpa"]}')
                        if somar_dec < 0:
                            result_format = f'{result_bin[0] + result_bin[3:]}'
                            result_str2 = str(result_format).replace(
                                '1', 'V').replace('0', 'F')
                            result_colorido1 = (result_str2
                                                .replace('-', f'{cor["vermelho"]}-{cor["limpa"]}')
                                                .replace('F', f'{cor["vermelho"]}0{cor["limpa"]}')
                                                .replace('V', f'{cor["verde"]}1{cor["limpa"]}'))
                            print(f'A subtração entre {n1_colorido} - {n2_colorido} - {n3_colorido} - {n4_colorido} '
                                  f'é = {result_colorido1}')
                        else:
                            print(f'A subtração entre {n1_colorido} - {n2_colorido} - {n3_colorido} - {n4_colorido} '
                                  f'é = {result_colorido}')
                        continuar = ''
                        while True:
                            continuar = input(
                                f'{cor["amarelo"]}Deseja converter outro valor? (S/N): {cor["limpa"]}').upper().strip()
                            print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                            if continuar in ['S', 'SIM']:
                                break
                            elif continuar in ['NÃO', 'NAO', 'N']:
                                print(
                                    f'{cor["ciano"]}SAINDO DO CALCULO{cor["limpa"]}', end='')
                                for c in range(3):
                                    print(f'{cor["ciano"]}.{cor["limpa"]}',
                                          end='', flush=True)
                                    sleep(1)
                                break
                            elif continuar not in ['SIM', 'S']:
                                print(
                                    f'{cor["vermelho"]}OPÇÃO INVALIDA! TENTE NOVAMENTE.{cor["limpa"]}'
                                )
                                print(f'{cor["branco"]}─{cor["limpa"]}' * 25)

                        if continuar in ['NÃO', 'NAO', 'N']:
                            break
                    else:
                        print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                        print(
                            f'{cor["vermelho"]}OPERAÇÃO INVÁLIDA! UTILIZE APENAS: {cor["limpa"]}'
                            f'{cor["verde"]}1s{cor["limpa"]} {cor["branco"]}E{cor["limpa"]} {cor["vermelho"]}0s{cor["limpa"]}'
                            f'{cor["branco"]}.{cor["limpa"]}'
                        )
                        print(f'{cor["branco"]}─{cor["limpa"]}' * 25)

    # ─────────────────────────────────────────────
    # OPÇÃO 4 – TABELA VERDADE
    # ─────────────────────────────────────────────
    elif escolhido == 4:
        escolha = 0
        print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
        while True:
            while True:
                print(f'{cor["roxo"]}QUANTAS PROPOSIÇÕES DESEJA?{cor["limpa"]}')
                print(
                    f'{cor["verde"]}[ 1 ]{cor["limpa"]} {cor["branco"]}PARA UMA PROPOSIÇÃO: ["a"]{cor["limpa"]}')
                print(
                    f'{cor["verde"]}[ 2 ]{cor["limpa"]} {cor["branco"]}PARA DUAS PROPOSIÇÃO: ["a", "b"]{cor["limpa"]}')
                print(
                    f'{cor["verde"]}[ 3 ]{cor["limpa"]} {cor["branco"]}PARA TRÊS PROPOSIÇÃO: ["a","b","c"]{cor["limpa"]}')
                print(
                    f'{cor["verde"]}[ 4 ]{cor["limpa"]} {cor["branco"]}PARA QUATRO PROPOSIÇÃO: ["a","b","c","d"]{cor["limpa"]}')
                escolha_str = str(
                    input(f'{cor["roxo"]}DIGITE AQUI: {cor["limpa"]}'))
                if escolha_str.isdigit():
                    escolha = int(escolha_str)
                if 1 <= escolha <= 4:
                    break
                elif escolha_str.isdigit():
                    print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                    print(
                        f'{cor["vermelho"]}VALOR INVÁLIDO! UTILIZE VALORES DE :{cor["limpa"]} '
                        f'{cor["branco"]}1 ATE 4.{cor["limpa"]}'
                    )
                    print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                elif escolha_str.isalpha():
                    print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                    print(
                        f'{cor["vermelho"]}UTILIZE NÚMEROS.{cor["limpa"]} '
                    )
                    print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                else:
                    print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                    print(
                        f'{cor["vermelho"]}UTILIZE APENAS NÚMEROS.{cor["limpa"]} '
                    )
                    print(f'{cor["branco"]}─{cor["limpa"]}' * 25)

            if escolha == 1:
                print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                for c in range(4):
                    ponto = f'.' * c
                    print(
                        f'\r\033[1;95m{"PROCESSANDO" + ponto:^25}\033[0m', end='', flush=True)
                    sleep(1.5)
                print()
                print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                print(f'{cor["verde"]}RESULTADO{cor["limpa"]}')
                tabela = ttg.Truths(['a'], ascending=True)
                tabela_str = str(tabela).replace('1', 'V').replace('0', 'F')
                tabela_colorida = (tabela_str
                                   .replace('F', f'{cor["vermelho"]}0{cor["limpa"]}')
                                   .replace('V', f'{cor["verde"]}1{cor["limpa"]}')
                                   .replace('|', f'{cor["amarelo"]}|{cor["limpa"]}')
                                   .replace('+', f'{cor["amarelo"]}+{cor["limpa"]}')
                                   .replace('-', f'{cor["ciano"]}-{cor["limpa"]}')
                                   .replace('a', f'{cor["branco"]}a{cor["limpa"]}'))
                print(tabela_colorida)
                continuar = ''
                while True:
                    continuar = input(
                        f'{cor["amarelo"]}Deseja visualizar outra tabela? (S/N): {cor["limpa"]}').upper().strip()
                    print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                    if continuar in ['S', 'SIM']:
                        break
                    elif continuar in ['NÃO', 'NAO', 'N']:
                        print(
                            f'{cor["ciano"]}SAINDO DA TABELA VERDADE{cor["limpa"]}', end='')
                        for c in range(3):
                            print(f'{cor["ciano"]}.{cor["limpa"]}',
                                  end='', flush=True)
                            sleep(1)
                        break
                    elif continuar not in ['SIM', 'S']:
                        print(
                            f'{cor["vermelho"]}OPÇÃO INVALIDA! TENTE NOVAMENTE.{cor["limpa"]}'
                        )
                        print(f'{cor["branco"]}─{cor["limpa"]}' * 25)

                if continuar in ['NÃO', 'NAO', 'N']:
                    break

            elif escolha == 2:
                print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                for c in range(4):
                    ponto = f'.' * c
                    print(
                        f'\r\033[1;95m{"PROCESSANDO" + ponto:^25}\033[0m', end='', flush=True)
                    sleep(1.5)
                print()
                print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                print(f'{cor["verde"]}RESULTADO{cor["limpa"]}')
                tabela = ttg.Truths(['a', 'b'], ascending=True)
                tabela_str = str(tabela).replace('1', 'V').replace('0', 'F')
                tabela_colorida = (tabela_str
                                   .replace('F', f'{cor["vermelho"]}0{cor["limpa"]}')
                                   .replace('V', f'{cor["verde"]}1{cor["limpa"]}')
                                   .replace('|', f'{cor["amarelo"]}|{cor["limpa"]}')
                                   .replace('+', f'{cor["amarelo"]}+{cor["limpa"]}')
                                   .replace('-', f'{cor["ciano"]}-{cor["limpa"]}')
                                   .replace('a', f'{cor["branco"]}a{cor["limpa"]}')
                                   .replace('b', f'{cor["branco"]}b{cor["limpa"]}'))
                print(tabela_colorida)
                continuar = ''
                while True:
                    continuar = input(
                        f'{cor["amarelo"]}Deseja visualizar outra tabela? (S/N): {cor["limpa"]}').upper().strip()
                    print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                    if continuar in ['S', 'SIM']:
                        break
                    elif continuar in ['NÃO', 'NAO', 'N']:
                        print(
                            f'{cor["ciano"]}SAINDO DA TABELA VERDADE{cor["limpa"]}', end='')
                        for c in range(3):
                            print(f'{cor["ciano"]}.{cor["limpa"]}',
                                  end='', flush=True)
                            sleep(1)
                        break
                    elif continuar not in ['SIM', 'S']:
                        print(
                            f'{cor["vermelho"]}OPÇÃO INVALIDA! TENTE NOVAMENTE.{cor["limpa"]}'
                        )
                        print(f'{cor["branco"]}─{cor["limpa"]}' * 25)

                if continuar in ['NÃO', 'NAO', 'N']:
                    break

            elif escolha == 3:
                print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                for c in range(4):
                    ponto = f'.' * c
                    print(
                        f'\r\033[1;95m{"PROCESSANDO" + ponto:^25}\033[0m', end='', flush=True)
                    sleep(1.5)
                print()
                print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                print(f'{cor["verde"]}RESULTADO{cor["limpa"]}')
                tabela = ttg.Truths(['a', 'b', 'c'], ascending=True)
                tabela_str = str(tabela).replace(
                    '1', 'V').replace('0', 'F')
                tabela_colorida = (tabela_str
                                   .replace('F', f'{cor["vermelho"]}0{cor["limpa"]}')
                                   .replace('V', f'{cor["verde"]}1{cor["limpa"]}')
                                   .replace('|', f'{cor["amarelo"]}|{cor["limpa"]}')
                                   .replace('+', f'{cor["amarelo"]}+{cor["limpa"]}')
                                   .replace('-', f'{cor["ciano"]}-{cor["limpa"]}')
                                   .replace('a', f'{cor["branco"]}a{cor["limpa"]}')
                                   .replace('b', f'{cor["branco"]}b{cor["limpa"]}')
                                   .replace('c', f'{cor["branco"]}c{cor["limpa"]}'))
                print(tabela_colorida)
                continuar = ''
                while True:
                    continuar = input(
                        f'{cor["amarelo"]}Deseja visualizar outra tabela? (S/N): {cor["limpa"]}').upper().strip()
                    print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                    if continuar in ['S', 'SIM']:
                        break
                    elif continuar in ['NÃO', 'NAO', 'N']:
                        print(
                            f'{cor["ciano"]}SAINDO DA TABELA VERDADE{cor["limpa"]}', end='')
                        for c in range(3):
                            print(f'{cor["ciano"]}.{cor["limpa"]}',
                                  end='', flush=True)
                            sleep(1)
                        break
                    elif continuar not in ['SIM', 'S']:
                        print(
                            f'{cor["vermelho"]}OPÇÃO INVALIDA! TENTE NOVAMENTE.{cor["limpa"]}'
                        )
                        print(f'{cor["branco"]}─{cor["limpa"]}' * 25)

                if continuar in ['NÃO', 'NAO', 'N']:
                    break

            elif escolha == 4:
                print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                for c in range(4):
                    ponto = f'.' * c
                    print(
                        f'\r\033[1;95m{"PROCESSANDO" + ponto:^25}\033[0m', end='', flush=True)
                    sleep(1.5)
                print()
                print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                print(f'{cor["verde"]}RESULTADO{cor["limpa"]}')
                tabela = ttg.Truths(['a', 'b', 'c', 'd'], ascending=True)
                tabela_str = str(tabela).replace(
                    '1', 'V').replace('0', 'F')
                tabela_colorida = (tabela_str
                                   .replace('F', f'{cor["vermelho"]}0{cor["limpa"]}')
                                   .replace('V', f'{cor["verde"]}1{cor["limpa"]}')
                                   .replace('|', f'{cor["amarelo"]}|{cor["limpa"]}')
                                   .replace('+', f'{cor["amarelo"]}+{cor["limpa"]}')
                                   .replace('-', f'{cor["ciano"]}-{cor["limpa"]}')
                                   .replace('a', f'{cor["branco"]}a{cor["limpa"]}')
                                   .replace('b', f'{cor["branco"]}b{cor["limpa"]}')
                                   .replace('c', f'{cor["branco"]}c{cor["limpa"]}')
                                   .replace('d', f'{cor["branco"]}d{cor["limpa"]}'))
                print(tabela_colorida)
                continuar = ''
                while True:
                    continuar = input(
                        f'{cor["amarelo"]}Deseja visualizar outra tabela? (S/N): {cor["limpa"]}').upper().strip()
                    print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                    if continuar in ['S', 'SIM']:
                        break
                    elif continuar in ['NÃO', 'NAO', 'N']:
                        print(
                            f'{cor["ciano"]}SAINDO DA TABELA VERDADE{cor["limpa"]}', end='')
                        for c in range(3):
                            print(f'{cor["ciano"]}.{cor["limpa"]}',
                                  end='', flush=True)
                            sleep(1)
                        break
                    elif continuar not in ['SIM', 'S']:
                        print(
                            f'{cor["vermelho"]}OPÇÃO INVALIDA! TENTE NOVAMENTE.{cor["limpa"]}'
                        )
                        print(f'{cor["branco"]}─{cor["limpa"]}' * 25)

                if continuar in ['NÃO', 'NAO', 'N']:
                    break

    # ─────────────────────────────────────────────
    # OPÇÃO 5 – EXPRESSÕES BOOLEANAS
    # ─────────────────────────────────────────────
    elif escolhido == 5:
        titulo = 'EXPRESSÕES BOOLEANAS'
        print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
        print(f'{cor["ciano"]}{titulo:^25}{cor["limpa"]}')
        print(f'{cor["branco"]}─{cor["limpa"]}' * 25)

        while True:
            valor1 = input(
                f'{cor["branco"]}Primeira Proposição: {cor["limpa"]}')
            valor2 = input(
                f'{cor["branco"]}Segunda Proposição: {cor["limpa"]}')
            if 'a' <= valor1 <= 'd' and 'a' <= valor2 <= 'd':
                while True:
                    funcao0 = input(
                        f'{cor["branco"]}Qual o Operador? {cor["limpa"]}').lower().strip()
                    funcao = funcao0
                    if funcao0 == '&&':
                        funcao = 'and'
                    elif funcao0 == '||':
                        funcao = 'or'
                    if funcao0 not in ['&&', 'and', '||', 'or']:
                        print(
                            f'{cor["vermelho"]}OPÇÃO INVÁLIDA! TENTE NOVAMENTE.{cor["limpa"]}'
                        )
                    else:
                        break
                if funcao == 'and' or funcao == 'or':
                    while True:
                        neg = input(
                            f'{cor["vermelho"]}Esta Negativado? {cor["limpa"]}').upper().strip()
                        tabela = input(
                            f'{cor["branco"]}ATÉ QUE PROPOSIÇÃO DESEJA IR? {cor["limpa"]}').lower()
                        print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                        if neg in ['SIM', 'S', 'N', 'NÃO', 'NAO'] and tabela in ['b', 'c', 'd']:
                            break
                        else:
                            print(
                                f'{cor["vermelho"]}OPÇÃO INVÁLIDA! TENTE NOVAMENTE.{cor["limpa"]}'
                            )
                            print(f'{cor["branco"]}─{cor["limpa"]}' * 25)

                    if neg in ['SIM', 'S']:
                        print(
                            f'{cor["amarelo"]}O QUE ESTA NEGATIVADO?{cor["limpa"]}')
                        print(f'{cor["branco"]}OPÇÃO{cor["limpa"]} {cor["verde"]}[1]{cor["limpa"]}'
                              f'{cor["branco"]}: "{cor["limpa"]}'
                              f'{cor["vermelho"]}not ({valor1}){cor["limpa"]}{cor["branco"]}"{cor["limpa"]}')
                        print(f'{cor["branco"]}OPÇÃO{cor["limpa"]} {cor["verde"]}[2]{cor["limpa"]}'
                              f'{cor["branco"]}: "{cor["limpa"]}{cor["vermelho"]}not ({valor2}){cor["limpa"]}'
                              f'{cor["branco"]}"{cor["limpa"]}')
                        print(f'{cor["branco"]}OPÇÃO{cor["limpa"]} {cor["verde"]}[3]{cor["limpa"]}'
                              f'{cor["branco"]}: "{cor["limpa"]}{cor["vermelho"]}'
                              f'not ({valor1} {funcao} {valor2}){cor["limpa"]}{cor["branco"]}"{cor["limpa"]}')
                        while True:
                            escolha_str = str(
                                input(f'{cor["roxo"]}DIGITE A OPÇÃO: {cor["limpa"]}')).strip()

                        # ── Tabela até b ──────────────────────────
                        if escolha == 1 and tabela == 'b':
                            tabela_obj = ttg.Truths(
                                ['a', 'b'], [f'(not {valor1}) {funcao} {valor2}'], ascending=True)
                            tabela_str = str(tabela_obj).replace(
                                '1', 'V').replace('0', 'F')
                            tabela_colorida = (tabela_str
                                               .replace('F', f'{cor["vermelho"]}0{cor["limpa"]}')
                                               .replace('V', f'{cor["verde"]}1{cor["limpa"]}')
                                               .replace('|', f'{cor["amarelo"]}|{cor["limpa"]}')
                                               .replace('+', f'{cor["amarelo"]}+{cor["limpa"]}')
                                               .replace('-', f'{cor["ciano"]}-{cor["limpa"]}')
                                               .replace('a', f'{cor["branco"]}a{cor["limpa"]}')
                                               .replace('b', f'{cor["branco"]}b{cor["limpa"]}')
                                               .replace('not', f'{cor["branco"]}not{cor["limpa"]}')
                                               .replace('or', f'{cor["branco"]}or{cor["limpa"]}')
                                               .replace('nd', f'{cor["branco"]}nd{cor["limpa"]}')
                                               .replace('(', f'{cor["branco"]}({cor["limpa"]}')
                                               .replace(')', f'{cor["branco"]}){cor["limpa"]}'))
                            print(tabela_colorida)
                        elif escolha == 2 and tabela == 'b':
                            tabela_obj = ttg.Truths(
                                ['a', 'b'], [f'{valor1} {funcao} (not {valor2})'], ascending=True)
                            tabela_str = str(tabela_obj).replace(
                                '1', 'V').replace('0', 'F')
                            tabela_colorida = (tabela_str
                                               .replace('F', f'{cor["vermelho"]}0{cor["limpa"]}')
                                               .replace('V', f'{cor["verde"]}1{cor["limpa"]}')
                                               .replace('|', f'{cor["amarelo"]}|{cor["limpa"]}')
                                               .replace('+', f'{cor["amarelo"]}+{cor["limpa"]}')
                                               .replace('-', f'{cor["ciano"]}-{cor["limpa"]}')
                                               .replace('a', f'{cor["branco"]}a{cor["limpa"]}')
                                               .replace('b', f'{cor["branco"]}b{cor["limpa"]}')
                                               .replace('not', f'{cor["branco"]}not{cor["limpa"]}')
                                               .replace('or', f'{cor["branco"]}or{cor["limpa"]}')
                                               .replace('nd', f'{cor["branco"]}nd{cor["limpa"]}')
                                               .replace('(', f'{cor["branco"]}({cor["limpa"]}')
                                               .replace(')', f'{cor["branco"]}){cor["limpa"]}'))
                            print(tabela_colorida)
                        elif escolha == 3 and tabela == 'b':
                            tabela_obj = ttg.Truths(
                                ['a', 'b'], [f'not ({valor1} {funcao} {valor2})'], ascending=True)
                            tabela_str = str(tabela_obj).replace(
                                '1', 'V').replace('0', 'F')
                            tabela_colorida = (tabela_str
                                               .replace('F', f'{cor["vermelho"]}0{cor["limpa"]}')
                                               .replace('V', f'{cor["verde"]}1{cor["limpa"]}')
                                               .replace('|', f'{cor["amarelo"]}|{cor["limpa"]}')
                                               .replace('+', f'{cor["amarelo"]}+{cor["limpa"]}')
                                               .replace('-', f'{cor["ciano"]}-{cor["limpa"]}')
                                               .replace('a', f'{cor["branco"]}a{cor["limpa"]}')
                                               .replace('b', f'{cor["branco"]}b{cor["limpa"]}')
                                               .replace('not', f'{cor["branco"]}not{cor["limpa"]}')
                                               .replace('or', f'{cor["branco"]}or{cor["limpa"]}')
                                               .replace('nd', f'{cor["branco"]}nd{cor["limpa"]}')
                                               .replace('(', f'{cor["branco"]}({cor["limpa"]}')
                                               .replace(')', f'{cor["branco"]}){cor["limpa"]}'))
                            print(tabela_colorida)
                        # ── Tabela até c ──────────────────────────
                        elif escolha == 1 and tabela == 'c':
                            tabela_obj = ttg.Truths(
                                ['a', 'b', 'c'], [f'(not {valor1}) {funcao} {valor2}'], ascending=True)
                            tabela_str = str(tabela_obj).replace(
                                '1', 'V').replace('0', 'F')
                            tabela_colorida = (tabela_str
                                               .replace('F', f'{cor["vermelho"]}0{cor["limpa"]}')
                                               .replace('V', f'{cor["verde"]}1{cor["limpa"]}')
                                               .replace('|', f'{cor["amarelo"]}|{cor["limpa"]}')
                                               .replace('+', f'{cor["amarelo"]}+{cor["limpa"]}')
                                               .replace('-', f'{cor["ciano"]}-{cor["limpa"]}')
                                               .replace('a', f'{cor["branco"]}a{cor["limpa"]}')
                                               .replace('b', f'{cor["branco"]}b{cor["limpa"]}')
                                               .replace('c', f'{cor["branco"]}c{cor["limpa"]}')
                                               .replace('not', f'{cor["branco"]}not{cor["limpa"]}')
                                               .replace('or', f'{cor["branco"]}or{cor["limpa"]}')
                                               .replace('nd', f'{cor["branco"]}nd{cor["limpa"]}')
                                               .replace('(', f'{cor["branco"]}({cor["limpa"]}')
                                               .replace(')', f'{cor["branco"]}){cor["limpa"]}'))
                            print(tabela_colorida)
                        elif escolha == 2 and tabela == 'c':
                            tabela_obj = ttg.Truths(
                                ['a', 'b', 'c'], [f'{valor1} {funcao} (not {valor2})'], ascending=True)
                            tabela_str = str(tabela_obj).replace(
                                '1', 'V').replace('0', 'F')
                            tabela_colorida = (tabela_str
                                               .replace('F', f'{cor["vermelho"]}0{cor["limpa"]}')
                                               .replace('V', f'{cor["verde"]}1{cor["limpa"]}')
                                               .replace('|', f'{cor["amarelo"]}|{cor["limpa"]}')
                                               .replace('+', f'{cor["amarelo"]}+{cor["limpa"]}')
                                               .replace('-', f'{cor["ciano"]}-{cor["limpa"]}')
                                               .replace('a', f'{cor["branco"]}a{cor["limpa"]}')
                                               .replace('b', f'{cor["branco"]}b{cor["limpa"]}')
                                               .replace('c', f'{cor["branco"]}c{cor["limpa"]}')
                                               .replace('not', f'{cor["branco"]}not{cor["limpa"]}')
                                               .replace('or', f'{cor["branco"]}or{cor["limpa"]}')
                                               .replace('nd', f'{cor["branco"]}nd{cor["limpa"]}')
                                               .replace('(', f'{cor["branco"]}({cor["limpa"]}')
                                               .replace(')', f'{cor["branco"]}){cor["limpa"]}'))
                            print(tabela_colorida)
                        elif escolha == 3 and tabela == 'c':
                            tabela_obj = ttg.Truths(
                                ['a', 'b', 'c'], [f'not ({valor1} {funcao} {valor2})'], ascending=True)
                            tabela_str = str(tabela_obj).replace(
                                '1', 'V').replace('0', 'F')
                            tabela_colorida = (tabela_str
                                               .replace('F', f'{cor["vermelho"]}0{cor["limpa"]}')
                                               .replace('V', f'{cor["verde"]}1{cor["limpa"]}')
                                               .replace('|', f'{cor["amarelo"]}|{cor["limpa"]}')
                                               .replace('+', f'{cor["amarelo"]}+{cor["limpa"]}')
                                               .replace('-', f'{cor["ciano"]}-{cor["limpa"]}')
                                               .replace('a', f'{cor["branco"]}a{cor["limpa"]}')
                                               .replace('b', f'{cor["branco"]}b{cor["limpa"]}')
                                               .replace('c', f'{cor["branco"]}c{cor["limpa"]}')
                                               .replace('not', f'{cor["branco"]}not{cor["limpa"]}')
                                               .replace('or', f'{cor["branco"]}or{cor["limpa"]}')
                                               .replace('nd', f'{cor["branco"]}nd{cor["limpa"]}')
                                               .replace('(', f'{cor["branco"]}({cor["limpa"]}')
                                               .replace(')', f'{cor["branco"]}){cor["limpa"]}'))
                            print(tabela_colorida)
                        # ── Tabela até d ──────────────────────────
                        elif escolha == 1 and tabela == 'd':
                            tabela_obj = ttg.Truths(['a', 'b', 'c', 'd'], [
                                                    f'(not {valor1}) {funcao} {valor2}'], ascending=True)
                            tabela_str = str(tabela_obj).replace(
                                '1', 'V').replace('0', 'F')
                            tabela_colorida = (tabela_str
                                               .replace('F', f'{cor["vermelho"]}0{cor["limpa"]}')
                                               .replace('V', f'{cor["verde"]}1{cor["limpa"]}')
                                               .replace('|', f'{cor["amarelo"]}|{cor["limpa"]}')
                                               .replace('+', f'{cor["amarelo"]}+{cor["limpa"]}')
                                               .replace('-', f'{cor["ciano"]}-{cor["limpa"]}')
                                               .replace('a', f'{cor["branco"]}a{cor["limpa"]}')
                                               .replace('b', f'{cor["branco"]}b{cor["limpa"]}')
                                               .replace('c', f'{cor["branco"]}c{cor["limpa"]}')
                                               .replace('d', f'{cor["branco"]}d{cor["limpa"]}')
                                               .replace('ot', f'{cor["branco"]}ot{cor["limpa"]}')
                                               .replace('or', f'{cor["branco"]}or{cor["limpa"]}')
                                               .replace('n', f'{cor["branco"]}n{cor["limpa"]}')
                                               .replace('(', f'{cor["branco"]}({cor["limpa"]}')
                                               .replace(')', f'{cor["branco"]}){cor["limpa"]}'))
                            print(tabela_colorida)
                        elif escolha == 2 and tabela == 'd':
                            tabela_obj = ttg.Truths(['a', 'b', 'c', 'd'], [
                                                    f'{valor1} {funcao} (not {valor2})'], ascending=True)
                            tabela_str = str(tabela_obj).replace(
                                '1', 'V').replace('0', 'F')
                            tabela_colorida = (tabela_str
                                               .replace('F', f'{cor["vermelho"]}0{cor["limpa"]}')
                                               .replace('V', f'{cor["verde"]}1{cor["limpa"]}')
                                               .replace('|', f'{cor["amarelo"]}|{cor["limpa"]}')
                                               .replace('+', f'{cor["amarelo"]}+{cor["limpa"]}')
                                               .replace('-', f'{cor["ciano"]}-{cor["limpa"]}')
                                               .replace('a', f'{cor["branco"]}a{cor["limpa"]}')
                                               .replace('b', f'{cor["branco"]}b{cor["limpa"]}')
                                               .replace('c', f'{cor["branco"]}c{cor["limpa"]}')
                                               .replace('d', f'{cor["branco"]}d{cor["limpa"]}')
                                               .replace('ot', f'{cor["branco"]}ot{cor["limpa"]}')
                                               .replace('or', f'{cor["branco"]}or{cor["limpa"]}')
                                               .replace('n', f'{cor["branco"]}n{cor["limpa"]}')
                                               .replace('(', f'{cor["branco"]}({cor["limpa"]}')
                                               .replace(')', f'{cor["branco"]}){cor["limpa"]}'))
                            print(tabela_colorida)
                        elif escolha == 3 and tabela == 'd':
                            tabela_obj = ttg.Truths(['a', 'b', 'c', 'd'], [
                                                    f'not ({valor1} {funcao} {valor2})'], ascending=True)
                            tabela_str = str(tabela_obj).replace(
                                '1', 'V').replace('0', 'F')
                            tabela_colorida = (tabela_str
                                               .replace('F', f'{cor["vermelho"]}0{cor["limpa"]}')
                                               .replace('V', f'{cor["verde"]}1{cor["limpa"]}')
                                               .replace('|', f'{cor["amarelo"]}|{cor["limpa"]}')
                                               .replace('+', f'{cor["amarelo"]}+{cor["limpa"]}')
                                               .replace('-', f'{cor["ciano"]}-{cor["limpa"]}')
                                               .replace('a', f'{cor["branco"]}a{cor["limpa"]}')
                                               .replace('b', f'{cor["branco"]}b{cor["limpa"]}')
                                               .replace('c', f'{cor["branco"]}c{cor["limpa"]}')
                                               .replace('d', f'{cor["branco"]}d{cor["limpa"]}')
                                               .replace('ot', f'{cor["branco"]}ot{cor["limpa"]}')
                                               .replace('or', f'{cor["branco"]}or{cor["limpa"]}')
                                               .replace('n', f'{cor["branco"]}n{cor["limpa"]}')
                                               .replace('(', f'{cor["branco"]}({cor["limpa"]}')
                                               .replace(')', f'{cor["branco"]}){cor["limpa"]}'))
                            print(tabela_colorida)
                        else:
                            print(
                                f'{cor["vermelho"]}OPÇÃO {tabela} INVÁLIDA. TENTE NOVAMENTE.{cor["limpa"]}')

                    else:  # sem negação
                        if tabela == 'b':
                            tabela_obj = ttg.Truths(
                                ['a', 'b'], [f'{valor1} {funcao} {valor2}'], ascending=True)
                            tabela_str = str(tabela_obj).replace(
                                '1', 'V').replace('0', 'F')
                            tabela_colorida = (tabela_str
                                               .replace('F', f'{cor["vermelho"]}0{cor["limpa"]}')
                                               .replace('V', f'{cor["verde"]}1{cor["limpa"]}')
                                               .replace('|', f'{cor["amarelo"]}|{cor["limpa"]}')
                                               .replace('+', f'{cor["amarelo"]}+{cor["limpa"]}')
                                               .replace('-', f'{cor["ciano"]}-{cor["limpa"]}')
                                               .replace('a', f'{cor["branco"]}a{cor["limpa"]}')
                                               .replace('b', f'{cor["branco"]}b{cor["limpa"]}')
                                               .replace('or', f'{cor["branco"]}or{cor["limpa"]}')
                                               .replace('nd', f'{cor["branco"]}nd{cor["limpa"]}')
                                               .replace('(', f'{cor["branco"]}({cor["limpa"]}')
                                               .replace(')', f'{cor["branco"]}){cor["limpa"]}'))
                            print(tabela_colorida)
                        elif tabela == 'c':
                            tabela_obj = ttg.Truths(
                                ['a', 'b', 'c'], [f'{valor1} {funcao} {valor2}'], ascending=True)
                            tabela_str = str(tabela_obj).replace(
                                '1', 'V').replace('0', 'F')
                            tabela_colorida = (tabela_str
                                               .replace('F', f'{cor["vermelho"]}0{cor["limpa"]}')
                                               .replace('V', f'{cor["verde"]}1{cor["limpa"]}')
                                               .replace('|', f'{cor["amarelo"]}|{cor["limpa"]}')
                                               .replace('+', f'{cor["amarelo"]}+{cor["limpa"]}')
                                               .replace('-', f'{cor["ciano"]}-{cor["limpa"]}')
                                               .replace('a', f'{cor["branco"]}a{cor["limpa"]}')
                                               .replace('b', f'{cor["branco"]}b{cor["limpa"]}')
                                               .replace('c', f'{cor["branco"]}c{cor["limpa"]}')
                                               .replace('or', f'{cor["branco"]}or{cor["limpa"]}')
                                               .replace('nd', f'{cor["branco"]}nd{cor["limpa"]}')
                                               .replace('(', f'{cor["branco"]}({cor["limpa"]}')
                                               .replace(')', f'{cor["branco"]}){cor["limpa"]}'))
                            print(tabela_colorida)
                        elif tabela == 'd':
                            tabela_obj = ttg.Truths(['a', 'b', 'c', 'd'], [
                                                    f'{valor1} {funcao} {valor2}'], ascending=True)
                            tabela_str = str(tabela_obj).replace(
                                '1', 'V').replace('0', 'F')
                            tabela_colorida = (tabela_str
                                               .replace('F', f'{cor["vermelho"]}0{cor["limpa"]}')
                                               .replace('V', f'{cor["verde"]}1{cor["limpa"]}')
                                               .replace('|', f'{cor["amarelo"]}|{cor["limpa"]}')
                                               .replace('+', f'{cor["amarelo"]}+{cor["limpa"]}')
                                               .replace('-', f'{cor["ciano"]}-{cor["limpa"]}')
                                               .replace('a', f'{cor["branco"]}a{cor["limpa"]}')
                                               .replace('b', f'{cor["branco"]}b{cor["limpa"]}')
                                               .replace('c', f'{cor["branco"]}c{cor["limpa"]}')
                                               .replace('d', f'{cor["branco"]}d{cor["limpa"]}')
                                               .replace('or', f'{cor["branco"]}or{cor["limpa"]}')
                                               .replace('n', f'{cor["branco"]}n{cor["limpa"]}')
                                               .replace('(', f'{cor["branco"]}({cor["limpa"]}')
                                               .replace(')', f'{cor["branco"]}){cor["limpa"]}'))
                            print(tabela_colorida)
                        else:
                            print(
                                f'{cor["vermelho"]}OPÇÃO {tabela} INVÁLIDA. TENTE NOVAMENTE.{cor["limpa"]}')

                else:
                    print(
                        f'{cor["vermelho"]}OPÇÃO {funcao} INVÁLIDA. TENTE NOVAMENTE.{cor["limpa"]}')

                    continuar = input(
                        f'{cor["amarelo"]}Deseja calcular outra expressão booleana? (S/N): {cor["limpa"]}').upper().strip()
                    if continuar != 'S':
                        print(
                            f'{cor["ciano"]}Saindo das expressões booleanas...{cor["limpa"]}')
                        break
            else:
                print(
                    f'{cor["vermelho"]}VALOR INVALIDO! COLOQUE LETRAS DE{cor["limpa"]} '
                    f'{cor["branco"]}A ATÉ D.{cor["limpa"]}'
                )
if escolhido != 0:
    print()
print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
print(f'{cor["verde"]}{'── FIM DO PROGRAMA ──────────────────────────':^25}{cor["limpa"]}')
