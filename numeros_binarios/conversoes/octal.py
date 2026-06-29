from funcoes.funcoes import limpatela, perguntar_continuar

def converter_de_octal_para_decimal(cor, data_formatada):
    titulo_octal_para_decimal = (  # * Título para a opção de conversão octal para decimal.
    f'{cor["ciano"]}    OCTAL = DECIMAL   {cor["limpa"]}\n'
    f'{cor["branco"]}═══════════════════════{cor["limpa"]}'
    )
    while True:
        limpatela()
        print(data_formatada)
        print()
        print(titulo_octal_para_decimal)
        octal = input(
            f'{cor["branco"]}Digite um valor em octal: {cor["limpa"]}'
        ).lower()
        if len(octal) == 0 or not all(c in "01234567o" for c in octal):
            print(
                f'{cor["vermelho"]}OPÇÃO INVALIDA! TENTE NOVAMENTE.{cor["limpa"]}'
            )
            print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
            print()
            input(
                f'{cor["branco"]}PRESSIONE ENTER PARA CONTINUAR...{cor["limpa"]}'
            )
            continue
        elif octal[0:2] == 'o0':
            print()
            print(
                f'{cor["vermelho"]}OPERAÇÃO INVALIDA!{cor["limpa"]}\n{cor["amarelo"]}COLOQUE O '
                f'PREFIXO{cor["limpa"]} {cor['vermelho']}"0"{cor['limpa']}{cor["amarelo"]} '
                f'ANTES DO{cor['limpa']} {cor['azul']}"o"{cor['limpa']}.'
            )
            print()
            input(
                f'{cor["branco"]}PRESSIONE ENTER PARA CONTINUAR...{cor["limpa"]}'
            )
            continue
        elif octal[0:2] != '0o':
            print()
            print(f'{cor['vermelho']}ERRO!{cor['limpa']}\n'
                    f'{cor['amarelo']}COLOQUE O PREFIXO "{cor['limpa']}'
                    f'{cor['vermelho']}0{cor['limpa']}{cor['azul']}o{cor['limpa']}'
                    f'{cor['amarelo']}" ANTES DOS NÚMEROS!{cor['limpa']}')
            print()
            input(f'{cor["branco"]}PRESSIONE ENTER PARA CONTINUAR...{cor["limpa"]}')
            continue
        else:
            try:
                decimal = int(octal, 8)
                octal_str = str(octal)
                octal_colorido = ""
                for i, char in enumerate(octal_str):
                    if char == "0":
                        octal_colorido += (
                            f'{cor["vermelho"]}0{cor["limpa"]}'
                        )
                    elif char == "1":
                        octal_colorido += f'{cor["verde"]}1{cor["limpa"]}'
                    else:
                        octal_colorido += (
                            f'{cor["azul"]}{char}{cor["limpa"]}'
                        )
                print(
                    f'{cor["verde"]}VALOR OCTAL{cor["limpa"]}: {octal_colorido}\n'
                    f'{cor["verde"]}VALOR INTEIRO{cor["limpa"]}{cor["branco"]}: {decimal}{cor["limpa"]}'
                )
                print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                if not perguntar_continuar(cor, data_formatada):
                    break # * Fim do loop de conversão octal para decimal
            except ValueError:
                print()
                print(f'{cor['vermelho']}PROBLEMA NO PROCESSAMENTO DA CONVERSÃO!{cor['limpa']}\n'
                      f'{cor['amarelo']}COLOQUE NÚMEROS APÓS O PREFIXO.{cor['limpa']}')
                print()
                input(f'{cor['branco']}PRESSIONE ENTER PARA DIGITAR UM NOVO VALOR...{cor['limpa']}')
                continue
