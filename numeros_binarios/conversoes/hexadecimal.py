from funcoes.funcoes import limpatela, perguntar_continuar

def converter_hexadecimal_para_decimal(cor, data_formatada):
    titulo_hexadecimal_para_decimal = (  # * Título para a opção de conversão hexadecimal para decimal.
        f'{cor["ciano"]}   HEXADECIMAL = DECIMAL   {cor["limpa"]}\n'
        f'{cor["branco"]}═══════════════════════════{cor["limpa"]}'
    )
    while True:
        limpatela()
        print(data_formatada)
        print()
        print(titulo_hexadecimal_para_decimal)
        hexadecimal = input(
            f'{cor["branco"]}Digite um valor em hexadecimal: {cor["limpa"]}'
        ).lower()
        if len(hexadecimal) == 0 or not all(c in "0123456789ABCDEFabcdefx" for c in hexadecimal):
            print(
                f'{cor["vermelho"]}ERRO!{cor["limpa"]}\n'
                f'{cor["amarelo"]}OPERAÇÃO INVÁLIDA! TENTE NOVAMENTE.{cor["limpa"]}'
            )
            print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
            input(
                f'{cor["branco"]}PRESSIONE ENTER PARA CONTINUAR...{cor["limpa"]}'
            )
            continue
        elif hexadecimal[0:2] != '0x':
            print()
            print(
                f'{cor["vermelho"]}ERRO!{cor["limpa"]}\n'
                f'{cor["amarelo"]}COLOQUE O PREFIXO CORRETO "{cor["limpa"]}'
                f'{cor["vermelho"]}0{cor["limpa"]}{cor["roxo"]}x{cor["limpa"]}'
                f'{cor["amarelo"]}" ANTES DOS NÚMEROS!{cor["limpa"]}'
            )
            print()
            input(f'{cor["branco"]}PRESSIONE ENTER PARA CONTINUAR...{cor["limpa"]}')
            continue
        else:
            try:
                decimal = int(hexadecimal, 16)
                hexadecimal_str = str(hexadecimal)
                hexadecimal_colorido = ""
                for i, char in enumerate(hexadecimal_str):
                    if char == "0":
                        hexadecimal_colorido += (
                            f'{cor["vermelho"]}0{cor["limpa"]}'
                        )
                    elif char == "1":
                        hexadecimal_colorido += (
                            f'{cor["verde"]}1{cor["limpa"]}'
                        )
                    else:
                        hexadecimal_colorido += (
                            f'{cor["roxo"]}{char}{cor["limpa"]}'
                        )
                print(
                    f'{cor["verde"]}VALOR HEXADECIMAL{cor["limpa"]}: {hexadecimal_colorido}\n'
                    f'{cor["verde"]}VALOR INTEIRO{cor["limpa"]}{cor["branco"]}: {decimal}{cor["limpa"]}'
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
def converter_hexadecimal_para_binario(cor, data_formatada):
    titulo_hexadecimal_para_binario = (  # * Título para a opção de conversão hexadecimal para binário.
        f'{cor["ciano"]}    HEXADECIMAL = BINÁRIO   {cor["limpa"]}\n'
        f'{cor["branco"]}═══════════════════════════{cor["limpa"]}'
    )
    while True:
        limpatela()
        print(data_formatada)
        print()
        print(titulo_hexadecimal_para_binario)
        hexadecimal_str = input(
            f'{cor["branco"]}Digite um valor em hexadecimal: {cor["limpa"]}'
        ).lower()
        if len(hexadecimal_str) == 0 or not all(c in "0123456789ABCDEFabcdefx" for c in hexadecimal_str):
            print(
                f'{cor["vermelho"]}ERRO!{cor["limpa"]}\n'
                f'{cor["amarelo"]}OPERAÇÃO INVÁLIDA! TENTE NOVAMENTE.{cor["limpa"]}'
            )
            print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
            input(
                f'{cor["branco"]}PRESSIONE ENTER PARA CONTINUAR...{cor["limpa"]}'
            )
            continue
        elif hexadecimal_str[0:2] != '0x':
            print()
            print(
                f'{cor["vermelho"]}ERRO!{cor["limpa"]}\n'
                f'{cor["amarelo"]}COLOQUE O PREFIXO CORRETO "{cor["limpa"]}'
                f'{cor["vermelho"]}0{cor["limpa"]}{cor["roxo"]}x{cor["limpa"]}'
                f'{cor["amarelo"]}" ANTES DOS NÚMEROS!{cor["limpa"]}'
            )
            print()
            input(f'{cor["branco"]}PRESSIONE ENTER PARA CONTINUAR...{cor["limpa"]}')
            continue
        else:
            try:
                decimal = int(hexadecimal_str, 16)
                binario = bin(decimal)
                binario_str = str(binario[2:])
                binario_str = binario_str.replace("1", "V").replace(
                    "0", "F"
                )
                binario_colorido = binario_str.replace(
                    "F", f'{cor["vermelho"]}0{cor["limpa"]}'
                ).replace("V", f'{cor["verde"]}1{cor["limpa"]}')
                hexadecimal_colorido = ""
                for i, char in enumerate(hexadecimal_str):
                    if char == "0":
                        hexadecimal_colorido += (
                            f'{cor["vermelho"]}0{cor["limpa"]}'
                        )
                    elif char == "1":
                        hexadecimal_colorido += (
                            f'{cor["verde"]}1{cor["limpa"]}'
                        )
                    else:
                        hexadecimal_colorido += (
                            f'{cor["roxo"]}{char}{cor["limpa"]}'
                        )
                print(
                    f'{cor["verde"]}VALOR HEXADECIMAL{cor["limpa"]}: {hexadecimal_colorido}\n'
                    f'{cor["verde"]}VALOR BINÁRIO:{cor["limpa"]} {binario_colorido}'
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
def converter_hexadecimal_para_octal(cor, data_formatada):
    titulo_hexadecimal_para_octal = (  # * Título para a opção de conversão hexadecimal para octal.
        f'{cor["ciano"]}    HEXADECIMAL = OCTAL   {cor["limpa"]}\n'
        f'{cor["branco"]}═══════════════════════════{cor["limpa"]}'
    )
    while True:
        limpatela()
        print(data_formatada)
        print()
        print(titulo_hexadecimal_para_octal)
        hexadecimal_str = input(
            f'{cor["branco"]}Digite um valor em hexadecimal: {cor["limpa"]}'
        ).lower()
        if  len(hexadecimal_str) == 0 or not all(c in "0123456789ABCDEFabcdefx" for c in hexadecimal_str):
            print(
                f'{cor["vermelho"]}ERRO!{cor["limpa"]}\n'
                f'{cor["amarelo"]}OPERAÇÃO INVÁLIDA! TENTE NOVAMENTE.{cor["limpa"]}'
            )
            print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
            input(
                f'{cor["branco"]}PRESSIONE ENTER PARA CONTINUAR...{cor["limpa"]}'
            )
            continue
        elif hexadecimal_str[0:2] != '0x':
            print()
            print(
                f'{cor["vermelho"]}ERRO!{cor["limpa"]}\n'
                f'{cor["amarelo"]}COLOQUE O PREFIXO CORRETO "{cor["limpa"]}'
                f'{cor["vermelho"]}0{cor["limpa"]}{cor["roxo"]}x{cor["limpa"]}'
                f'{cor["amarelo"]}" ANTES DOS NÚMEROS!{cor["limpa"]}'
            )
            print()
            input(f'{cor["branco"]}PRESSIONE ENTER PARA CONTINUAR...{cor["limpa"]}')
            continue
        else:
            try:
                decimal = int(hexadecimal_str, 16)
                octal = oct(decimal)
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
                hexadecimal_colorido = ""
                for i, char in enumerate(hexadecimal_str):
                    if char == "0":
                        hexadecimal_colorido += (
                            f'{cor["vermelho"]}0{cor["limpa"]}'
                        )
                    elif char == "1":
                        hexadecimal_colorido += (
                            f'{cor["verde"]}1{cor["limpa"]}'
                        )
                    else:
                        hexadecimal_colorido += (
                            f'{cor["roxo"]}{char}{cor["limpa"]}'
                        )
                print(
                    f'{cor["verde"]}VALOR HEXADECIMAL{cor["limpa"]}: {hexadecimal_colorido}\n'
                    f'{cor["verde"]}VALOR OCTAL:{cor["limpa"]} {octal_colorido}'
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