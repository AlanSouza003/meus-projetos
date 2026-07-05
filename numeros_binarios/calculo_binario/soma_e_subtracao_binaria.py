from funcoes.funcoes import limpatela, perguntar_continuar
from time import sleep

def colorir_binario(valor_str, cor):
    manipulado = valor_str.replace("1", "V").replace("0", "F")
    return manipulado.replace(
        "F", f'{cor["vermelho"]}0{cor["limpa"]}'
    ).replace("V", f'{cor["verde"]}1{cor["limpa"]}')

def calculos_binarios(cor, data_formatada):
    titulo = "SOMANDO NÚMEROS"
    titulo2 = "BINÁRIOS"
    
    while True:
        limpatela()
        print(data_formatada)
        print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
        print(f'{cor["ciano"]}{titulo:^25}\n{titulo2:^25}{cor["limpa"]}')
        print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
        print(f'{cor["amarelo"]}ESCOLHA UMA DAS OPÇÕES ABAIXO:{cor["limpa"]}')
        print(f'{cor["verde"]}[ 1 ]{cor["limpa"]} {cor["branco"]}ADIÇÃO{cor["limpa"]}')
        print(f'{cor["verde"]}[ 2 ]{cor["limpa"]} {cor["branco"]}SUBTRAÇÃO{cor["limpa"]}')
        print(f'{cor["vermelho"]}[ 0 ]{cor["limpa"]} {cor["branco"]}VOLTAR AO MENU PRINCIPAL{cor["limpa"]}')
        print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
        escolha_str = input(f'{cor["roxo"]}DIGITE A OPÇÃO: {cor["limpa"]}').strip()
        print(f'{cor["branco"]}─{cor["limpa"]}' * 25)

        if not escolha_str.isdigit() or escolha_str not in ["1", "2", "0"]:
            
            print(f'{cor["vermelho"]}OPÇÃO INVÁLIDA! TENTE NOVAMENTE.{cor["limpa"]}')
            print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
            input(f'{cor["branco"]}PRESSIONE ENTER PARA CONTINUAR...{cor["limpa"]}')
            continue
            
        limpatela()

        escolha = int(escolha_str)

        if escolha == 0:
            break

        elif escolha == 1:
            somar_binarios(cor, data_formatada)
        elif escolha == 2:
            subtrair_binarios(cor, data_formatada)

