try:
    from importacao.imports import *
    # TODO: CORES
    cor = paleta_cor()

    # TODO: DATA DE EXIBIÇÃO
    data_formatada = data_atual(cor)

    # TODO: MENUS DO SISTEMA
    titulo = f'{cor["ciano"]}{"NÚMEROS BINÁRIOS":^25}{cor["limpa"]}'
    menu_principal = (  # * Menu principal do programa.
        f'{cor["amarelo"]}ESCOLHA A OPÇÃO DESEJADA:{cor["limpa"]}\n'
        f'{cor["verde"]}[ 1 ]{cor["limpa"]} {cor["verde"]}CONVERSÃO{cor["limpa"]}\n'
        f'{cor["verde"]}[ 2 ]{cor["limpa"]} {cor["ciano"]}NOMES EM BINÁRIOS{cor["limpa"]}\n'
        f'{cor["verde"]}[ 3 ]{cor["limpa"]} {cor["roxo"]}OPERAÇÕES BINÁRIAS{cor["limpa"]}\n'
        f'{cor["verde"]}[ 4 ]{cor["limpa"]} {cor["azul"]}TABELA VERDADE{cor["limpa"]}\n'
        f'{cor["verde"]}[ 5 ]{cor["limpa"]} {cor["amarelo"]}EXPRESSÕES BOOLEANAS{cor["limpa"]}\n'
        f'{cor["verde"]}[ 6 ]{cor["limpa"]} {cor["ciano"]}MAPA DE KARNAUGH{cor["limpa"]}\n'
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
        f'{cor["verde"]}[ 4 ]{cor["limpa"]} {cor["roxo"]}HEXADECIMAL{cor["limpa"]}\n'
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
    while True:
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
                if escolhido == 0 or 1 <= escolhido <= 5:
                    break
                else:
                    print(
                        f'{cor["vermelho"]}❌ ENTRADA INVÁLIDA!\n{cor["limpa"]}'
                        f'{cor["branco"]}DIGITE{cor["limpa"]} {cor["verde"]}[1-5]{cor["limpa"]} '
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

        if escolhido == 1:  # * Opção 1 – CONVERSÕES
            while True:  # * Loop menu de conversões
                limpatela()
                print(data_formatada)
                print(titulo_conversões)
                print(menu_conversões)
                print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                opcao_str = str(input(f'{cor["roxo"]}DIGITE SUA OPÇÃO [DIGITE 0 PARA VOLTAR]: {cor["limpa"]}')).strip()
                print()

                if not opcao_str.isdigit():
                    print(f'{cor["vermelho"]}❌ ENTRADA INVÁLIDA!\n{cor["limpa"]}{cor["amarelo"]}UTILIZE APENAS NÚMEROS.{cor["limpa"]}')
                    print()
                    input(f'{cor["branco"]}PRESSIONE ENTER PARA CONTINUAR...{cor["limpa"]}')
                    continue

                opcao = int(opcao_str)
                if opcao == 0:
                    break  # * Volta ao menu principal

                elif opcao == 1:  # * Menu de conversões decimais
                    while True:
                        limpatela()
                        print(data_formatada)
                        print(titulo_decimais)
                        print(menu_decimais)
                        print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                        op_decimais_str = str(input(f'{cor["branco"]}Digite sua opção [DIGITE 0 PARA O MENU ANTERIOR]: {cor["limpa"]}')).strip()
                        print()

                        if not op_decimais_str.isdigit():
                            print(f'{cor["vermelho"]}❌ ENTRADA INVÁLIDA!\n{cor["limpa"]}{cor["amarelo"]}UTILIZE APENAS NÚMEROS.{cor["limpa"]}')
                            print(); input(f'{cor["branco"]}PRESSIONE ENTER PARA CONTINUAR...{cor["limpa"]}')
                            continue

                        op_decimais = int(op_decimais_str)
                        
                        if op_decimais == 0:
                            break  # * Sai do menu de decimais e volta para o menu de conversões
                        elif op_decimais == 1:
                            converter_de_decimal_binario(cor, data_formatada)
                        elif op_decimais == 2:
                            converter_de_decimal_octal(cor, data_formatada)
                        elif op_decimais == 3:
                            converter_de_decimal_hexadecimal(cor, data_formatada)
                        else:
                            print(f'{cor["vermelho"]}❌ ENTRADA INVÁLIDA!\n{cor["limpa"]}{cor["branco"]}DIGITE {cor["verde"]}[1-3]{cor["limpa"]} ou {cor["vermelho"]}[0]{cor["limpa"]} PARA VOLTAR.')
                            print(); input(f'{cor["branco"]}PRESSIONE ENTER PARA CONTINUAR...{cor["limpa"]}')

                elif opcao == 2:  # * Menu de conversões binárias
                    while True:
                        limpatela()
                        print(data_formatada)
                        print(titulo_binarios)
                        print(menu_binarios)
                        print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                        op_binario_str = str(input(f'{cor["branco"]}Digite sua opção [DIGITE 0 PARA O MENU ANTERIOR]: {cor["limpa"]}')).strip()
                        print()

                        if not op_binario_str.isdigit():
                            print(f'{cor["vermelho"]}❌ ENTRADA INVÁLIDA!\n{cor["limpa"]}{cor["amarelo"]}UTILIZE APENAS NÚMEROS.{cor["limpa"]}')
                            print(); input(f'{cor["branco"]}PRESSIONE ENTER PARA CONTINUAR...{cor["limpa"]}')
                            continue

                        op_binario = int(op_binario_str)
                        
                        if op_binario == 0:
                            break
                        elif op_binario == 1:
                            converter_binario_para_decimal(cor, data_formatada)
                        elif op_binario == 2:
                            converter_binario_para_octal(cor, data_formatada)
                        elif op_binario == 3:
                            converter_binario_para_hexadecimal(cor, data_formatada)
                        else:
                            print(f'{cor["vermelho"]}❌ ENTRADA INVÁLIDA!\n{cor["limpa"]}{cor["branco"]}DIGITE {cor["verde"]}[1-3]{cor["limpa"]} ou {cor["vermelho"]}[0]{cor["limpa"]} PARA VOLTAR.')
                            print(); input(f'{cor["branco"]}PRESSIONE ENTER PARA CONTINUAR...{cor["limpa"]}')

                elif opcao == 3:  # * Menu de conversões octal
                    while True:
                        limpatela()
                        print(data_formatada)
                        print(titulo_octal)
                        print(menu_octal)
                        print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                        op_octal_str = str(input(f'{cor["branco"]}Digite sua opção [DIGITE 0 PARA O MENU ANTERIOR]: {cor["limpa"]}')).strip()
                        print()

                        if not op_octal_str.isdigit():
                            print(f'{cor["vermelho"]}❌ ENTRADA INVÁLIDA!\n{cor["limpa"]}{cor["amarelo"]}UTILIZE APENAS NÚMEROS.{cor["limpa"]}')
                            print(); input(f'{cor["branco"]}PRESSIONE ENTER PARA CONTINUAR...{cor["limpa"]}')
                            continue

                        op_octal = int(op_octal_str)
                        
                        if op_octal == 0:
                            break
                        elif op_octal == 1:
                            converter_de_octal_para_decimal(cor, data_formatada)
                        elif op_octal == 2:
                            converter_octal_para_binario(cor, data_formatada)
                        elif op_octal == 3:
                            converter_octal_para_hexadecimal(cor, data_formatada)
                        else:
                            print(f'{cor["vermelho"]}❌ ENTRADA INVÁLIDA!\n{cor["limpa"]}{cor["branco"]}DIGITE {cor["verde"]}[1-3]{cor["limpa"]} ou {cor["vermelho"]}[0]{cor["limpa"]} PARA VOLTAR.')
                            print(); input(f'{cor["branco"]}PRESSIONE ENTER PARA CONTINUAR...{cor["limpa"]}')

                elif opcao == 4:  # * Menu de conversões hexadecimal
                    while True:
                        limpatela()
                        print(data_formatada)
                        print(titulo_hexadecimal)
                        print(menu_hexadecimal)
                        print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                        op_hexadecimal_str = str(input(f'{cor["branco"]}Digite sua opção [DIGITE 0 PARA O MENU ANTERIOR]: {cor["limpa"]}')).strip()
                        print()

                        if not op_hexadecimal_str.isdigit():
                            print(f'{cor["vermelho"]}❌ ENTRADA INVÁLIDA!\n{cor["limpa"]}{cor["amarelo"]}UTILIZE APENAS NÚMEROS.{cor["limpa"]}')
                            print(); input(f'{cor["branco"]}PRESSIONE ENTER PARA CONTINUAR...{cor["limpa"]}')
                            continue

                        op_hexadecimal = int(op_hexadecimal_str)
                        
                        if op_hexadecimal == 0:
                            break
                        elif op_hexadecimal == 1:
                            converter_hexadecimal_para_decimal(cor, data_formatada)
                        elif op_hexadecimal == 2:
                            converter_hexadecimal_para_binario(cor, data_formatada)
                        elif op_hexadecimal == 3:
                            converter_hexadecimal_para_octal(cor, data_formatada)
                        else:
                            print(f'{cor["vermelho"]}❌ ENTRADA INVÁLIDA!\n{cor["limpa"]}{cor["branco"]}DIGITE {cor["verde"]}[1-3]{cor["limpa"]} ou {cor["vermelho"]}[0]{cor["limpa"]} PARA VOLTAR.')
                            print(); input(f'{cor["branco"]}PRESSIONE ENTER PARA CONTINUAR...{cor["limpa"]}')
                else:
                    print(f'{cor["vermelho"]}❌ ENTRADA INVÁLIDA!\n{cor["limpa"]}{cor["branco"]}DIGITE {cor["verde"]}[1-4]{cor["limpa"]} ou {cor["vermelho"]}[0]{cor["limpa"]} PARA VOLTAR.')
                    print(); input(f'{cor["branco"]}PRESSIONE ENTER PARA CONTINUAR...{cor["limpa"]}')

        elif escolhido == 2: # * OPÇÃO 2 - NOMES EM BINARIOS
            conversor_de_nomes(cor, data_formatada)

        elif escolhido == 3: # * OPÇÃO 3 – OPERAÇÕES BINÁRIAS
            calculos_binarios(cor, data_formatada)

        elif escolhido == 4: # * OPÇÃO 4 – TABELA VERDADE
           tabela_verdade(cor, data_formatada)

        elif escolhido == 5:  # * Opção 5 – EXPRESSÕES BOOLEANAS
           expressoes_booleanas(cor, data_formatada)

        elif escolhido == 6:  # * Opção 6 – MAPA DE KARNAUGH
            mapa_karnaugh(cor, data_formatada)
            
    if escolhido != 0:
        print()

    print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
    print(f"{cor['verde']}{'── FIM DO PROGRAMA ──────────────────────────':^25}{cor['limpa']}")
    
except KeyboardInterrupt:
    print()
    print(f'\n{cor["amarelo"]}ENCERRADO PELO USUÁRIO {cor["limpa"]}')
    input(f'{cor["branco"]}PRESSIONE ENTER PARA SAIR...{cor["limpa"]}')
except EOFError:
    print()
    print(f'\n{cor["amarelo"]}ENCERRADO PELO USUÁRIO.{cor["limpa"]}')
    input(f'{cor["branco"]}PRESSIONE ENTER PARA SAIR...{cor["limpa"]}')