def converter_octal_para_binario(cor, data_formatada):
    titulo_octal_para_binario = (  # * Título para a opção de conversão octal para binário.
    f'{cor["ciano"]}    OCTAL = BINÁRIO   {cor["limpa"]}\n'
    f'{cor["branco"]}═══════════════════════{cor["limpa"]}'
    )
    while True:
        limpatela()
        print(data_formatada)
        print()
        print(titulo_octal_para_binario)
        octal_str = input(
            f'{cor["branco"]}Digite um valor em octal: {cor["limpa"]}'
        ).lower()
        if len(octal_str) == 0 or not all(c in "01234567o" for c in octal_str):
            print(f'{cor["vermelho"]}OPÇÃO INVALIDA! TENTE NOVAMENTE.{cor["limpa"]}')
            print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
            print()
            input(f'{cor["branco"]}PRESSIONE ENTER PARA CONTINUAR...{cor["limpa"]}')
            continue
        
        elif octal_str[0:2] == 'o0':
            print()
            print(f'{cor["vermelho"]}OPERAÇÃO INVALIDA!{cor["limpa"]}\n{cor["amarelo"]}COLOQUE O '
                    f'PREFIXO{cor["limpa"]} {cor['vermelho']}"0"{cor['limpa']}{cor["amarelo"]} '
                    f'ANTES DO{cor['limpa']} {cor['azul']}"o"{cor['limpa']}.'
                )
            print()
            input(f'{cor["branco"]}PRESSIONE ENTER PARA CONTINUAR...{cor["limpa"]}'
            )
            continue
        elif octal_str[0:2] != '0o':
            print()
            print(f'{cor['vermelho']}ERRO!{cor['limpa']}\n'
                f'{cor['amarelo']}COLOQUE O PREFIXO "{cor['limpa']}'
                f'{cor['vermelho']}0{cor['limpa']}{cor['azul']}o{cor['limpa']}'
                f'{cor['amarelo']}" ANTES DOS NÚMEROS!{cor['limpa']}')
            print()
            input(
                f'{cor["branco"]}PRESSIONE ENTER PARA CONTINUAR...{cor["limpa"]}'
            )
            continue
        else:
            try:
                decimal = int(octal_str, 8)
                binario = bin(decimal)
                binario_str = str(binario[2:])
                binario_str = binario_str.replace("1", "V").replace(
                    "0", "F"
                )
                binario_colorido = binario_str.replace(
                    "F", f'{cor["vermelho"]}0{cor["limpa"]}'
                ).replace("V", f'{cor["verde"]}1{cor["limpa"]}')
                octal_colorido = ""
                for i, char in enumerate(octal_str):
                    if char == "0":
                        octal_colorido += (
                            f'{cor["vermelho"]}0{cor["limpa"]}'
                        )
                    elif char == "1":
                        octal_colorido += f'{cor["verde"]}1{cor["limpa"]}'
                    else:
                        octal_colorido += (
                            f'{cor["azul"]}{char}{cor["limpa"]}'
                        )
                print(
                    f'{cor["verde"]}VALOR OCTAL{cor["limpa"]}: {octal_colorido}\n'
                    f'{cor["verde"]}VALOR BINÁRIO:{cor["limpa"]} {binario_colorido}'
                )
                print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                if not perguntar_continuar(cor, data_formatada):
                    break # * Fim do loop de conversão octal para binario
            except ValueError:      
                print()
                print(f'{cor["vermelho"]}PROBLEMA NO PROCESSAMENTO DA CONVERSÃO!{cor["limpa"]}\n'
                      f'{cor["amarelo"]}COLOQUE NÚMEROS APÓS O PREFIXO.{cor["limpa"]}')
                print()
                input(f'{cor["branco"]}PRESSIONE ENTER PARA DIGITAR UM NOVO VALOR...{cor["limpa"]}')
                continue
