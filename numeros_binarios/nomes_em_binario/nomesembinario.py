from time import sleep

from funcoes.funcoes import perguntar_continuar, limpatela,barra_processando


def nome_para_binario(nome, cor):
    binarios = []
    for letra in nome:
        codigo = ord(letra)
        binario = format(codigo, '08b')
        binarios.append(binario)
    return " ".join(binarios)

def validar_nome(nome):
    if nome == "":
        return "O NOME NÃO PODE FICAR VAZIO!"
    if any(c.isdigit() for c in nome):
        return "NOMES NÃO PODEM CONTER NÚMEROS!"
    if not nome.isalpha():
        return "USE APENAS LETRAS, SEM ESPAÇOS OU SÍMBOLOS!"
    return None


def conversor_de_nomes(cor, data_formatada):
    titulo_nomes_em_binario = (  # * Título para a opção de conversão nomes em binário.
        f'{cor["ciano"]}    NOMES = BINÁRIO   {cor["limpa"]}\n'
        f'{cor["branco"]}═══════════════════════════{cor["limpa"]}'
    )

    try:
        while True:
            limpatela()
            print(data_formatada)
            print()
            print(titulo_nomes_em_binario)
            print(f'{cor["verde"]}■{cor["limpa"]} = 1     {cor["vermelho"]}■{cor["limpa"]} = 0\n')

            nome = str(input("Digite seu nome: "))

            erro = validar_nome(nome)
            if erro:
                print(
                    f'{cor["vermelho"]}ERRO!{cor["limpa"]}\n'
                    f'{cor["amarelo"]}{erro}{cor["limpa"]}'
                )
                print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                input(
                    f'{cor["branco"]}PRESSIONE ENTER PARA CONTINUAR...{cor["limpa"]}'
                )
                continue

            resultado = nome_para_binario(nome, cor)
            resultado_manipulado = resultado.replace("1", "V").replace("0", "F")
            resultado_colorido = resultado_manipulado.replace(
                "F", f'{cor["vermelho"]}0{cor["limpa"]}'
            ).replace("V", f'{cor["verde"]}1{cor["limpa"]}')

            print()
            barra_processando(cor)
            print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
            print(f'{cor["verde"]}RESULTADO{cor["limpa"]}')
            print(f"{cor['branco']}NOME DIGITADO = {nome}{cor['limpa']}")
            print(f"{cor['branco']}NOME EM BINÁRIO ={cor['limpa']} {resultado_colorido}")

            print()
            print(f'{cor["ciano"]}LETRA POR LETRA:{cor["limpa"]}')
            for letra, bits in zip(nome, resultado.split(" ")):
                print(f'  {cor["ciano"]}{letra}{cor["limpa"]} → {cor["verde"]}{bits}{cor["limpa"]}')

            print()
            print(
                f"{cor['branco']}Total de letras: {len(nome)} | "
                f"Total de bits: {len(nome) * 8}{cor['limpa']}"
            )
            print()

            if not perguntar_continuar(
                cor,
                data_formatada,
                "DESEJA CONVERTER OUTRO NOME?",
                "SAINDO DA CONVERSÃO DOS NOMES",
            ):
                break

    except KeyboardInterrupt:
        print(f'\n{cor["amarelo"]}ENCERRADO PELO USUÁRIO.{cor["limpa"]}')
        input(f'{cor["branco"]}PRESSIONE ENTER PARA SAIR...{cor["limpa"]}')
    except EOFError:
        print(f'\n{cor["amarelo"]}ENCERRADO PELO USUÁRIO.{cor["limpa"]}')
        input(f'{cor["branco"]}PRESSIONE ENTER PARA SAIR...{cor["limpa"]}')