def somar_binarios(cor, data_formatada):
    while True:
        limpatela()
        print(data_formatada)
        print()
        while True:
            print(f'{cor["amarelo"]}QUANTAS PARCELAS DESEJA:{cor["limpa"]}')
            print(f'{cor["branco"]}DIGITE{cor["limpa"]} {cor["verde"]}[1]{cor["limpa"]} '
                  f'{cor["branco"]}PARA DUAS PARCELAS{cor["limpa"]}')
            print(f'{cor["branco"]}DIGITE{cor["limpa"]} {cor["verde"]}[2]{cor["limpa"]} '
                  f'{cor["branco"]}PARA TRÊS PARCELAS{cor["limpa"]}')
            print(f'{cor["branco"]}DIGITE{cor["limpa"]} {cor["verde"]}[3]{cor["limpa"]} '
                  f'{cor["branco"]}PARA QUATRO PARCELAS{cor["limpa"]}')
            print(f'{cor["branco"]}DIGITE{cor["limpa"]} {cor["vermelho"]}[0]{cor["limpa"]} '
                  f'{cor["branco"]}PARA VOLTAR AO MENU ANTERIOR{cor["limpa"]}')
            print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
            num_str = input(f'{cor["roxo"]}DIGITE AQUI: {cor["limpa"]}').strip()
            print(f'{cor["branco"]}─{cor["limpa"]}' * 25)

            if not num_str.isdigit():
                print(f'{cor["vermelho"]}OPÇÃO INVÁLIDA! DIGITE SOMENTE NÚMEROS.{cor["limpa"]}')
                input(f'{cor["branco"]}PRESSIONE ENTER PARA CONTINUAR...{cor["limpa"]}')
                print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                limpatela()
                print(data_formatada)
                print()
                continue

            num = int(num_str)

            if 0 <= num <= 3:
                break
            else:
                print(f'{cor["vermelho"]}OPÇÃO INVÁLIDA! DIGITE OS VALORES DE 1 ATÉ 3\n{cor["limpa"]}'
                      f'{cor["vermelho"]}OU 0 PARA RETONAR AO MENU ANTERIOR.{cor["limpa"]}')
                print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                input(f'{cor["branco"]}PRESSIONE ENTER PARA CONTINUAR...{cor["limpa"]}')
                limpatela()
                print(data_formatada)
                print()
                continue

        total_parcelas = num + 1 
        if num == 0:
            return
        if 1 <= num <= 3:
            while True:
                limpatela()
                print(data_formatada)
                print()
                print(f'{cor["verde"]}CERTO. VAMOS REALIZAR A OPERAÇÃO.{cor["limpa"]}')
                print(f'{cor["branco"]}─{cor["limpa"]}' * 25)

                parcelas_str = []
                nomes = ["Primeira", "Segunda", "Terceira", "Quarta"]
                for i in range(total_parcelas):
                    valor = input(f'{cor["branco"]}{nomes[i]} Parcela: {cor["limpa"]}')
                    parcelas_str.append(valor)

                # valida todas as parcelas
                if all(all(c in "01" for c in p) and len(p) > 0 for p in parcelas_str):
                    valores_dec = [int(p, 2) for p in parcelas_str]
                    resultado_dec = sum(valores_dec)
                    resultado_bin = bin(resultado_dec)[2:]

                    parcelas_coloridas = [colorir_binario(p, cor) for p in parcelas_str]
                    resultado_colorido = colorir_binario(resultado_bin, cor)

                    print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                    for c in range(4):
                        print(f'\r\033[1;95m{"PROCESSANDO" + "." * c:^25}\033[0m', end="", flush=True)
                        sleep(1.5)
                    print()
                    print(f'{cor["branco"]}─{cor["limpa"]}' * 25)

                    print(f'{cor["verde"]}RESULTADO{cor["limpa"]}')
                    soma_str = f' {cor["branco"]}+{cor["limpa"]} '.join(parcelas_coloridas)
                    print(f'{cor["branco"]}A soma entre{cor["limpa"]} {soma_str} {cor["branco"]}é ={cor["limpa"]} {resultado_colorido}')
                    print(f'{cor["branco"]}─{cor["limpa"]}' * 25)

                    if not perguntar_continuar(cor, data_formatada, "DESEJA REALIZAR OUTRA SOMA?", "SAINDO DO CALCULO"):
                        break
                else:
                    print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                    print(
                        f'{cor["vermelho"]}OPERAÇÃO INVÁLIDA! UTILIZE APENAS: {cor["limpa"]}'
                        f'{cor["verde"]}1s{cor["limpa"]} {cor["branco"]}E{cor["limpa"]} {cor["vermelho"]}0s{cor["limpa"]}.'
                    )
                    print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                    input(f'{cor["branco"]}PRESSIONE ENTER PARA CONTINUAR...{cor["limpa"]}')
                    continue
        limpatela()
        print(data_formatada)
        if not perguntar_continuar(cor, data_formatada, "DESEJA MUDAR A QUANTIDADE DE PARCELAS?", 
                                    "SAINDO DO CALCULO DE ADIÇÃO BINÁRIA"):
            break