def converter_octal_para_hexadecimal(cor, data_formatada):
    titulo_octal_para_hexadecimal = (  # * Título para a opção de conversão octal para hexadecimal.
        f'{cor["ciano"]}    OCTAL = HEXADECIMAL{cor["limpa"]}\n'
        f'{cor["branco"]}═══════════════════════════{cor["limpa"]}'
    )
    while True:
        limpatela()
        print(data_formatada)
        print()
        print(titulo_octal_para_hexadecimal)
        octal_str = input(
                    f'{cor["branco"]}Digite um valor em octal: {cor["limpa"]}'
                ).lower()
        if len(octal_str) == 0 or not all(c in "01234567o" for c in octal_str):
            print(
                f'{cor["vermelho"]}OPÇÃO INVALIDA! TENTE NOVAMENTE.{cor["limpa"]}'
            )
            print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
            print()
            input(
                f'{cor["branco"]}PRESSIONE ENTER PARA CONTINUAR...{cor["limpa"]}'
            )
            continue  # * Fim do loop de conversão octal para hexadecimal
        elif octal_str[0:2] == 'o0':
            print()
            print(f'{cor["vermelho"]}OPERAÇÃO INVALIDA!{cor["limpa"]}\n{cor["amarelo"]}COLOQUE O '
                f'PREFIXO{cor["limpa"]} {cor['vermelho']}"0"{cor['limpa']}{cor["amarelo"]} '
                f'ANTES DO{cor['limpa']} {cor['azul']}"o"{cor['limpa']}.'
                )
            print()
            input(f'{cor["branco"]}PRESSIONE ENTER PARA CONTINUAR...{cor["limpa"]}'
            )
            continue
        elif octal_str[0:2] != '0o':
            print()
            print(f'{cor['vermelho']}ERRO!{cor['limpa']}\n'
                f'{cor['amarelo']}COLOQUE O PREFIXO "{cor['limpa']}'
                f'{cor['vermelho']}0{cor['limpa']}{cor['azul']}o{cor['limpa']}'
                f'{cor['amarelo']}" ANTES DOS NÚMEROS!{cor['limpa']}')
            print()
            input(
                f'{cor["branco"]}PRESSIONE ENTER PARA CONTINUAR...{cor["limpa"]}'
            )
            continue
        else:
            try:
                decimal = int(octal_str, 8)
                hexadecimal = hex(decimal)
                hexadecimal_str = str(hexadecimal)
                hexadecimal_colorido = ""
                for i, char in enumerate(hexadecimal_str):
                    if i == 1:
                        hexadecimal_colorido += (
                            f'{cor["roxo"]}x{cor["limpa"]}'
                        )
                    elif char == "0" and i == 0:
                        hexadecimal_colorido += (
                            f'{cor["vermelho"]}0{cor["limpa"]}'
                        )
                    elif char == "1":
                        hexadecimal_colorido += (
                            f'{cor["verde"]}1{cor["limpa"]}'
                        )
                    elif char == "0":
                        hexadecimal_colorido += (
                            f'{cor["vermelho"]}0{cor["limpa"]}'
                        )
                    else:
                        hexadecimal_colorido += (
                            f'{cor["roxo"]}{char}{cor["limpa"]}'
                        )
                octal_colorido = ""
                for i, char in enumerate(octal_str):
                    if char == "0":
                        octal_colorido += (
                            f'{cor["vermelho"]}0{cor["limpa"]}'
                        )
                    elif char == "1":
                        octal_colorido += f'{cor["verde"]}1{cor["limpa"]}'
                    else:
                        octal_colorido += (
                            f'{cor["azul"]}{char}{cor["limpa"]}'
                        )
                print(
                    f'{cor["verde"]}VALOR OCTAL{cor["limpa"]}: {octal_colorido}\n'
                    f'{cor["verde"]}VALOR HEXADECIMAL:{cor["limpa"]} {hexadecimal_colorido}'
                )
                print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                if not perguntar_continuar(cor, data_formatada):
                    break
            except ValueError:
                print()
                print(f'{cor["vermelho"]}PROBLEMA NO PROCESSAMENTO DA CONVERSÃO!{cor["limpa"]}\n'
                      f'{cor["amarelo"]}COLOQUE NÚMEROS APÓS O PREFIXO.{cor["limpa"]}')
                print()
                input(f'{cor["branco"]}PRESSIONE ENTER PARA DIGITAR UM NOVO VALOR...{cor["limpa"]}')
                continue
