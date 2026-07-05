from funcoes.funcoes import limpatela, perguntar_continuar

def converter_binario_para_decimal(cor, data_formatada):
     titulo_binario_para_decimal = (  # * Título para a opção de conversão binária para decimal.
    f'{cor["ciano"]}  BINÁRIOS = DECIMAL   {cor["limpa"]}\n'
    f'{cor["branco"]}═══════════════════════{cor["limpa"]}'
    )
     while True:
        limpatela()
        print(data_formatada)
        print()
        print(titulo_binario_para_decimal)
        binario = input(
            f'{cor["branco"]}Digite um valor em binário: {cor["limpa"]}'
        )
        if all(c in "01" for c in binario) and len(binario) > 0:
            decimal = int(binario, 2)
            binario_str = str(binario)
            binario_str = binario_str.replace("1", "V").replace("0", "F")
            binario_colorido = binario_str.replace(
                "F", f'{cor["vermelho"]}0{cor["limpa"]}'
            ).replace("V", f'{cor["verde"]}1{cor["limpa"]}')

            print(
                f'{cor["verde"]}VALOR BINÁRIO{cor["limpa"]}: {binario_colorido}\n'
                f'{cor["verde"]}VALOR INTEIRO{cor["limpa"]}{cor["branco"]}: {decimal}{cor["limpa"]}'
            )
            print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
            if not perguntar_continuar(cor, data_formatada, mensagem="Deseja realizar outra conversão?"):
                break # * Fim do loop de conversão binario para decimal
        else:
            print(
                f'{cor["vermelho"]}OPÇÃO INVALIDA! TENTE NOVAMENTE.{cor["limpa"]}'
            )
            print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
            print()
            input(
                f'{cor["branco"]}PRESSIONE ENTER PARA CONTINUAR...{cor["limpa"]}'
            )
            continue  # * Fim do loop de conversão binario para decimal
def converter_binario_para_octal(cor, data_formatada):
    titulo_binario_para_octal = (  # * Título para a opção de conversão binária para octal.
    f'{cor["ciano"]}  BINÁRIOS = OCTAL   {cor["limpa"]}\n'
    f'{cor["branco"]}═══════════════════════{cor["limpa"]}'
    )
    while True:
        limpatela()
        print(data_formatada)
        print()
        print(titulo_binario_para_octal)
        binario = input(
            f'{cor["branco"]}Digite um valor em binário: {cor["limpa"]}'
        )
        binario_manipulado = binario.replace("1", "V").replace("0", "F")
        binario_colorido = binario_manipulado.replace(
            "F", f'{cor["vermelho"]}0{cor["limpa"]}'
        ).replace("V", f'{cor["verde"]}1{cor["limpa"]}')

        if all(c in "01" for c in binario) and len(binario) > 0:
            decimal = int(binario, 2)
            octal = oct(decimal)
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
                f'{cor["verde"]}VALOR BINÁRIO{cor["limpa"]}: {binario_colorido}\n'
                f'{cor["verde"]}VALOR OCTAL:{cor["limpa"]} {octal_colorido}'
            )
            print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
            if not perguntar_continuar(cor, data_formatada):
                break
        else:
            print(
                f'{cor["vermelho"]}OPÇÃO INVALIDA! TENTE NOVAMENTE.{cor["limpa"]}'
            )
            print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
            print()
            input(
                f'{cor["branco"]}PRESSIONE ENTER PARA CONTINUAR...{cor["limpa"]}'
            )
            continue  # * Fim do loop de conversão binario para octal
def converter_binario_para_hexadecimal(cor, data_formatada):
    titulo_binario_para_hexadecimal = (  # * Título para a opção de conversão binária para hexadecimal.
    f'{cor["ciano"]}  BINÁRIOS = HEXADECIMAL{cor["limpa"]}\n'
    f'{cor["branco"]}═══════════════════════════{cor["limpa"]}'
    )
    while True:
        limpatela()
        print(data_formatada)
        print()
        print(titulo_binario_para_hexadecimal)
        binario = input(
            f'{cor["branco"]}Digite um valor em binário: {cor["limpa"]}'
        )
        binario_manipulado = binario.replace("1", "V").replace("0", "F")
        binario_colorido = binario_manipulado.replace(
            "F", f'{cor["vermelho"]}0{cor["limpa"]}'
        ).replace("V", f'{cor["verde"]}1{cor["limpa"]}')

        if all(c in "01" for c in binario) and len(binario) > 0:
            decimal = int(binario, 2)
            hexadecimal = hex(decimal)
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
                f'{cor["verde"]}VALOR BINÁRIO{cor["limpa"]}: {binario_colorido}\n'
                f'{cor["verde"]}VALOR HEXADECIMAL:{cor["limpa"]} {hexadecimal_colorido}'
            )
            print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
            if not perguntar_continuar(cor, data_formatada):
                break
        else:
            print(
                f'{cor["vermelho"]}OPÇÃO INVALIDA! TENTE NOVAMENTE.{cor["limpa"]}'
            )
            print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
            print()
            input(
                f'{cor["branco"]}PRESSIONE ENTER PARA CONTINUAR...{cor["limpa"]}'
            )
            continue  # * Fim do loop de conversão binario para hexadecimal