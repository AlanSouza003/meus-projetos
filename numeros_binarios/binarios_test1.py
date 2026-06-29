try:
    from imports import *
    # TODO: CORES
    cor = paleta_cor()

    # TODO: DATA DE EXIBIÇÃO
    data_formatada = data_atual(cor)

    # TODO: MENUS DO SISTEMA
    titulo = f'{cor["ciano"]}{"NÚMEROS BINÁRIOS":^25}{cor["limpa"]}'
    menu_principal = (  # * Menu principal do programa.
        f'{cor["amarelo"]}ESCOLHA A OPÇÃO DESEJADA:{cor["limpa"]}\n'
        f'{cor["verde"]}[ 1 ]{cor["limpa"]} {cor["verde"]}CONVERSÃO{cor["limpa"]}\n'
        f'{cor["verde"]}[ 2 ]{cor["limpa"]} {cor["roxo"]}OPERAÇÕES BINÁRIAS{cor["limpa"]}\n'
        f'{cor["verde"]}[ 3 ]{cor["limpa"]} {cor["azul"]}TABELA VERDADE{cor["limpa"]}\n'
        f'{cor["verde"]}[ 4 ]{cor["limpa"]} {cor["amarelo"]}EXPRESSÕES BOOLEANAS{cor["limpa"]}\n'
        f'{cor["vermelho"]}[ 0 ]{cor["limpa"]} {cor["vermelho"]}ENCERRAR O PROGRAMA{cor["limpa"]}'
    )
    titulo_conversões = (  # * Subtítulo para a opção de conversão.
        f'{cor["branco"]}┌─────────────────────┐{cor["limpa"]}\n'
        f'{cor["ciano"]}│      CONVERSÕES    │{cor["limpa"]}\n'
        f'{cor["branco"]}└─────────────────────┘{cor["limpa"]}'
    )
    menu_conversões = (  # * Submenu para a opção de conversão disponíveis.
        f'{cor["verde"]}[ 1 ]{cor["limpa"]} {cor["amarelo"]}DECIMAL{cor["limpa"]}\n'
        f'{cor["verde"]}[ 2 ]{cor["limpa"]} {cor["verde"]}BINÁRIO{cor["limpa"]}\n'
        f'{cor["verde"]}[ 3 ]{cor["limpa"]} {cor["azul"]}OCTAL{cor["limpa"]}\n'
        f'{cor["verde"]}[ 4 ]{cor["limpa"]} {cor["roxo"]}HEXDECIMAL{cor["limpa"]}\n'
        f'{cor["vermelho"]}[ 0 ]{cor["limpa"]} {cor["vermelho"]}MENU PRINCIPAL{cor["limpa"]}'
    )
    titulo_decimais = (  # * Título para a opção de conversão decimal para binário.
        f'{cor["branco"]}╔══════════════════════╗{cor["limpa"]}\n'
        f'{cor["ciano"]}║   NÚMEROS DECIMAIS  ║{cor["limpa"]}\n'
        f'{cor["branco"]}╚══════════════════════╝{cor["limpa"]}'
    )
    menu_decimais = (  # * Menu para a opção de conversões de decimais.
        f'{cor["verde"]}[ 1 ]{cor["limpa"]} {cor["verde"]}BINÁRIO{cor["limpa"]}\n'
        f'{cor["verde"]}[ 2 ]{cor["limpa"]} {cor["azul"]}OCTAL{cor["limpa"]}\n'
        f'{cor["verde"]}[ 3 ]{cor["limpa"]} {cor["roxo"]}HEXADECIMAL{cor["limpa"]}\n'
        f'{cor["vermelho"]}[ 0 ]{cor["limpa"]} {cor["vermelho"]}MENU ANTERIOR{cor["limpa"]}'
    )
    titulo_binarios = (  # * Título para a opção de conversão binária.
        f'{cor["branco"]}╔══════════════════════╗{cor["limpa"]}\n'
        f'{cor["ciano"]}║   NÚMEROS BINÁRIOS  ║{cor["limpa"]}\n'
        f'{cor["branco"]}╚══════════════════════╝{cor["limpa"]}'
    )
    menu_binarios = (  # * Menu para a opção de conversões de binários.
        f'{cor["verde"]}[ 1 ]{cor["limpa"]} {cor["verde"]}DECIMAL{cor["limpa"]}\n'
        f'{cor["verde"]}[ 2 ]{cor["limpa"]} {cor["azul"]}OCTAL{cor["limpa"]}\n'
        f'{cor["verde"]}[ 3 ]{cor["limpa"]} {cor["roxo"]}HEXADECIMAL{cor["limpa"]}\n'
        f'{cor["vermelho"]}[ 0 ]{cor["limpa"]} {cor["vermelho"]}MENU ANTERIOR{cor["limpa"]}'
    )
    titulo_octal = (  # * Título para a opção de conversão octal.
        f'{cor["branco"]}╔═══════════════════╗{cor["limpa"]}\n'
        f'{cor["ciano"]}║   NÚMEROS OCTAL  ║{cor["limpa"]}\n'
        f'{cor["branco"]}╚═══════════════════╝{cor["limpa"]}'
    )
    menu_octal = (  # * Menu para a opção de conversões de octal.
        f'{cor["verde"]}[ 1 ]{cor["limpa"]} {cor["verde"]}DECIMAL{cor["limpa"]}\n'
        f'{cor["verde"]}[ 2 ]{cor["limpa"]} {cor["azul"]}BINÁRIO{cor["limpa"]}\n'
        f'{cor["verde"]}[ 3 ]{cor["limpa"]} {cor["roxo"]}HEXADECIMAL{cor["limpa"]}\n'
        f'{cor["vermelho"]}[ 0 ]{cor["limpa"]} {cor["vermelho"]}MENU ANTERIOR{cor["limpa"]}'
    )
    titulo_hexadecimal = (  # * Título para a opção de conversão hexadecimal.
        f'{cor["branco"]}╔═════════════════════════╗{cor["limpa"]}\n'
        f'{cor["ciano"]}║   NÚMEROS HEXADECIMAL  ║{cor["limpa"]}\n'
        f'{cor["branco"]}╚═════════════════════════╝{cor["limpa"]}'
    )
    menu_hexadecimal = (  # * Menu para a opção de conversões de hexadecimal.
        f'{cor["verde"]}[ 1 ]{cor["limpa"]} {cor["amarelo"]}DECIMAL{cor["limpa"]}\n'
        f'{cor["verde"]}[ 2 ]{cor["limpa"]} {cor["verde"]}BINÁRIO{cor["limpa"]}\n'
        f'{cor["verde"]}[ 3 ]{cor["limpa"]} {cor["azul"]}OCTAL{cor["limpa"]}\n'
        f'{cor["vermelho"]}[ 0 ]{cor["limpa"]} {cor["vermelho"]}MENU ANTERIOR{cor["limpa"]}'
    )
    # TODO: Variaveis de controle
    escolhido = 0
    escolhido_str = ""
    opcao = 0
    while True:  # ! AJUSTANDO A LOGICA DO LOOP.
        while True:  # * Loop para validar a entrada do menu principal
            if escolhido_str != "0":
                limpatela()
            print(data_formatada)
            print(f'{cor["branco"]}-={cor["limpa"]}' * 12)
            print(titulo)
            print(f'{cor["branco"]}-={cor["limpa"]}' * 12)
            print(menu_principal)
            print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
            escolhido_str = str(
                input(
                    f'{cor["roxo"]}DIGITE O NÚMERO DA SUA OPÇÃO '
                    f'[DIGITE 0 PARA SAIR]: {cor["limpa"]}'
                )
            ).strip()
            if escolhido_str != "0":
                print()
            if escolhido_str.isdigit():
                escolhido = int(escolhido_str)
                if escolhido == 0 or 1 <= escolhido <= 4:
                    break
                else:
                    print(
                        f'{cor["vermelho"]}❌ ENTRADA INVÁLIDA!\n{cor["limpa"]}'
                        f'{cor["branco"]}DIGITE{cor["limpa"]} {cor["verde"]}[1-4]{cor["limpa"]} '
                        f'{cor["branco"]}ou{cor["limpa"]} '
                        f'{cor["vermelho"]}[0]{cor["limpa"]} {cor["branco"]}PARA SAIR.{cor["limpa"]}'
                    )
                    print()
                    input(f'{cor["branco"]}PRESSIONE ENTER PARA CONTINUAR...{cor["limpa"]}')
                    continue
            elif escolhido_str.isalpha():
                print(
                    f'{cor["vermelho"]}❌ ENTRADA INVÁLIDA!\n{cor["limpa"]}'
                    f'{cor["amarelo"]}UTILIZE NÚMEROS.{cor["limpa"]}'
                )
                print()
                input(f'{cor["branco"]}PRESSIONE ENTER PARA CONTINUAR...{cor["limpa"]}')
                continue
            else:
                print(
                    f'{cor["vermelho"]}❌ ENTRADA INVÁLIDA!{cor["limpa"]}\n'
                    f'{cor["amarelo"]}UTILIZE APENAS NÚMEROS.{cor["limpa"]}'
                )
                print()
                input(f'{cor["branco"]}PRESSIONE ENTER PARA CONTINUAR...{cor["limpa"]}')
                continue  # * Fim do loop de validação do menu principal
        if escolhido == 0:  # * Opção para encerrar o programa
            break

        if escolhido == 1:  # * Opção para acessar o menu de conversões
            # TODO: Variaveis de Controle para os submenus
            op_decimais = None
            op_binario = None
            op_octal = None
            op_hexadecimal = None
            while True:  # * Loop menu de conversões
                limpatela()
                print(data_formatada)
                print(titulo_conversões)
                print(menu_conversões)
                print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                opcao_str = str(
                    input(
                        f'{cor["roxo"]}DIGITE SUA OPÇÃO '
                        f'[DIGITE 0 PARA VOLTAR]: {cor["limpa"]}'
                    )
                ).strip()
                print()

                if not opcao_str.isdigit():  # * Letras ou caracteres especiais
                    print(
                        f'{cor["vermelho"]}❌ ENTRADA INVÁLIDA!\n{cor["limpa"]}'
                        f'{cor["amarelo"]}UTILIZE APENAS NÚMEROS.{cor["limpa"]}'
                    )
                    print()
                    input(f'{cor["branco"]}PRESSIONE ENTER PARA CONTINUAR...{cor["limpa"]}')
                    continue

                opcao = int(opcao_str)

                if opcao == 0:
                    break  # * Volta ao menu anterior

                elif opcao == 1:  # * Opção para acessar o menu de conversões decimais
                    while True:  # * Loop menu decimais
                        limpatela()
                        print(data_formatada)
                        print(titulo_decimais)
                        print(menu_decimais)
                        print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                        op_decimais_str = str(
                            input(
                                f'{cor["branco"]}Digite sua opção '
                                f'[DIGITE 0 PARA O MENU ANTERIOR]: {cor["limpa"]}'
                            )
                        ).strip()
                        print()

                        if not op_decimais_str.isdigit():
                            print(
                                f'{cor["vermelho"]}❌ ENTRADA INVÁLIDA!\n{cor["limpa"]}'
                                f'{cor["amarelo"]}UTILIZE APENAS NÚMEROS.{cor["limpa"]}'
                            )
                            print()
                            input(
                                f'{cor["branco"]}PRESSIONE ENTER PARA CONTINUAR...{cor["limpa"]}'
                            )
                            continue

                        op_decimais = int(op_decimais_str)
                        if op_decimais == 0 or 1 <= op_decimais <= 3:
                            break  # * Volta ao menu de conversões ou continua para a conversão escolhida

                        else:
                            print(
                                f'{cor["vermelho"]}❌ ENTRADA INVÁLIDA!\n{cor["limpa"]}'
                                f'{cor["branco"]}DIGITE{cor["limpa"]} {cor["verde"]}[1-3]{cor["limpa"]} '
                                f'{cor["branco"]}ou{cor["limpa"]} '
                                f'{cor["vermelho"]}[0]{cor["limpa"]} {cor["branco"]}PARA VOLTAR.{cor["limpa"]}'
                            )
                            print()
                            input(
                                f'{cor["branco"]}PRESSIONE ENTER PARA CONTINUAR...{cor["limpa"]}'
                            )
                            continue

                elif opcao == 2:  # * Opção para acessar o menu de conversões binários
                    while True:  # * Loop menu Binario
                        limpatela()
                        print(data_formatada)
                        print(titulo_binarios)
                        print(menu_binarios)
                        print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                        op_binario_str = str(
                            input(
                                f'{cor["branco"]}Digite sua opção '
                                f'[DIGITE 0 PARA O MENU ANTERIOR]: {cor["limpa"]}'
                            )
                        ).strip()
                        print()

                        if not op_binario_str.isdigit():
                            print(
                                f'{cor["vermelho"]}❌ ENTRADA INVÁLIDA!\n{cor["limpa"]}'
                                f'{cor["amarelo"]}UTILIZE APENAS NÚMEROS.{cor["limpa"]}'
                            )
                            print()
                            input(
                                f'{cor["branco"]}PRESSIONE ENTER PARA CONTINUAR...{cor["limpa"]}'
                            )
                            continue

                        op_binario = int(op_binario_str)

                        if op_binario == 0 or 1 <= op_binario <= 3:
                            break  # * Volta ao menu de conversões ou continua para a conversão escolhida

                        else:
                            print(
                                f'{cor["vermelho"]}❌ ENTRADA INVÁLIDA!\n{cor["limpa"]}'
                                f'{cor["branco"]}DIGITE{cor["limpa"]} {cor["verde"]}[1-3]{cor["limpa"]} '
                                f'{cor["branco"]}ou{cor["limpa"]} '
                                f'{cor["vermelho"]}[0]{cor["limpa"]} {cor["branco"]}PARA VOLTAR.{cor["limpa"]}'
                            )
                            print()
                            input(
                                f'{cor["branco"]}PRESSIONE ENTER PARA CONTINUAR...{cor["limpa"]}'
                            )
                            continue  # * Fim do loop menu de binarios

                elif opcao == 3:  # * Opção para acessar o menu de conversões octal
                    while True:  # * Loop menu Octal
                        limpatela()
                        print(data_formatada)
                        print(titulo_octal)
                        print(menu_octal)
                        print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                        op_octal_str = str(
                            input(
                                f'{cor["branco"]}Digite sua opção '
                                f'[DIGITE 0 PARA O MENU ANTERIOR]: {cor["limpa"]}'
                            )
                        ).strip()
                        print()

                        if not op_octal_str.isdigit():
                            print(
                                f'{cor["vermelho"]}❌ ENTRADA INVÁLIDA!\n{cor["limpa"]}'
                                f'{cor["amarelo"]}UTILIZE APENAS NÚMEROS.{cor["limpa"]}'
                            )
                            print()
                            input(
                                f'{cor["branco"]}PRESSIONE ENTER PARA CONTINUAR...{cor["limpa"]}'
                            )
                            continue

                        op_octal = int(op_octal_str)

                        if op_octal == 0 or 1 <= op_octal <= 3:
                            break  # * Volta ao menu de conversões ou continua para a conversão escolhida

                        else:
                            print(
                                f'{cor["vermelho"]}❌ ENTRADA INVÁLIDA!\n{cor["limpa"]}'
                                f'{cor["branco"]}DIGITE{cor["limpa"]} {cor["verde"]}[1-3]{cor["limpa"]} '
                                f'{cor["branco"]}ou{cor["limpa"]} '
                                f'{cor["vermelho"]}[0]{cor["limpa"]} {cor["branco"]}PARA VOLTAR.{cor["limpa"]}'
                            )
                            print()
                            input(
                                f'{cor["branco"]}PRESSIONE ENTER PARA CONTINUAR...{cor["limpa"]}'
                            )
                            continue  # * Fim do loop menu de octal

                elif opcao == 4:  # * Opção para acessar o menu de conversões hexadecimal
                    while True:  # * Loop menu Hexadecimal
                        limpatela()
                        print(data_formatada)
                        print(titulo_hexadecimal)
                        print(menu_hexadecimal)
                        print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                        op_hexadecimal_str = str(
                            input(
                                f'{cor["branco"]}Digite sua opção '
                                f'[DIGITE 0 PARA O MENU ANTERIOR]: {cor["limpa"]}'
                            )
                        ).strip()
                        print()

                        if not op_hexadecimal_str.isdigit():
                            print(
                                f'{cor["vermelho"]}❌ ENTRADA INVÁLIDA!\n{cor["limpa"]}'
                                f'{cor["amarelo"]}UTILIZE APENAS NÚMEROS.{cor["limpa"]}'
                            )
                            print()
                            input(
                                f'{cor["branco"]}PRESSIONE ENTER PARA CONTINUAR...{cor["limpa"]}'
                            )
                            continue

                        op_hexadecimal = int(op_hexadecimal_str)

                        if op_hexadecimal == 0 or 1 <= op_hexadecimal <= 3:
                            break  # * Volta ao menu de conversões ou continua para a conversão escolhida

                else:
                    print(
                        f'{cor["vermelho"]}❌ ENTRADA INVÁLIDA!\n{cor["limpa"]}'
                        f'{cor["branco"]}DIGITE{cor["limpa"]} {cor["verde"]}[1-4]{cor["limpa"]} '
                        f'{cor["branco"]}ou{cor["limpa"]} '
                        f'{cor["vermelho"]}[0]{cor["limpa"]} {cor["branco"]}PARA VOLTAR.{cor["limpa"]}'
                    )
                    print()
                    input(f'{cor["branco"]}PRESSIONE ENTER PARA CONTINUAR...{cor["limpa"]}')
                    continue  # * Fim do loop menu de conversões

                if op_decimais == 1:  # * Opção para conversão decimal para binário
                    converter_de_decimal_binario(cor, data_formatada)

                elif op_decimais == 2:  # * Opção para conversão decimal para octal
                    converter_de_decimal_octal(cor, data_formatada)

                elif op_decimais == 3:  # * Opção para conversão decimal para hexadecimal
                    converter_de_decimal_hexadecimal(cor, data_formatada)

                if op_binario == 1:  # * Opção para conversão binário para decimal
                    converter_binario_para_decimal(cor, data_formatada)

                elif op_binario == 2:  # * Opção para conversão binário para octal
                    converter_binario_para_octal(cor, data_formatada)

                elif op_binario == 3:  # * Opção para conversão binário para hexadecimal
                    converter_binario_para_hexadecimal(cor, data_formatada)

                if op_octal == 1:  # * Opção para conversão octal para decimal
                    converter_de_octal_para_decimal(cor, data_formatada)

                elif op_octal == 2:  # * Opção para conversão octal para binário
                    converter_octal_para_binario(cor, data_formatada)

                elif op_octal == 3:  # * Opção para conversão octal para hexadecimal
                    converter_octal_para_hexadecimal(cor, data_formatada)
 
                if op_hexadecimal == 1:
                    converter_hexadecimal_para_decimal(cor, data_formatada)
                elif op_hexadecimal == 2:  # * Opção para conversão de hexadecimal para binário
                    converter_hexadecimal_para_binario(cor, data_formatada)

                elif op_hexadecimal == 3: # * Opção para conversão de hexadecimal para octal
                    converter_hexadecimal_para_octal(cor, data_formatada)
                
                elif escolhido == 3:  # ? * Ajustar para concatenar com o loop do menu principal, e outros detalhes
                    titulo = "SOMANDO NÚMEROS"
                    titulo2 = "BINÁRIOS"
                    print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                    print(f'{cor["ciano"]}{titulo:^25}\n' f'{titulo2:^25}{cor["limpa"]}')
                    print(f'{cor["branco"]}─{cor["limpa"]}' * 25)

                    while True:
                        print(
                            f'{cor["amarelo"]}ESCOLHA UMA DAS OPÇÕES ABAIXO:{cor["limpa"]}'
                        )
                        print(
                            f'{cor["verde"]}[ 1 ]{cor["limpa"]} {cor["branco"]}ADIÇÃO{cor["limpa"]}'
                        )
                        print(
                            f'{cor["verde"]}[ 2 ]{cor["limpa"]} {cor["branco"]}SUBTRAÇÃO{cor["limpa"]}'
                        )
                        print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                        escolha_str = str(
                            input(f'{cor["roxo"]}DIGITE A OPÇÃO: {cor["limpa"]}')
                        ).strip()
                        print(f'{cor["branco"]}─{cor["limpa"]}' * 25)

                        if escolha_str not in ["1", "2"]:
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
                                f'{cor["branco"]}DIGITE{cor["limpa"]} {cor["verde"]}[1]{cor["limpa"]} {cor["branco"]}PARA DUAS PARCELAS{cor["limpa"]}'
                            )
                            print(
                                f'{cor["branco"]}DIGITE{cor["limpa"]} {cor["verde"]}[2]{cor["limpa"]} {cor["branco"]}PARA TRÊS PARCELAS{cor["limpa"]}'
                            )
                            print(
                                f'{cor["branco"]}DIGITE{cor["limpa"]} {cor["verde"]}[3]{cor["limpa"]} {cor["branco"]}PARA QUATRO PARCELAS{cor["limpa"]}'
                            )
                            print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                            num_str = str(
                                input(f'{cor["roxo"]}DIGITE AQUI: {cor["limpa"]}')
                            )
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
                                f'{cor["verde"]}CERTO. VAMOS REALIZAR A OPERAÇÃO.{cor["limpa"]}'
                            )
                            print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                            while True:
                                n1_str = str(
                                    input(
                                        f'{cor["branco"]}Primeira Parcela: {cor["limpa"]}'
                                    )
                                )
                                n2_str = str(
                                    input(f'{cor["branco"]}Segunda Parcela: {cor["limpa"]}')
                                )
                                if all(c in "01" for c in n1_str) and all(
                                    c in "01" for c in n2_str
                                ):
                                    n1_dec = int(n1_str, 2)
                                    n2_dec = int(n2_str, 2)
                                    somar_dec = n1_dec + n2_dec
                                    result_bin = bin(somar_dec)
                                    result_str = (
                                        str(result_bin[2:])
                                        .replace("1", "V")
                                        .replace("0", "F")
                                    )
                                    n1_c = n1_str.replace("1", "V").replace("0", "F")
                                    n2_c = n2_str.replace("1", "V").replace("0", "F")
                                    n1_colorido = n1_c.replace(
                                        "F", f'{cor["vermelho"]}0{cor["limpa"]}'
                                    ).replace("V", f'{cor["verde"]}1{cor["limpa"]}')
                                    n2_colorido = n2_c.replace(
                                        "F", f'{cor["vermelho"]}0{cor["limpa"]}'
                                    ).replace("V", f'{cor["verde"]}1{cor["limpa"]}')
                                    result_colorido = result_str.replace(
                                        "F", f'{cor["vermelho"]}0{cor["limpa"]}'
                                    ).replace("V", f'{cor["verde"]}1{cor["limpa"]}')
                                    print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                                    for c in range(4):
                                        ponto = f"." * c
                                        print(
                                            f'\r\033[1;95m{"PROCESSANDO" + ponto:^25}\033[0m',
                                            end="",
                                            flush=True,
                                        )
                                        sleep(1.5)
                                    print()
                                    print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                                    print(f'{cor["verde"]}RESULTADO{cor["limpa"]}')
                                    print(
                                        f'{cor["branco"]}A soma entre{cor["limpa"]} {n1_colorido} {cor["branco"]}+{cor["limpa"]} '
                                        f'{n2_colorido} {cor["branco"]}é ={cor["limpa"]} {result_colorido}'
                                    )
                                    continuar = ""
                                    while True:
                                        continuar = (
                                            input(
                                                f'{cor["amarelo"]}Deseja converter outro valor? (S/N): {cor["limpa"]}'
                                            )
                                            .upper()
                                            .strip()
                                        )
                                        print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                                        if continuar in ["S", "SIM"]:
                                            break
                                        elif continuar in ["NÃO", "NAO", "N"]:
                                            print(
                                                f'{cor["ciano"]}SAINDO DO CALCULO{cor["limpa"]}',
                                                end="",
                                            )
                                            for c in range(3):
                                                print(
                                                    f'{cor["ciano"]}.{cor["limpa"]}',
                                                    end="",
                                                    flush=True,
                                                )
                                                sleep(1)
                                            break
                                        elif continuar not in ["SIM", "S"]:
                                            print(
                                                f'{cor["vermelho"]}OPÇÃO INVALIDA! TENTE NOVAMENTE.{cor["limpa"]}'
                                            )
                                            print(f'{cor["branco"]}─{cor["limpa"]}' * 25)

                                    if continuar in ["NÃO", "NAO", "N"]:
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
                                f'{cor["verde"]}CERTO. VAMOS REALIZAR AS OPERAÇÕES.{cor["limpa"]}'
                            )
                            print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                            while True:
                                n1_str = input(
                                    f'{cor["branco"]}Primeira Parcela: {cor["limpa"]}'
                                )
                                n2_str = input(
                                    f'{cor["branco"]}Segunda Parcela: {cor["limpa"]}'
                                )
                                n3_str = input(
                                    f'{cor["branco"]}Terceira Parcela: {cor["limpa"]}'
                                )
                                if (
                                    all(c in "01" for c in n1_str)
                                    and all(c in "01" for c in n2_str)
                                    and all(c in "01" for c in n3_str)
                                ):
                                    n1_dec = int(n1_str, 2)
                                    n2_dec = int(n2_str, 2)
                                    n3_dec = int(n3_str, 2)
                                    somar_dec = n1_dec + n2_dec + n3_dec
                                    result_bin = bin(somar_dec)
                                    result_str = (
                                        str(result_bin[2:])
                                        .replace("1", "V")
                                        .replace("0", "F")
                                    )
                                    n1_c = n1_str.replace("1", "V").replace("0", "F")
                                    n2_c = n2_str.replace("1", "V").replace("0", "F")
                                    n3_c = n3_str.replace("1", "V").replace("0", "F")
                                    n1_colorido = n1_c.replace(
                                        "F", f'{cor["vermelho"]}0{cor["limpa"]}'
                                    ).replace("V", f'{cor["verde"]}1{cor["limpa"]}')
                                    n2_colorido = n2_c.replace(
                                        "F", f'{cor["vermelho"]}0{cor["limpa"]}'
                                    ).replace("V", f'{cor["verde"]}1{cor["limpa"]}')
                                    n3_colorido = n3_c.replace(
                                        "F", f'{cor["vermelho"]}0{cor["limpa"]}'
                                    ).replace("V", f'{cor["verde"]}1{cor["limpa"]}')
                                    result_colorido = result_str.replace(
                                        "F", f'{cor["vermelho"]}0{cor["limpa"]}'
                                    ).replace("V", f'{cor["verde"]}1{cor["limpa"]}')
                                    print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                                    for c in range(4):
                                        ponto = f"." * c
                                        print(
                                            f'\r\033[1;95m{"PROCESSANDO" + ponto:^25}\033[0m',
                                            end="",
                                            flush=True,
                                        )
                                        sleep(1.5)
                                    print()
                                    print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                                    print(f'{cor["verde"]}RESULTADO{cor["limpa"]}')
                                    print(
                                        f'{cor["branco"]}A soma entre{cor["limpa"]} {n1_colorido} {cor["branco"]}+{cor["limpa"]} '
                                        f'{n2_colorido} {cor["branco"]}+{cor["limpa"]} {n3_colorido} '
                                        f'{cor["branco"]}é ={cor["limpa"]} {result_colorido}'
                                    )
                                    continuar = ""
                                    while True:
                                        continuar = (
                                            input(
                                                f'{cor["amarelo"]}Deseja converter outro valor? (S/N): {cor["limpa"]}'
                                            )
                                            .upper()
                                            .strip()
                                        )
                                        print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                                        if continuar in ["S", "SIM"]:
                                            break
                                        elif continuar in ["NÃO", "NAO", "N"]:
                                            print(
                                                f'{cor["ciano"]}SAINDO DO CALCULO{cor["limpa"]}',
                                                end="",
                                            )
                                            for c in range(3):
                                                print(
                                                    f'{cor["ciano"]}.{cor["limpa"]}',
                                                    end="",
                                                    flush=True,
                                                )
                                                sleep(1)
                                            break
                                        elif continuar not in ["SIM", "S"]:
                                            print(
                                                f'{cor["vermelho"]}OPÇÃO INVALIDA! TENTE NOVAMENTE.{cor["limpa"]}'
                                            )
                                            print(f'{cor["branco"]}─{cor["limpa"]}' * 25)

                                    if continuar in ["NÃO", "NAO", "N"]:
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
                                f'{cor["verde"]}CERTO. VAMOS REALIZAR AS OPERAÇÕES.{cor["limpa"]}'
                            )
                            print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                            while True:
                                print(
                                    f'{cor["verde"]}CERTO. VAMOS REALIZAR AS OPERAÇÕES.{cor["limpa"]}'
                                )
                                n1_str = input(
                                    f'{cor["branco"]}Primeira Parcela: {cor["limpa"]}'
                                )
                                n2_str = input(
                                    f'{cor["branco"]}Segunda Parcela: {cor["limpa"]}'
                                )
                                n3_str = input(
                                    f'{cor["branco"]}Terceira Parcela: {cor["limpa"]}'
                                )
                                n4_str = input(
                                    f'{cor["branco"]}Quarta Parcela: {cor["limpa"]}'
                                )
                                if (
                                    all(c in "01" for c in n1_str)
                                    and all(c in "01" for c in n2_str)
                                    and all(c in "01" for c in n3_str)
                                    and all(c in "01" for c in n4_str)
                                ):
                                    n1_dec = int(n1_str, 2)
                                    n2_dec = int(n2_str, 2)
                                    n3_dec = int(n3_str, 2)
                                    n4_dec = int(n4_str, 2)
                                    soma_dec = n1_dec + n2_dec + n3_dec + n4_dec
                                    result_bin = bin(soma_dec)
                                    result_str = (
                                        str(result_bin[2:])
                                        .replace("1", "V")
                                        .replace("0", "F")
                                    )
                                    n1_c = n1_str.replace("1", "V").replace("0", "F")
                                    n2_c = n2_str.replace("1", "V").replace("0", "F")
                                    n3_c = n3_str.replace("1", "V").replace("0", "F")
                                    n4_c = n4_str.replace("1", "V").replace("0", "F")
                                    n1_colorido = n1_c.replace(
                                        "F", f'{cor["vermelho"]}0{cor["limpa"]}'
                                    ).replace("V", f'{cor["verde"]}1{cor["limpa"]}')
                                    n2_colorido = n2_c.replace(
                                        "F", f'{cor["vermelho"]}0{cor["limpa"]}'
                                    ).replace("V", f'{cor["verde"]}1{cor["limpa"]}')
                                    n3_colorido = n3_c.replace(
                                        "F", f'{cor["vermelho"]}0{cor["limpa"]}'
                                    ).replace("V", f'{cor["verde"]}1{cor["limpa"]}')
                                    n4_colorido = n4_c.replace(
                                        "F", f'{cor["vermelho"]}0{cor["limpa"]}'
                                    ).replace("V", f'{cor["verde"]}1{cor["limpa"]}')
                                    result_colorido = result_str.replace(
                                        "F", f'{cor["vermelho"]}0{cor["limpa"]}'
                                    ).replace("V", f'{cor["verde"]}1{cor["limpa"]}')
                                    print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                                    for c in range(4):
                                        ponto = f"." * c
                                        print(
                                            f'\r\033[1;95m{"PROCESSANDO" + ponto:^25}\033[0m',
                                            end="",
                                            flush=True,
                                        )
                                        sleep(1.5)
                                    print()
                                    print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                                    print(f'{cor["verde"]}RESULTADO{cor["limpa"]}')
                                    print(
                                        f'{cor["branco"]}A soma entre{cor["limpa"]} {n1_colorido} {cor["branco"]}+{cor["limpa"]} '
                                        f'{n2_colorido} {cor["branco"]}+{cor["limpa"]} {n3_colorido} '
                                        f'{cor["branco"]}+{cor["limpa"]} {n4_colorido}{cor["branco"]} é ={cor["limpa"]} {result_colorido}'
                                    )
                                    continuar = ""
                                    while True:
                                        continuar = (
                                            input(
                                                f'{cor["amarelo"]}Deseja converter outro valor? (S/N): {cor["limpa"]}'
                                            )
                                            .upper()
                                            .strip()
                                        )
                                        print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                                        if continuar in ["S", "SIM"]:
                                            break
                                        elif continuar in ["NÃO", "NAO", "N"]:
                                            print(
                                                f'{cor["ciano"]}SAINDO DO CALCULO{cor["limpa"]}',
                                                end="",
                                            )
                                            for c in range(3):
                                                print(
                                                    f'{cor["ciano"]}.{cor["limpa"]}',
                                                    end="",
                                                    flush=True,
                                                )
                                                sleep(1)
                                            break
                                        elif continuar not in ["SIM", "S"]:
                                            print(
                                                f'{cor["vermelho"]}OPÇÃO INVALIDA! TENTE NOVAMENTE.{cor["limpa"]}'
                                            )
                                            print(f'{cor["branco"]}─{cor["limpa"]}' * 25)

                                    if continuar in ["NÃO", "NAO", "N"]:
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
                                f'{cor["branco"]}DIGITE{cor["limpa"]} {cor["verde"]}[1]{cor["limpa"]} {cor["branco"]}PARA DUAS PARCELAS{cor["limpa"]}'
                            )
                            print(
                                f'{cor["branco"]}DIGITE{cor["limpa"]} {cor["verde"]}[2]{cor["limpa"]} {cor["branco"]}PARA TRÊS PARCELAS{cor["limpa"]}'
                            )
                            print(
                                f'{cor["branco"]}DIGITE{cor["limpa"]} {cor["verde"]}[3]{cor["limpa"]} {cor["branco"]}PARA QUATRO PARCELAS{cor["limpa"]}'
                            )
                            print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                            num_str = str(
                                input(f'{cor["roxo"]}DIGITE AQUI: {cor["limpa"]}')
                            )
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
                                f'{cor["verde"]}CERTO. VAMOS REALIZAR A OPERAÇÃO.{cor["limpa"]}'
                            )
                            print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                            while True:
                                n1_str = input(
                                    f'{cor["branco"]}Primeira Parcela: {cor["limpa"]}'
                                )
                                n2_str = input(
                                    f'{cor["branco"]}Segunda Parcela: {cor["limpa"]}'
                                )
                                if all(c in "01" for c in n1_str) and all(
                                    c in "01" for c in n2_str
                                ):
                                    n1_dec = int(n1_str, 2)
                                    n2_dec = int(n2_str, 2)
                                    somar_dec = n1_dec - n2_dec
                                    result_bin = bin(somar_dec)
                                    result_str = (
                                        str(result_bin[2:])
                                        .replace("1", "V")
                                        .replace("0", "F")
                                    )
                                    n1_c = n1_str.replace("1", "V").replace("0", "F")
                                    n2_c = n2_str.replace("1", "V").replace("0", "F")
                                    n1_colorido = n1_c.replace(
                                        "F", f'{cor["vermelho"]}0{cor["limpa"]}'
                                    ).replace("V", f'{cor["verde"]}1{cor["limpa"]}')
                                    n2_colorido = n2_c.replace(
                                        "F", f'{cor["vermelho"]}0{cor["limpa"]}'
                                    ).replace("V", f'{cor["verde"]}1{cor["limpa"]}')
                                    result_colorido = result_str.replace(
                                        "F", f'{cor["vermelho"]}0{cor["limpa"]}'
                                    ).replace("V", f'{cor["verde"]}1{cor["limpa"]}')
                                    print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                                    for c in range(4):
                                        ponto = f"." * c
                                        print(
                                            f'\r\033[1;95m{"PROCESSANDO" + ponto:^25}\033[0m',
                                            end="",
                                            flush=True,
                                        )
                                        sleep(1.5)
                                    print()
                                    print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                                    print(f'{cor["verde"]}RESULTADO{cor["limpa"]}')
                                    if somar_dec < 0:
                                        result_format = f"{result_bin[0] + result_bin[3:]}"
                                        result_str2 = (
                                            str(result_format)
                                            .replace("1", "V")
                                            .replace("0", "F")
                                        )
                                        result_colorido1 = (
                                            result_str2.replace(
                                                "-", f'{cor["vermelho"]}-{cor["limpa"]}'
                                            )
                                            .replace(
                                                "F", f'{cor["vermelho"]}0{cor["limpa"]}'
                                            )
                                            .replace("V", f'{cor["verde"]}1{cor["limpa"]}')
                                        )
                                        print(
                                            f"A subtração entre {n1_colorido} - {n2_colorido} é = {result_colorido1}"
                                        )
                                    else:
                                        print(
                                            f"A subtração entre {n1_colorido} - {n2_colorido} é = {result_colorido}"
                                        )
                                    continuar = ""
                                    while True:
                                        continuar = (
                                            input(
                                                f'{cor["amarelo"]}Deseja converter outro valor? (S/N): {cor["limpa"]}'
                                            )
                                            .upper()
                                            .strip()
                                        )
                                        print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                                        if continuar in ["S", "SIM"]:
                                            break
                                        elif continuar in ["NÃO", "NAO", "N"]:
                                            print(
                                                f'{cor["ciano"]}SAINDO DO CALCULO{cor["limpa"]}',
                                                end="",
                                            )
                                            for c in range(3):
                                                print(
                                                    f'{cor["ciano"]}.{cor["limpa"]}',
                                                    end="",
                                                    flush=True,
                                                )
                                                sleep(1)
                                            break
                                        elif continuar not in ["SIM", "S"]:
                                            print(
                                                f'{cor["vermelho"]}OPÇÃO INVALIDA! TENTE NOVAMENTE.{cor["limpa"]}'
                                            )
                                            print(f'{cor["branco"]}─{cor["limpa"]}' * 25)

                                    if continuar in ["NÃO", "NAO", "N"]:
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
                                f'{cor["verde"]}CERTO. VAMOS REALIZAR AS OPERAÇÕES.{cor["limpa"]}'
                            )
                            print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                            while True:
                                n1_str = input(
                                    f'{cor["branco"]}Primeira Parcela: {cor["limpa"]}'
                                )
                                n2_str = input(
                                    f'{cor["branco"]}Segunda Parcela: {cor["limpa"]}'
                                )
                                n3_str = input(
                                    f'{cor["branco"]}Terceira Parcela: {cor["limpa"]}'
                                )
                                if (
                                    all(c in "01" for c in n1_str)
                                    and all(c in "01" for c in n2_str)
                                    and all(c in "01" for c in n3_str)
                                ):
                                    n1_dec = int(n1_str, 2)
                                    n2_dec = int(n2_str, 2)
                                    n3_dec = int(n3_str, 2)
                                    somar_dec = n1_dec - n2_dec - n3_dec
                                    result_bin = bin(somar_dec)
                                    result_str = (
                                        str(result_bin[2:])
                                        .replace("1", "V")
                                        .replace("0", "F")
                                    )
                                    n1_c = n1_str.replace("1", "V").replace("0", "F")
                                    n2_c = n2_str.replace("1", "V").replace("0", "F")
                                    n3_c = n3_str.replace("1", "V").replace("0", "F")
                                    n1_colorido = n1_c.replace(
                                        "F", f'{cor["vermelho"]}0{cor["limpa"]}'
                                    ).replace("V", f'{cor["verde"]}1{cor["limpa"]}')
                                    n2_colorido = n2_c.replace(
                                        "F", f'{cor["vermelho"]}0{cor["limpa"]}'
                                    ).replace("V", f'{cor["verde"]}1{cor["limpa"]}')
                                    n3_colorido = n3_c.replace(
                                        "F", f'{cor["vermelho"]}0{cor["limpa"]}'
                                    ).replace("V", f'{cor["verde"]}1{cor["limpa"]}')
                                    result_colorido = result_str.replace(
                                        "F", f'{cor["vermelho"]}0{cor["limpa"]}'
                                    )
                                    print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                                    for c in range(4):
                                        ponto = f"." * c
                                        print(
                                            f'\r\033[1;95m{"PROCESSANDO" + ponto:^25}\033[0m',
                                            end="",
                                            flush=True,
                                        )
                                        sleep(1.5)
                                    print()
                                    print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                                    print(f'{cor["verde"]}RESULTADO{cor["limpa"]}')
                                    if somar_dec < 0:
                                        result_format = f"{result_bin[0] + result_bin[3:]}"
                                        result_str2 = (
                                            str(result_format)
                                            .replace("1", "V")
                                            .replace("0", "F")
                                        )
                                        result_colorido1 = (
                                            result_str2.replace(
                                                "-", f'{cor["vermelho"]}-{cor["limpa"]}'
                                            )
                                            .replace(
                                                "F", f'{cor["vermelho"]}0{cor["limpa"]}'
                                            )
                                            .replace("V", f'{cor["verde"]}1{cor["limpa"]}')
                                        )
                                        print(
                                            f"A subtração entre {n1_colorido} - {n2_colorido} - {n3_colorido} é = {result_colorido1}"
                                        )
                                    else:
                                        print(
                                            f"A subtração entre {n1_colorido} - {n2_colorido} - {n3_colorido} é = {result_colorido}"
                                        )
                                    continuar = ""
                                    while True:
                                        continuar = (
                                            input(
                                                f'{cor["amarelo"]}Deseja converter outro valor? (S/N): {cor["limpa"]}'
                                            )
                                            .upper()
                                            .strip()
                                        )
                                        print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                                        if continuar in ["S", "SIM"]:
                                            break
                                        elif continuar in ["NÃO", "NAO", "N"]:
                                            print(
                                                f'{cor["ciano"]}SAINDO DO CALCULO{cor["limpa"]}',
                                                end="",
                                            )
                                            for c in range(3):
                                                print(
                                                    f'{cor["ciano"]}.{cor["limpa"]}',
                                                    end="",
                                                    flush=True,
                                                )
                                                sleep(1)
                                            break
                                        elif continuar not in ["SIM", "S"]:
                                            print(
                                                f'{cor["vermelho"]}OPÇÃO INVALIDA! TENTE NOVAMENTE.{cor["limpa"]}'
                                            )
                                            print(f'{cor["branco"]}─{cor["limpa"]}' * 25)

                                    if continuar in ["NÃO", "NAO", "N"]:
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
                                f'{cor["verde"]}CERTO. VAMOS REALIZAR AS OPERAÇÕES.{cor["limpa"]}'
                            )
                            print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                            while True:
                                n1_str = input(
                                    f'{cor["branco"]}Primeira Parcela: {cor["limpa"]}'
                                )
                                n2_str = input(
                                    f'{cor["branco"]}Segunda Parcela: {cor["limpa"]}'
                                )
                                n3_str = input(
                                    f'{cor["branco"]}Terceira Parcela: {cor["limpa"]}'
                                )
                                n4_str = input(
                                    f'{cor["branco"]}Quarta Parcela: {cor["limpa"]}'
                                )
                                if (
                                    all(c in "01" for c in n1_str)
                                    and all(c in "01" for c in n2_str)
                                    and all(c in "01" for c in n3_str)
                                    and all(c in "01" for c in n4_str)
                                ):
                                    n1_dec = int(n1_str, 2)
                                    n2_dec = int(n2_str, 2)
                                    n3_dec = int(n3_str, 2)
                                    n4_dec = int(n4_str, 2)
                                    somar_dec = n1_dec - n2_dec - n3_dec - n4_dec
                                    result_bin = bin(somar_dec)
                                    result_str = (
                                        str(result_bin[2:])
                                        .replace("1", "V")
                                        .replace("0", "F")
                                    )
                                    n1_c = n1_str.replace("1", "V").replace("0", "F")
                                    n2_c = n2_str.replace("1", "V").replace("0", "F")
                                    n3_c = n3_str.replace("1", "V").replace("0", "F")
                                    n4_c = n4_str.replace("1", "V").replace("0", "F")
                                    n1_colorido = n1_c.replace(
                                        "F", f'{cor["vermelho"]}0{cor["limpa"]}'
                                    ).replace("V", f'{cor["verde"]}1{cor["limpa"]}')
                                    n2_colorido = n2_c.replace(
                                        "F", f'{cor["vermelho"]}0{cor["limpa"]}'
                                    ).replace("V", f'{cor["verde"]}1{cor["limpa"]}')
                                    n3_colorido = n3_c.replace(
                                        "F", f'{cor["vermelho"]}0{cor["limpa"]}'
                                    ).replace("V", f'{cor["verde"]}1{cor["limpa"]}')
                                    n4_colorido = n4_c.replace(
                                        "F", f'{cor["vermelho"]}0{cor["limpa"]}'
                                    ).replace("V", f'{cor["verde"]}1{cor["limpa"]}')
                                    result_colorido = result_str.replace(
                                        "F", f'{cor["vermelho"]}0{cor["limpa"]}'
                                    ).replace("V", f'{cor["verde"]}1{cor["limpa"]}')
                                    print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                                    for c in range(4):
                                        ponto = f"." * c
                                        print(
                                            f'\r\033[1;95m{"PROCESSANDO" + ponto:^25}\033[0m',
                                            end="",
                                            flush=True,
                                        )
                                        sleep(1.5)
                                    print()
                                    print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                                    print(f'{cor["verde"]}RESULTADO{cor["limpa"]}')
                                    if somar_dec < 0:
                                        result_format = f"{result_bin[0] + result_bin[3:]}"
                                        result_str2 = (
                                            str(result_format)
                                            .replace("1", "V")
                                            .replace("0", "F")
                                        )
                                        result_colorido1 = (
                                            result_str2.replace(
                                                "-", f'{cor["vermelho"]}-{cor["limpa"]}'
                                            )
                                            .replace(
                                                "F", f'{cor["vermelho"]}0{cor["limpa"]}'
                                            )
                                            .replace("V", f'{cor["verde"]}1{cor["limpa"]}')
                                        )
                                        print(
                                            f"A subtração entre {n1_colorido} - {n2_colorido} - {n3_colorido} - {n4_colorido} "
                                            f"é = {result_colorido1}"
                                        )
                                    else:
                                        print(
                                            f"A subtração entre {n1_colorido} - {n2_colorido} - {n3_colorido} - {n4_colorido} "
                                            f"é = {result_colorido}"
                                        )
                                    continuar = ""
                                    while True:
                                        continuar = (
                                            input(
                                                f'{cor["amarelo"]}Deseja converter outro valor? (S/N): {cor["limpa"]}'
                                            )
                                            .upper()
                                            .strip()
                                        )
                                        print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                                        if continuar in ["S", "SIM"]:
                                            break
                                        elif continuar in ["NÃO", "NAO", "N"]:
                                            print(
                                                f'{cor["ciano"]}SAINDO DO CALCULO{cor["limpa"]}',
                                                end="",
                                            )
                                            for c in range(3):
                                                print(
                                                    f'{cor["ciano"]}.{cor["limpa"]}',
                                                    end="",
                                                    flush=True,
                                                )
                                                sleep(1)
                                            break
                                        elif continuar not in ["SIM", "S"]:
                                            print(
                                                f'{cor["vermelho"]}OPÇÃO INVALIDA! TENTE NOVAMENTE.{cor["limpa"]}'
                                            )
                                            print(f'{cor["branco"]}─{cor["limpa"]}' * 25)

                                    if continuar in ["NÃO", "NAO", "N"]:
                                        break
                                else:
                                    print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                                    print(
                                        f'{cor["vermelho"]}OPERAÇÃO INVÁLIDA! UTILIZE APENAS: {cor["limpa"]}'
                                        f'{cor["verde"]}1s{cor["limpa"]} {cor["branco"]}E{cor["limpa"]} {cor["vermelho"]}0s{cor["limpa"]}'
                                        f'{cor["branco"]}.{cor["limpa"]}'
                                    )
                                    print(f'{cor["branco"]}─{cor["limpa"]}' * 25)

        # * ─────────────────────────────────────────────
        # * OPÇÃO 4 – TABELA VERDADE
        # * ─────────────────────────────────────────────
        elif escolhido == 4:  # ? * Ajusta a logica para concatenar com o loop do menu principal, e outros detalhes
            escolha = 0
            print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
            while True:
                while True:
                    print(f'{cor["roxo"]}QUANTAS PROPOSIÇÕES DESEJA?{cor["limpa"]}')
                    print(
                        f'{cor["verde"]}[ 1 ]{cor["limpa"]} {cor["branco"]}PARA UMA PROPOSIÇÃO: ["a"]{cor["limpa"]}'
                    )
                    print(
                        f'{cor["verde"]}[ 2 ]{cor["limpa"]} {cor["branco"]}PARA DUAS PROPOSIÇÃO: ["a", "b"]{cor["limpa"]}'
                    )
                    print(
                        f'{cor["verde"]}[ 3 ]{cor["limpa"]} {cor["branco"]}PARA TRÊS PROPOSIÇÃO: ["a","b","c"]{cor["limpa"]}'
                    )
                    print(
                        f'{cor["verde"]}[ 4 ]{cor["limpa"]} {cor["branco"]}PARA QUATRO PROPOSIÇÃO: ["a","b","c","d"]{cor["limpa"]}'
                    )
                    escolha_str = str(
                        input(f'{cor["roxo"]}DIGITE AQUI: {cor["limpa"]}')
                    ).strip()
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
                        print(f'{cor["vermelho"]}UTILIZE NÚMEROS.{cor["limpa"]} ')
                        print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                    else:
                        print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                        print(f'{cor["vermelho"]}UTILIZE APENAS NÚMEROS.{cor["limpa"]} ')
                        print(f'{cor["branco"]}─{cor["limpa"]}' * 25)

                if escolha == 1:
                    print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                    for c in range(4):
                        ponto = f"." * c
                        print(
                            f'\r\033[1;95m{"PROCESSANDO" + ponto:^25}\033[0m',
                            end="",
                            flush=True,
                        )
                        sleep(1.5)
                    print()
                    print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                    print(f'{cor["verde"]}RESULTADO{cor["limpa"]}')
                    tabela = ttg.Truths(["a"], ascending=True)
                    tabela_str = str(tabela).replace("1", "V").replace("0", "F")
                    tabela_colorida = (
                        tabela_str.replace("F", f'{cor["vermelho"]}0{cor["limpa"]}')
                        .replace("V", f'{cor["verde"]}1{cor["limpa"]}')
                        .replace("|", f'{cor["amarelo"]}|{cor["limpa"]}')
                        .replace("+", f'{cor["amarelo"]}+{cor["limpa"]}')
                        .replace("-", f'{cor["ciano"]}-{cor["limpa"]}')
                        .replace("a", f'{cor["branco"]}a{cor["limpa"]}')
                    )
                    print(tabela_colorida)
                    continuar = ""
                    while True:
                        continuar = (
                            input(
                                f'{cor["amarelo"]}Deseja visualizar outra tabela? (S/N): {cor["limpa"]}'
                            )
                            .upper()
                            .strip()
                        )
                        print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                        if continuar in ["S", "SIM"]:
                            break
                        elif continuar in ["NÃO", "NAO", "N"]:
                            print(
                                f'{cor["ciano"]}SAINDO DA TABELA VERDADE{cor["limpa"]}',
                                end="",
                            )
                            for c in range(3):
                                print(
                                    f'{cor["ciano"]}.{cor["limpa"]}',
                                    end="",
                                    flush=True,
                                )
                                sleep(1)
                            break
                        elif continuar not in ["SIM", "S"]:
                            print(
                                f'{cor["vermelho"]}OPÇÃO INVALIDA! TENTE NOVAMENTE.{cor["limpa"]}'
                            )
                            print(f'{cor["branco"]}─{cor["limpa"]}' * 25)

                    if continuar in ["NÃO", "NAO", "N"]:
                        break

                elif escolha == 2:
                    print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                    for c in range(4):
                        ponto = f"." * c
                        print(
                            f'\r\033[1;95m{"PROCESSANDO" + ponto:^25}\033[0m',
                            end="",
                            flush=True,
                        )
                        sleep(1.5)
                    print()
                    print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                    print(f'{cor["verde"]}RESULTADO{cor["limpa"]}')
                    tabela = ttg.Truths(["a", "b"], ascending=True)
                    tabela_str = str(tabela).replace("1", "V").replace("0", "F")
                    tabela_colorida = (
                        tabela_str.replace("F", f'{cor["vermelho"]}0{cor["limpa"]}')
                        .replace("V", f'{cor["verde"]}1{cor["limpa"]}')
                        .replace("|", f'{cor["amarelo"]}|{cor["limpa"]}')
                        .replace("+", f'{cor["amarelo"]}+{cor["limpa"]}')
                        .replace("-", f'{cor["ciano"]}-{cor["limpa"]}')
                        .replace("a", f'{cor["branco"]}a{cor["limpa"]}')
                        .replace("b", f'{cor["branco"]}b{cor["limpa"]}')
                    )
                    print(tabela_colorida)
                    continuar = ""
                    while True:
                        continuar = (
                            input(
                                f'{cor["amarelo"]}Deseja visualizar outra tabela? (S/N): {cor["limpa"]}'
                            )
                            .upper()
                            .strip()
                        )
                        print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                        if continuar in ["S", "SIM"]:
                            break
                        elif continuar in ["NÃO", "NAO", "N"]:
                            print(
                                f'{cor["ciano"]}SAINDO DA TABELA VERDADE{cor["limpa"]}',
                                end="",
                            )
                            for c in range(3):
                                print(
                                    f'{cor["ciano"]}.{cor["limpa"]}',
                                    end="",
                                    flush=True,
                                )
                                sleep(1)
                            break
                        elif continuar not in ["SIM", "S"]:
                            print(
                                f'{cor["vermelho"]}OPÇÃO INVALIDA! TENTE NOVAMENTE.{cor["limpa"]}'
                            )
                            print(f'{cor["branco"]}─{cor["limpa"]}' * 25)

                    if continuar in ["NÃO", "NAO", "N"]:
                        break

                elif escolha == 3:
                    print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                    for c in range(4):
                        ponto = f"." * c
                        print(
                            f'\r\033[1;95m{"PROCESSANDO" + ponto:^25}\033[0m',
                            end="",
                            flush=True,
                        )
                        sleep(1.5)
                    print()
                    print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                    print(f'{cor["verde"]}RESULTADO{cor["limpa"]}')
                    tabela = ttg.Truths(["a", "b", "c"], ascending=True)
                    tabela_str = str(tabela).replace("1", "V").replace("0", "F")
                    tabela_colorida = (
                        tabela_str.replace("F", f'{cor["vermelho"]}0{cor["limpa"]}')
                        .replace("V", f'{cor["verde"]}1{cor["limpa"]}')
                        .replace("|", f'{cor["amarelo"]}|{cor["limpa"]}')
                        .replace("+", f'{cor["amarelo"]}+{cor["limpa"]}')
                        .replace("-", f'{cor["ciano"]}-{cor["limpa"]}')
                        .replace("a", f'{cor["branco"]}a{cor["limpa"]}')
                        .replace("b", f'{cor["branco"]}b{cor["limpa"]}')
                        .replace("c", f'{cor["branco"]}c{cor["limpa"]}')
                    )
                    print(tabela_colorida)
                    continuar = ""
                    while True:
                        continuar = (
                            input(
                                f'{cor["amarelo"]}Deseja visualizar outra tabela? (S/N): {cor["limpa"]}'
                            )
                            .upper()
                            .strip()
                        )
                        print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                        if continuar in ["S", "SIM"]:
                            break
                        elif continuar in ["NÃO", "NAO", "N"]:
                            print(
                                f'{cor["ciano"]}SAINDO DA TABELA VERDADE{cor["limpa"]}',
                                end="",
                            )
                            for c in range(3):
                                print(
                                    f'{cor["ciano"]}.{cor["limpa"]}',
                                    end="",
                                    flush=True,
                                )
                                sleep(1)
                            break
                        elif continuar not in ["SIM", "S"]:
                            print(
                                f'{cor["vermelho"]}OPÇÃO INVALIDA! TENTE NOVAMENTE.{cor["limpa"]}'
                            )
                            print(f'{cor["branco"]}─{cor["limpa"]}' * 25)

                    if continuar in ["NÃO", "NAO", "N"]:
                        break

                elif escolha == 4:
                    print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                    for c in range(4):
                        ponto = f"." * c
                        print(
                            f'\r\033[1;95m{"PROCESSANDO" + ponto:^25}\033[0m',
                            end="",
                            flush=True,
                        )
                        sleep(1.5)
                    print()
                    print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                    print(f'{cor["verde"]}RESULTADO{cor["limpa"]}')
                    tabela = ttg.Truths(["a", "b", "c", "d"], ascending=True)
                    tabela_str = str(tabela).replace("1", "V").replace("0", "F")
                    tabela_colorida = (
                        tabela_str.replace("F", f'{cor["vermelho"]}0{cor["limpa"]}')
                        .replace("V", f'{cor["verde"]}1{cor["limpa"]}')
                        .replace("|", f'{cor["amarelo"]}|{cor["limpa"]}')
                        .replace("+", f'{cor["amarelo"]}+{cor["limpa"]}')
                        .replace("-", f'{cor["ciano"]}-{cor["limpa"]}')
                        .replace("a", f'{cor["branco"]}a{cor["limpa"]}')
                        .replace("b", f'{cor["branco"]}b{cor["limpa"]}')
                        .replace("c", f'{cor["branco"]}c{cor["limpa"]}')
                        .replace("d", f'{cor["branco"]}d{cor["limpa"]}')
                    )
                    print(tabela_colorida)
                    continuar = ""
                    while True:
                        continuar = (
                            input(
                                f'{cor["amarelo"]}Deseja visualizar outra tabela? (S/N): {cor["limpa"]}'
                            )
                            .upper()
                            .strip()
                        )
                        print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                        if continuar in ["S", "SIM"]:
                            break
                        elif continuar in ["NÃO", "NAO", "N"]:
                            print(
                                f'{cor["ciano"]}SAINDO DA TABELA VERDADE{cor["limpa"]}',
                                end="",
                            )
                            for c in range(3):
                                print(
                                    f'{cor["ciano"]}.{cor["limpa"]}',
                                    end="",
                                    flush=True,
                                )
                                sleep(1)
                            break
                        elif continuar not in ["SIM", "S"]:
                            print(
                                f'{cor["vermelho"]}OPÇÃO INVALIDA! TENTE NOVAMENTE.{cor["limpa"]}'
                            )
                            print(f'{cor["branco"]}─{cor["limpa"]}' * 25)

                    if continuar in ["NÃO", "NAO", "N"]:
                        break

        # * ─────────────────────────────────────────────
        # * OPÇÃO 5 – EXPRESSÕES BOOLEANAS
        # * ─────────────────────────────────────────────
        elif escolhido == 5:  # ? * Ajusta a logica para concatenar com o loop do menu principal, e outros detalhes
            titulo = "EXPRESSÕES BOOLEANAS"
            print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
            print(f'{cor["ciano"]}{titulo:^25}{cor["limpa"]}')
            print(f'{cor["branco"]}─{cor["limpa"]}' * 25)

            while True:
                valor1 = input(f'{cor["branco"]}Primeira Proposição: {cor["limpa"]}')
                valor2 = input(f'{cor["branco"]}Segunda Proposição: {cor["limpa"]}')
                if "a" <= valor1 <= "d" and "a" <= valor2 <= "d":
                    while True:
                        funcao0 = (
                            input(f'{cor["branco"]}Qual o Operador? {cor["limpa"]}')
                            .lower()
                            .strip()
                        )
                        funcao = funcao0
                        if funcao0 == "&&":
                            funcao = "and"
                        elif funcao0 == "||":
                            funcao = "or"
                        if funcao0 not in ["&&", "and", "||", "or"]:
                            print(
                                f'{cor["vermelho"]}OPÇÃO INVÁLIDA! TENTE NOVAMENTE.{cor["limpa"]}'
                            )
                        else:
                            break
                    if funcao == "and" or funcao == "or":
                        while True:
                            neg = (
                                input(f'{cor["vermelho"]}Esta Negativado? {cor["limpa"]}')
                                .upper()
                                .strip()
                            )
                            tabela = input(
                                f'{cor["branco"]}ATÉ QUE PROPOSIÇÃO DESEJA IR? {cor["limpa"]}'
                            ).lower()
                            print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                            if neg in [
                                "SIM",
                                "S",
                                "N",
                                "NÃO",
                                "NAO",
                            ] and tabela in [
                                "b",
                                "c",
                                "d",
                            ]:
                                break
                            else:
                                print(
                                    f'{cor["vermelho"]}OPÇÃO INVÁLIDA! TENTE NOVAMENTE.{cor["limpa"]}'
                                )
                                print(f'{cor["branco"]}─{cor["limpa"]}' * 25)

                        if neg in ["SIM", "S"]:
                            print(f'{cor["amarelo"]}O QUE ESTA NEGATIVADO?{cor["limpa"]}')
                            print(
                                f'{cor["branco"]}OPÇÃO{cor["limpa"]} {cor["verde"]}[1]{cor["limpa"]}'
                                f'{cor["branco"]}: "{cor["limpa"]}'
                                f'{cor["vermelho"]}not ({valor1}){cor["limpa"]}{cor["branco"]}"{cor["limpa"]}'
                            )
                            print(
                                f'{cor["branco"]}OPÇÃO{cor["limpa"]} {cor["verde"]}[2]{cor["limpa"]}'
                                f'{cor["branco"]}: "{cor["limpa"]}{cor["vermelho"]}not ({valor2}){cor["limpa"]}'
                                f'{cor["branco"]}"{cor["limpa"]}'
                            )
                            print(
                                f'{cor["branco"]}OPÇÃO{cor["limpa"]} {cor["verde"]}[3]{cor["limpa"]}'
                                f'{cor["branco"]}: "{cor["limpa"]}{cor["vermelho"]}'
                                f'not ({valor1} {funcao} {valor2}){cor["limpa"]}{cor["branco"]}"{cor["limpa"]}'
                            )
                            while True:
                                escolha_str = str(
                                    input(f'{cor["roxo"]}DIGITE A OPÇÃO: {cor["limpa"]}')
                                ).strip()

                            # ── Tabela até b ──────────────────────────
                            if escolha == 1 and tabela == "b":
                                tabela_obj = ttg.Truths(
                                    ["a", "b"],
                                    [f"(not {valor1}) {funcao} {valor2}"],
                                    ascending=True,
                                )
                                tabela_str = (
                                    str(tabela_obj).replace("1", "V").replace("0", "F")
                                )
                                tabela_colorida = (
                                    tabela_str.replace(
                                        "F", f'{cor["vermelho"]}0{cor["limpa"]}'
                                    )
                                    .replace("V", f'{cor["verde"]}1{cor["limpa"]}')
                                    .replace("|", f'{cor["amarelo"]}|{cor["limpa"]}')
                                    .replace("+", f'{cor["amarelo"]}+{cor["limpa"]}')
                                    .replace("-", f'{cor["ciano"]}-{cor["limpa"]}')
                                    .replace("a", f'{cor["branco"]}a{cor["limpa"]}')
                                    .replace("b", f'{cor["branco"]}b{cor["limpa"]}')
                                    .replace("not", f'{cor["branco"]}not{cor["limpa"]}')
                                    .replace("or", f'{cor["branco"]}or{cor["limpa"]}')
                                    .replace("nd", f'{cor["branco"]}nd{cor["limpa"]}')
                                    .replace("(", f'{cor["branco"]}({cor["limpa"]}')
                                    .replace(")", f'{cor["branco"]}){cor["limpa"]}')
                                )
                                print(tabela_colorida)
                            elif escolha == 2 and tabela == "b":
                                tabela_obj = ttg.Truths(
                                    ["a", "b"],
                                    [f"{valor1} {funcao} (not {valor2})"],
                                    ascending=True,
                                )
                                tabela_str = (
                                    str(tabela_obj).replace("1", "V").replace("0", "F")
                                )
                                tabela_colorida = (
                                    tabela_str.replace(
                                        "F", f'{cor["vermelho"]}0{cor["limpa"]}'
                                    )
                                    .replace("V", f'{cor["verde"]}1{cor["limpa"]}')
                                    .replace("|", f'{cor["amarelo"]}|{cor["limpa"]}')
                                    .replace("+", f'{cor["amarelo"]}+{cor["limpa"]}')
                                    .replace("-", f'{cor["ciano"]}-{cor["limpa"]}')
                                    .replace("a", f'{cor["branco"]}a{cor["limpa"]}')
                                    .replace("b", f'{cor["branco"]}b{cor["limpa"]}')
                                    .replace("not", f'{cor["branco"]}not{cor["limpa"]}')
                                    .replace("or", f'{cor["branco"]}or{cor["limpa"]}')
                                    .replace("nd", f'{cor["branco"]}nd{cor["limpa"]}')
                                    .replace("(", f'{cor["branco"]}({cor["limpa"]}')
                                    .replace(")", f'{cor["branco"]}){cor["limpa"]}')
                                )
                                print(tabela_colorida)
                            elif escolha == 3 and tabela == "b":
                                tabela_obj = ttg.Truths(
                                    ["a", "b"],
                                    [f"not ({valor1} {funcao} {valor2})"],
                                    ascending=True,
                                )
                                tabela_str = (
                                    str(tabela_obj).replace("1", "V").replace("0", "F")
                                )
                                tabela_colorida = (
                                    tabela_str.replace(
                                        "F", f'{cor["vermelho"]}0{cor["limpa"]}'
                                    )
                                    .replace("V", f'{cor["verde"]}1{cor["limpa"]}')
                                    .replace("|", f'{cor["amarelo"]}|{cor["limpa"]}')
                                    .replace("+", f'{cor["amarelo"]}+{cor["limpa"]}')
                                    .replace("-", f'{cor["ciano"]}-{cor["limpa"]}')
                                    .replace("a", f'{cor["branco"]}a{cor["limpa"]}')
                                    .replace("b", f'{cor["branco"]}b{cor["limpa"]}')
                                    .replace("not", f'{cor["branco"]}not{cor["limpa"]}')
                                    .replace("or", f'{cor["branco"]}or{cor["limpa"]}')
                                    .replace("nd", f'{cor["branco"]}nd{cor["limpa"]}')
                                    .replace("(", f'{cor["branco"]}({cor["limpa"]}')
                                    .replace(")", f'{cor["branco"]}){cor["limpa"]}')
                                )
                                print(tabela_colorida)
                            # ── Tabela até c ──────────────────────────
                            elif escolha == 1 and tabela == "c":
                                tabela_obj = ttg.Truths(
                                    ["a", "b", "c"],
                                    [f"(not {valor1}) {funcao} {valor2}"],
                                    ascending=True,
                                )
                                tabela_str = (
                                    str(tabela_obj).replace("1", "V").replace("0", "F")
                                )
                                tabela_colorida = (
                                    tabela_str.replace(
                                        "F", f'{cor["vermelho"]}0{cor["limpa"]}'
                                    )
                                    .replace("V", f'{cor["verde"]}1{cor["limpa"]}')
                                    .replace("|", f'{cor["amarelo"]}|{cor["limpa"]}')
                                    .replace("+", f'{cor["amarelo"]}+{cor["limpa"]}')
                                    .replace("-", f'{cor["ciano"]}-{cor["limpa"]}')
                                    .replace("a", f'{cor["branco"]}a{cor["limpa"]}')
                                    .replace("b", f'{cor["branco"]}b{cor["limpa"]}')
                                    .replace("c", f'{cor["branco"]}c{cor["limpa"]}')
                                    .replace("not", f'{cor["branco"]}not{cor["limpa"]}')
                                    .replace("or", f'{cor["branco"]}or{cor["limpa"]}')
                                    .replace("nd", f'{cor["branco"]}nd{cor["limpa"]}')
                                    .replace("(", f'{cor["branco"]}({cor["limpa"]}')
                                    .replace(")", f'{cor["branco"]}){cor["limpa"]}')
                                )
                                print(tabela_colorida)
                            elif escolha == 2 and tabela == "c":
                                tabela_obj = ttg.Truths(
                                    ["a", "b", "c"],
                                    [f"{valor1} {funcao} (not {valor2})"],
                                    ascending=True,
                                )
                                tabela_str = (
                                    str(tabela_obj).replace("1", "V").replace("0", "F")
                                )
                                tabela_colorida = (
                                    tabela_str.replace(
                                        "F", f'{cor["vermelho"]}0{cor["limpa"]}'
                                    )
                                    .replace("V", f'{cor["verde"]}1{cor["limpa"]}')
                                    .replace("|", f'{cor["amarelo"]}|{cor["limpa"]}')
                                    .replace("+", f'{cor["amarelo"]}+{cor["limpa"]}')
                                    .replace("-", f'{cor["ciano"]}-{cor["limpa"]}')
                                    .replace("a", f'{cor["branco"]}a{cor["limpa"]}')
                                    .replace("b", f'{cor["branco"]}b{cor["limpa"]}')
                                    .replace("c", f'{cor["branco"]}c{cor["limpa"]}')
                                    .replace("not", f'{cor["branco"]}not{cor["limpa"]}')
                                    .replace("or", f'{cor["branco"]}or{cor["limpa"]}')
                                    .replace("nd", f'{cor["branco"]}nd{cor["limpa"]}')
                                    .replace("(", f'{cor["branco"]}({cor["limpa"]}')
                                    .replace(")", f'{cor["branco"]}){cor["limpa"]}')
                                )
                                print(tabela_colorida)
                            elif escolha == 3 and tabela == "c":
                                tabela_obj = ttg.Truths(
                                    ["a", "b", "c"],
                                    [f"not ({valor1} {funcao} {valor2})"],
                                    ascending=True,
                                )
                                tabela_str = (
                                    str(tabela_obj).replace("1", "V").replace("0", "F")
                                )
                                tabela_colorida = (
                                    tabela_str.replace(
                                        "F", f'{cor["vermelho"]}0{cor["limpa"]}'
                                    )
                                    .replace("V", f'{cor["verde"]}1{cor["limpa"]}')
                                    .replace("|", f'{cor["amarelo"]}|{cor["limpa"]}')
                                    .replace("+", f'{cor["amarelo"]}+{cor["limpa"]}')
                                    .replace("-", f'{cor["ciano"]}-{cor["limpa"]}')
                                    .replace("a", f'{cor["branco"]}a{cor["limpa"]}')
                                    .replace("b", f'{cor["branco"]}b{cor["limpa"]}')
                                    .replace("c", f'{cor["branco"]}c{cor["limpa"]}')
                                    .replace("not", f'{cor["branco"]}not{cor["limpa"]}')
                                    .replace("or", f'{cor["branco"]}or{cor["limpa"]}')
                                    .replace("nd", f'{cor["branco"]}nd{cor["limpa"]}')
                                    .replace("(", f'{cor["branco"]}({cor["limpa"]}')
                                    .replace(")", f'{cor["branco"]}){cor["limpa"]}')
                                )
                                print(tabela_colorida)
                            # ── Tabela até d ──────────────────────────
                            elif escolha == 1 and tabela == "d":
                                tabela_obj = ttg.Truths(
                                    ["a", "b", "c", "d"],
                                    [f"(not {valor1}) {funcao} {valor2}"],
                                    ascending=True,
                                )
                                tabela_str = (
                                    str(tabela_obj).replace("1", "V").replace("0", "F")
                                )
                                tabela_colorida = (
                                    tabela_str.replace(
                                        "F", f'{cor["vermelho"]}0{cor["limpa"]}'
                                    )
                                    .replace("V", f'{cor["verde"]}1{cor["limpa"]}')
                                    .replace("|", f'{cor["amarelo"]}|{cor["limpa"]}')
                                    .replace("+", f'{cor["amarelo"]}+{cor["limpa"]}')
                                    .replace("-", f'{cor["ciano"]}-{cor["limpa"]}')
                                    .replace("a", f'{cor["branco"]}a{cor["limpa"]}')
                                    .replace("b", f'{cor["branco"]}b{cor["limpa"]}')
                                    .replace("c", f'{cor["branco"]}c{cor["limpa"]}')
                                    .replace("d", f'{cor["branco"]}d{cor["limpa"]}')
                                    .replace("ot", f'{cor["branco"]}ot{cor["limpa"]}')
                                    .replace("or", f'{cor["branco"]}or{cor["limpa"]}')
                                    .replace("n", f'{cor["branco"]}n{cor["limpa"]}')
                                    .replace("(", f'{cor["branco"]}({cor["limpa"]}')
                                    .replace(")", f'{cor["branco"]}){cor["limpa"]}')
                                )
                                print(tabela_colorida)
                            elif escolha == 2 and tabela == "d":
                                tabela_obj = ttg.Truths(
                                    ["a", "b", "c", "d"],
                                    [f"{valor1} {funcao} (not {valor2})"],
                                    ascending=True,
                                )
                                tabela_str = (
                                    str(tabela_obj).replace("1", "V").replace("0", "F")
                                )
                                tabela_colorida = (
                                    tabela_str.replace(
                                        "F", f'{cor["vermelho"]}0{cor["limpa"]}'
                                    )
                                    .replace("V", f'{cor["verde"]}1{cor["limpa"]}')
                                    .replace("|", f'{cor["amarelo"]}|{cor["limpa"]}')
                                    .replace("+", f'{cor["amarelo"]}+{cor["limpa"]}')
                                    .replace("-", f'{cor["ciano"]}-{cor["limpa"]}')
                                    .replace("a", f'{cor["branco"]}a{cor["limpa"]}')
                                    .replace("b", f'{cor["branco"]}b{cor["limpa"]}')
                                    .replace("c", f'{cor["branco"]}c{cor["limpa"]}')
                                    .replace("d", f'{cor["branco"]}d{cor["limpa"]}')
                                    .replace("ot", f'{cor["branco"]}ot{cor["limpa"]}')
                                    .replace("or", f'{cor["branco"]}or{cor["limpa"]}')
                                    .replace("n", f'{cor["branco"]}n{cor["limpa"]}')
                                    .replace("(", f'{cor["branco"]}({cor["limpa"]}')
                                    .replace(")", f'{cor["branco"]}){cor["limpa"]}')
                                )
                                print(tabela_colorida)
                            elif escolha == 3 and tabela == "d":
                                tabela_obj = ttg.Truths(
                                    ["a", "b", "c", "d"],
                                    [f"not ({valor1} {funcao} {valor2})"],
                                    ascending=True,
                                )
                                tabela_str = (
                                    str(tabela_obj).replace("1", "V").replace("0", "F")
                                )
                                tabela_colorida = (
                                    tabela_str.replace(
                                        "F", f'{cor["vermelho"]}0{cor["limpa"]}'
                                    )
                                    .replace("V", f'{cor["verde"]}1{cor["limpa"]}')
                                    .replace("|", f'{cor["amarelo"]}|{cor["limpa"]}')
                                    .replace("+", f'{cor["amarelo"]}+{cor["limpa"]}')
                                    .replace("-", f'{cor["ciano"]}-{cor["limpa"]}')
                                    .replace("a", f'{cor["branco"]}a{cor["limpa"]}')
                                    .replace("b", f'{cor["branco"]}b{cor["limpa"]}')
                                    .replace("c", f'{cor["branco"]}c{cor["limpa"]}')
                                    .replace("d", f'{cor["branco"]}d{cor["limpa"]}')
                                    .replace("ot", f'{cor["branco"]}ot{cor["limpa"]}')
                                    .replace("or", f'{cor["branco"]}or{cor["limpa"]}')
                                    .replace("n", f'{cor["branco"]}n{cor["limpa"]}')
                                    .replace("(", f'{cor["branco"]}({cor["limpa"]}')
                                    .replace(")", f'{cor["branco"]}){cor["limpa"]}')
                                )
                                print(tabela_colorida)
                            else:
                                print(
                                    f'{cor["vermelho"]}OPÇÃO {tabela} INVÁLIDA. TENTE NOVAMENTE.{cor["limpa"]}'
                                )

                        else:  # sem negação
                            if tabela == "b":
                                tabela_obj = ttg.Truths(
                                    ["a", "b"],
                                    [f"{valor1} {funcao} {valor2}"],
                                    ascending=True,
                                )
                                tabela_str = (
                                    str(tabela_obj).replace("1", "V").replace("0", "F")
                                )
                                tabela_colorida = (
                                    tabela_str.replace(
                                        "F", f'{cor["vermelho"]}0{cor["limpa"]}'
                                    )
                                    .replace("V", f'{cor["verde"]}1{cor["limpa"]}')
                                    .replace("|", f'{cor["amarelo"]}|{cor["limpa"]}')
                                    .replace("+", f'{cor["amarelo"]}+{cor["limpa"]}')
                                    .replace("-", f'{cor["ciano"]}-{cor["limpa"]}')
                                    .replace("a", f'{cor["branco"]}a{cor["limpa"]}')
                                    .replace("b", f'{cor["branco"]}b{cor["limpa"]}')
                                    .replace("or", f'{cor["branco"]}or{cor["limpa"]}')
                                    .replace("nd", f'{cor["branco"]}nd{cor["limpa"]}')
                                    .replace("(", f'{cor["branco"]}({cor["limpa"]}')
                                    .replace(")", f'{cor["branco"]}){cor["limpa"]}')
                                )
                                print(tabela_colorida)
                            elif tabela == "c":
                                tabela_obj = ttg.Truths(
                                    ["a", "b", "c"],
                                    [f"{valor1} {funcao} {valor2}"],
                                    ascending=True,
                                )
                                tabela_str = (
                                    str(tabela_obj).replace("1", "V").replace("0", "F")
                                )
                                tabela_colorida = (
                                    tabela_str.replace(
                                        "F", f'{cor["vermelho"]}0{cor["limpa"]}'
                                    )
                                    .replace("V", f'{cor["verde"]}1{cor["limpa"]}')
                                    .replace("|", f'{cor["amarelo"]}|{cor["limpa"]}')
                                    .replace("+", f'{cor["amarelo"]}+{cor["limpa"]}')
                                    .replace("-", f'{cor["ciano"]}-{cor["limpa"]}')
                                    .replace("a", f'{cor["branco"]}a{cor["limpa"]}')
                                    .replace("b", f'{cor["branco"]}b{cor["limpa"]}')
                                    .replace("c", f'{cor["branco"]}c{cor["limpa"]}')
                                    .replace("or", f'{cor["branco"]}or{cor["limpa"]}')
                                    .replace("nd", f'{cor["branco"]}nd{cor["limpa"]}')
                                    .replace("(", f'{cor["branco"]}({cor["limpa"]}')
                                    .replace(")", f'{cor["branco"]}){cor["limpa"]}')
                                )
                                print(tabela_colorida)
                            elif tabela == "d":
                                tabela_obj = ttg.Truths(
                                    ["a", "b", "c", "d"],
                                    [f"{valor1} {funcao} {valor2}"],
                                    ascending=True,
                                )
                                tabela_str = (
                                    str(tabela_obj).replace("1", "V").replace("0", "F")
                                )
                                tabela_colorida = (
                                    tabela_str.replace(
                                        "F", f'{cor["vermelho"]}0{cor["limpa"]}'
                                    )
                                    .replace("V", f'{cor["verde"]}1{cor["limpa"]}')
                                    .replace("|", f'{cor["amarelo"]}|{cor["limpa"]}')
                                    .replace("+", f'{cor["amarelo"]}+{cor["limpa"]}')
                                    .replace("-", f'{cor["ciano"]}-{cor["limpa"]}')
                                    .replace("a", f'{cor["branco"]}a{cor["limpa"]}')
                                    .replace("b", f'{cor["branco"]}b{cor["limpa"]}')
                                    .replace("c", f'{cor["branco"]}c{cor["limpa"]}')
                                    .replace("d", f'{cor["branco"]}d{cor["limpa"]}')
                                    .replace("or", f'{cor["branco"]}or{cor["limpa"]}')
                                    .replace("n", f'{cor["branco"]}n{cor["limpa"]}')
                                    .replace("(", f'{cor["branco"]}({cor["limpa"]}')
                                    .replace(")", f'{cor["branco"]}){cor["limpa"]}')
                                )
                                print(tabela_colorida)
                            else:
                                print(
                                    f'{cor["vermelho"]}OPÇÃO {tabela} INVÁLIDA. TENTE NOVAMENTE.{cor["limpa"]}'
                                )

                    else:
                        print(
                            f'{cor["vermelho"]}OPÇÃO {funcao} INVÁLIDA. TENTE NOVAMENTE.{cor["limpa"]}'
                        )

                        continuar = (
                            input(
                                f'{cor["amarelo"]}Deseja calcular outra expressão booleana? (S/N): {cor["limpa"]}'
                            )
                            .upper()
                            .strip()
                        )
                        if continuar != "S":
                            print(
                                f'{cor["ciano"]}Saindo das expressões booleanas...{cor["limpa"]}'
                            )
                            break
                else:
                    print(
                        f'{cor["vermelho"]}VALOR INVALIDO! COLOQUE LETRAS DE{cor["limpa"]} '
                        f'{cor["branco"]}A ATÉ D.{cor["limpa"]}'
                    )
    if escolhido != 0:
        print()
    print(
        f'{cor["branco"]}─{cor["limpa"]}' * 25)
    print(
        f'{cor["verde"]}{'── FIM DO PROGRAMA ──────────────────────────':^25}{cor["limpa"]}')
except KeyboardInterrupt:
    print()
    print(f'\n{cor["vermelho"]}PROGRAMA ENCERRADO!{cor["limpa"]}')
    input(f'{cor["branco"]}PRESSIONE ENTER PARA SAIR...{cor["limpa"]}')
except EOFError:
    print()
    print(f'\n{cor["vermelho"]}PROGRAMA ENCERRADO!{cor["limpa"]}')
    input(f'{cor["branco"]}PRESSIONE ENTER PARA SAIR...{cor["limpa"]}')