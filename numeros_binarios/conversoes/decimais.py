from funcoes.funcoes import limpatela, perguntar_continuar

def converter_de_decimal_binario(cor, data_formatada):
    titulo_decimal_para_binario = (  # * Título para a opção de conversão decimal para binário.
    f'{cor["ciano"]}  DECIMAIS = BINÁRIO   {cor["limpa"]}\n'
    f'{cor["branco"]}═══════════════════════{cor["limpa"]}'
    )
    while True:
        limpatela()
        print(data_formatada)
        print()
        print(titulo_decimal_para_binario)
        valor_str = str(
            input(f'{cor["branco"]}Digite um valor inteiro: {cor["limpa"]}')
        )

        if valor_str.isdigit():
            valor = int(valor_str)
            binario = bin(valor)
            binario_str = str(binario[2:])
            binario_str = binario_str.replace("1", "V").replace("0", "F")
            binario_colorido = binario_str.replace(
                "F", f'{cor["vermelho"]}0{cor["limpa"]}'
            ).replace("V", f'{cor["verde"]}1{cor["limpa"]}')

            print(
                f'{cor["verde"]}VALOR INTEIRO{cor["limpa"]}{cor["branco"]}: {valor}{cor["limpa"]}\n'
                f'{cor["verde"]}VALOR BINÁRIO:{cor["limpa"]} {binario_colorido}'
            )
            print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
        else:
            print(
                f'{cor["vermelho"]}ERRO NA CONVERSÃO! TENTE NOVAMENTE.{cor["limpa"]}'
            )
            print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
            print()
            input(
                f'{cor["branco"]}PRESSIONE ENTER PARA CONTINUAR...{cor["limpa"]}'
            )
            continue 
        if not perguntar_continuar(cor, data_formatada):
            break # * Fim do loop de conversão decimal para binário
def converter_de_decimal_octal(cor, data_formatada):
    titulo_decimal_para_octal = (  # * Título para a opção de conversão decimal para octal.
    f'{cor["ciano"]}  DECIMAIS = OCTAL   {cor["limpa"]}\n'
    f'{cor["branco"]}═══════════════════════{cor["limpa"]}'
    )
    while True:
        limpatela()
        print(data_formatada)
        print()
        print(titulo_decimal_para_octal)
        valor_str = str(
            input(f'{cor["branco"]}Digite um valor inteiro: {cor["limpa"]}')
        )

        if valor_str.isdigit():
            valor = int(valor_str)
            octal = oct(valor)
            octal_str = str(octal)
            octal_colorido = ""
            for i, char in enumerate(octal_str):
                if i == 1:
                    octal_colorido += f'{cor["azul"]}o{cor["limpa"]}'
                elif char == "0" and i == 0:
                    octal_colorido += f'{cor["vermelho"]}0{cor["limpa"]}'
                elif char == "1":
                    octal_colorido += f'{cor["verde"]}1{cor["limpa"]}'
                elif char == "0":
                    octal_colorido += f'{cor["vermelho"]}0{cor["limpa"]}'
                else:
                    octal_colorido += f'{cor["azul"]}{char}{cor["limpa"]}'
            print(
                f'{cor["verde"]}VALOR INTEIRO{cor["limpa"]}{cor["branco"]}: {valor}{cor["limpa"]}\n'
                f'{cor["verde"]}VALOR OCTAL:{cor["limpa"]} {octal_colorido}'
            )
            print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
        else:
            print(
                f'{cor["vermelho"]}ERRO NA CONVERSÃO! TENTE NOVAMENTE.{cor["limpa"]}'
            )
            print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
            print()
            input(
                f'{cor["branco"]}PRESSIONE ENTER PARA CONTINUAR...{cor["limpa"]}'
            )
            continue  
            
        if not perguntar_continuar(cor, data_formatada):
            break # * Fim do loop de conversão decimal para octal
def converter_de_decimal_hexadecimal(cor, data_formatada):
     titulo_decimal_para_hexadecimal = (  # * Título para a opção de conversão decimal para hexadecimal.
    f'{cor["ciano"]}  DECIMAIS = HEXADECIMAL{cor["limpa"]}\n'
    f'{cor["branco"]}═══════════════════════════{cor["limpa"]}'
    )
     while True:
        limpatela()
        print(data_formatada)
        print()
        print(titulo_decimal_para_hexadecimal)
        valor_str = str(
            input(f'{cor["branco"]}Digite um valor inteiro: {cor["limpa"]}')
        )

        if valor_str.isdigit():
            valor = int(valor_str)
            hexadecimal = hex(valor)
            hexadecimal_str = str(hexadecimal)
            hexadecimal_colorido = ""
            for i, char in enumerate(hexadecimal_str):
                if i == 1:
                    hexadecimal_colorido += f'{cor["roxo"]}x{cor["limpa"]}'
                elif char == "0" and i == 0:
                    hexadecimal_colorido += (
                        f'{cor["vermelho"]}0{cor["limpa"]}'
                    )
                elif char == "1":
                    hexadecimal_colorido += f'{cor["verde"]}1{cor["limpa"]}'
                elif char == "0":
                    hexadecimal_colorido += (
                        f'{cor["vermelho"]}0{cor["limpa"]}'
                    )
                else:
                    hexadecimal_colorido += (
                        f'{cor["roxo"]}{char}{cor["limpa"]}'
                    )

            print(
                f'{cor["verde"]}VALOR INTEIRO{cor["limpa"]}{cor["branco"]}: {valor}{cor["limpa"]}\n'
                f'{cor["verde"]}VALOR HEXADECIMAL:{cor["limpa"]} {hexadecimal_colorido}'
            )
            print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
            
        else:
            print(
                 f'{cor["vermelho"]}ERRO NA CONVERSÃO! TENTE NOVAMENTE.{cor["limpa"]}'
            )
            print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
            print()
            input(
                f'{cor["branco"]}PRESSIONE ENTER PARA CONTINUAR...{cor["limpa"]}'
            )
            continue 
        if not perguntar_continuar(cor, data_formatada):
            break # * Fim do loop de conversão decimal para hexadecimal
