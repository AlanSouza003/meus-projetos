import ttg
from time import sleep
from funcoes.funcoes import limpatela, perguntar_continuar, barra_processando

def expressoes_booleanas(cor, data_formatada):
    proposicoes_disponiveis = ["a", "b", "c", "d"]

    def colorir_tabela_booleana(tabela_str, props):
        resultado = (
            tabela_str
            .replace("F", f'{cor["vermelho"]}0{cor["limpa"]}')
            .replace("V", f'{cor["verde"]}1{cor["limpa"]}')
            .replace("|", f'{cor["amarelo"]}|{cor["limpa"]}')
            .replace("+", f'{cor["amarelo"]}+{cor["limpa"]}')
            .replace("-", f'{cor["ciano"]}-{cor["limpa"]}')
            .replace("not", f'{cor["vermelho"]}not{cor["limpa"]}')
            .replace("and", f'{cor["branco"]}and{cor["limpa"]}')
            .replace("or", f'{cor["branco"]}or{cor["limpa"]}')
            .replace("(", f'{cor["branco"]}({cor["limpa"]}')
            .replace(")", f'{cor["branco"]}){cor["limpa"]}')
        )
        for p in props:
            resultado = resultado.replace(p, f'{cor["branco"]}{p}{cor["limpa"]}')
        return resultado

    while True:
        try:
            limpatela()
            print(data_formatada)
            print()
            print(f'{cor["ciano"]}{"EXPRESSÕES BOOLEANAS":^25}{cor["limpa"]}')
            print(f'{cor["branco"]}─{cor["limpa"]}' * 25)

            while True:
                valor1 = input(f'{cor["branco"]}Primeira Proposição (a-d): {cor["limpa"]}').lower().strip()
                valor2 = input(f'{cor["branco"]}Segunda Proposição (a-d): {cor["limpa"]}').lower().strip()
                if valor1 in proposicoes_disponiveis and valor2 in proposicoes_disponiveis:
                    break
                print(f'{cor["vermelho"]}VALOR INVÁLIDO! COLOQUE LETRAS DE A ATÉ D.{cor["limpa"]}')
                print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                input(f'{cor["branco"]}PRESSIONE ENTER PARA CONTINUAR...{cor["limpa"]}')
                limpatela()
                print(data_formatada)
                print()
                print(f'{cor["ciano"]}{"EXPRESSÕES BOOLEANAS":^25}{cor["limpa"]}')
                print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                continue

            while True:
                funcao0 = input(f'{cor["branco"]}Qual o Operador? (and/&&/or/||): {cor["limpa"]}').lower().strip()
                if funcao0 == "&&":
                    funcao = "and"
                    break
                elif funcao0 == "||":
                    funcao = "or"
                    break
                elif funcao0 in ["and", "or"]:
                    funcao = funcao0
                    break
                print(f'{cor["vermelho"]}OPÇÃO INVÁLIDA! USE: and, &&, or, ||{cor["limpa"]}')
                input(f'{cor["branco"]}PRESSIONE ENTER PARA CONTINUAR...{cor["limpa"]}')
                print("\033[3A\033[J", end="")
                continue

            while True:
                neg = input(f'{cor["branco"]}Está negativado? (S/N): {cor["limpa"]}').upper().strip()
                if neg not in ["S", "SIM", "N", "NÃO", "NAO"]:
                    print(f'{cor["vermelho"]}OPÇÃO INVÁLIDA! TENTE NOVAMENTE.{cor["limpa"]}')
                    print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                    input(f'{cor["branco"]}PRESSIONE ENTER PARA CONTINUAR...{cor["limpa"]}')
                    print("\033[4A\033[J", end="")
                    continue
                if neg in ["S", "SIM", "N", "NÃO", "NAO"]:
                    break
            while True:
                tabela_ate = input(f'{cor["branco"]}Até que proposição deseja ir? (b/c/d): '
                                    f'{cor["limpa"]}').lower().strip()
                if tabela_ate not in ["b", "c", "d"]:
                    print(f'{cor["vermelho"]}OPÇÃO INVÁLIDA! TENTE NOVAMENTE.\n'
                          f'{cor["vermelho"]}DIGITE DE B ATÉ D.{cor["limpa"]}')
                    print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
                    input(f'{cor["branco"]}PRESSIONE ENTER PARA CONTINUAR...{cor["limpa"]}')
                    # apaga as 3 linhas anteriores (erro + enter + linha do operador)
                    print("\033[5A\033[J", end="")
                    continue
                if tabela_ate in ["b", "c", "d"]:
                    break
            idx = proposicoes_disponiveis.index(tabela_ate)
            props = proposicoes_disponiveis[:idx + 1]

            if neg in ["S", "SIM"]:
                print(f'{cor["amarelo"]}O QUE ESTÁ NEGATIVADO?{cor["limpa"]}')
                print(f'{cor["verde"]}[ 1 ]{cor["limpa"]} {cor["vermelho"]}not ({valor1}){cor["limpa"]} {funcao} {valor2}')
                print(f'{cor["verde"]}[ 2 ]{cor["limpa"]} {valor1} {funcao} {cor["vermelho"]}not ({valor2}){cor["limpa"]}')
                print(f'{cor["verde"]}[ 3 ]{cor["limpa"]} {cor["vermelho"]}not ({valor1} {funcao} {valor2}){cor["limpa"]}')
                print(f'{cor["branco"]}─{cor["limpa"]}' * 25)

                while True:
                    escolha_str = input(f'{cor["roxo"]}DIGITE A OPÇÃO: {cor["limpa"]}').strip()
                    if escolha_str in ["1", "2", "3"]:
                        escolha = int(escolha_str)
                        break
                    print(f'{cor["vermelho"]}OPÇÃO INVÁLIDA! DIGITE 1, 2 OU 3.{cor["limpa"]}')
                    print(f'{cor["branco"]}─{cor["limpa"]}' * 25)

                expressoes = {
                    1: f"(not {valor1}) {funcao} {valor2}",
                    2: f"{valor1} {funcao} (not {valor2})",
                    3: f"not ({valor1} {funcao} {valor2})",
                }
                expressao = expressoes[escolha]
            else:
                expressao = f"{valor1} {funcao} {valor2}"
            print()
            barra_processando(cor)
            print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
            print(f'{cor["verde"]}RESULTADO{cor["limpa"]}')

            tabela_obj = ttg.Truths(props, [expressao], ascending=True)
            tabela_str = str(tabela_obj).replace("1", "V").replace("0", "F")
            tabela_colorida = colorir_tabela_booleana(tabela_str, props)
            print(tabela_colorida)
            print(f'{cor["branco"]}─{cor["limpa"]}' * 25)

            if not perguntar_continuar(cor, data_formatada, "DESEJA CALCULAR OUTRA EXPRESSÃO?", 
                                    "SAINDO DAS EXPRESSÕES BOOLEANAS"):
                break

        except TypeError:
            print(f'{cor["vermelho"]}ERRO AO CALCULAR A EXPRESSÃO! TENTE NOVAMENTE.{cor["limpa"]}')
            print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
            input(f'{cor["branco"]}PRESSIONE ENTER PARA CONTINUAR...{cor["limpa"]}')
            continue