def subtrair_binarios(cor, data_formatada):
    while True:
        limpatela()
        print(data_formatada)
        print()
        while True:
            print(f'{cor["amarelo"]}QUANTAS PARCELAS DESEJA:{cor["limpa"]}')
            print(f'{cor["branco"]}DIGITE{cor["limpa"]} {cor["verde"]}[1]{cor["limpa"]} '
                  f'{cor["branco"]}PARA DUAS PARCELAS{cor["limpa"]}')
            print(f'{cor["branco"]}DIGITE{cor["limpa"]} {cor["verde"]}[2]{cor["limpa"]} '
                  f'{cor["branco"]}PARA TRÊS PARCELAS{cor["limpa"]}')
            print(f'{cor["branco"]}DIGITE{cor["limpa"]} {cor["verde"]}[3]{cor["limpa"]} '
                  f'{cor["branco"]}PARA QUATRO PARCELAS{cor["limpa"]}')
            print(f'{cor["branco"]}DIGITE{cor["limpa"]} {cor["vermelho"]}[0]{cor["limpa"]} '
                  f'{cor["branco"]}PARA VOLTAR AO MENU ANTERIOR{cor["limpa"]}')
            print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
            num_str = input(f'{cor["roxo"]}DIGITE AQUI: {cor["limpa"]}').strip()
            print(f'{cor["branco"]}─{cor["limpa"]}' * 25)

            if not num_str.isdigit():
                print(f'{cor["vermelho"]}OPÇÃO INVÁLIDA! DIGITE SOMENTE NÚMEROS.{cor["limpa"]}')
                input(f'{cor["branco"]}PRESSIONE ENTER PARA CONTINUAR...{cor["limpa"]}')
                limpatela()
                print(data_formatada)
                print()
                continue

            num = int(num_str)
            if 0 <= num <= 3:
                break
            else:
                print(f'{cor["vermelho"]}OPÇÃO INVÁLIDA! DIGITE OS VALORES DE 1 ATÉ 3\n{cor["limpa"]}'
                      f'{cor["vermelho"]}OU 0 PARA RETORNAR AO MENU ANTERIOR.{cor["limpa"]}')
                print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                input(f'{cor["branco"]}PRESSIONE ENTER PARA CONTINUAR...{cor["limpa"]}')
                limpatela()
                print(data_formatada)
                print()
                continue

        total_parcelas = num + 1
        if num == 0:
            return
        if 1 <= num <= 3:
            while True:
                limpatela()
                print(data_formatada)
                print()
                print(f'{cor["verde"]}CERTO. VAMOS REALIZAR A OPERAÇÃO.{cor["limpa"]}')
                print(f'{cor["branco"]}─{cor["limpa"]}' * 25)

                parcelas_str = []
                nomes = ["Primeira", "Segunda", "Terceira", "Quarta"]
                for i in range(total_parcelas):
                    valor = input(f'{cor["branco"]}{nomes[i]} Parcela: {cor["limpa"]}')
                    parcelas_str.append(valor)

                if all(all(c in "01" for c in p) and len(p) > 0 for p in parcelas_str):
                    valores_dec = [int(p, 2) for p in parcelas_str]
                    resultado_dec = valores_dec[0]
                    for v in valores_dec[1:]:
                        resultado_dec -= v

                    resultado_bin = bin(resultado_dec)

                    parcelas_coloridas = [colorir_binario(p, cor) for p in parcelas_str]

                    if resultado_dec < 0:
                        result_format = resultado_bin[0] + resultado_bin[3:]
                        result_str = str(result_format).replace("1", "V").replace("0", "F")
                        resultado_colorido = (
                            result_str
                            .replace("-", f'{cor["vermelho"]}-{cor["limpa"]}')
                            .replace("F", f'{cor["vermelho"]}0{cor["limpa"]}')
                            .replace("V", f'{cor["verde"]}1{cor["limpa"]}')
                        )
                    else:
                        resultado_colorido = colorir_binario(resultado_bin[2:], cor)

                    print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                    for c in range(4):
                        print(f'\r\033[1;95m{"PROCESSANDO" + "." * c:^25}\033[0m', end="", flush=True)
                        sleep(1.5)
                    print()
                    print(f'{cor["branco"]}─{cor["limpa"]}' * 25)

                    print(f'{cor["verde"]}RESULTADO{cor["limpa"]}')
                    subtracao_str = f' {cor["branco"]}-{cor["limpa"]} '.join(parcelas_coloridas)
                    print(f'{cor["branco"]}A subtração entre{cor["limpa"]} {subtracao_str} '
                          f'{cor["branco"]}é ={cor["limpa"]} {resultado_colorido}')
                    print(f'{cor["branco"]}─{cor["limpa"]}' * 25)

                    if not perguntar_continuar(cor, data_formatada, "DESEJA REALIZAR OUTRA SUBTRAÇÃO?", "SAINDO DO CALCULO"):
                        break
                else:
                    print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                    print(
                        f'{cor["vermelho"]}OPERAÇÃO INVÁLIDA! UTILIZE APENAS: {cor["limpa"]}'
                        f'{cor["verde"]}1s{cor["limpa"]} {cor["branco"]}E{cor["limpa"]} {cor["vermelho"]}0s{cor["limpa"]}.'
                    )
                    print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                    input(f'{cor["branco"]}PRESSIONE ENTER PARA CONTINUAR...{cor["limpa"]}')
                    continue
        limpatela()
        print(data_formatada)
        if not perguntar_continuar(cor, data_formatada, "DESEJA MUDAR A QUANTIDADE DE PARCELAS?", 
                                "SAINDO DO CALCULO DE SUBTRAÇÃO BINÁRIA"):
            break