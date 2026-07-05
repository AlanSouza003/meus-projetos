import ttg
from time import sleep
from funcoes.funcoes import limpatela, perguntar_continuar

def tabela_verdade(cor, data_formatada):
    proposicoes_disponiveis = ["a", "b", "c", "d"]
    
    while True:
        limpatela()
        print(data_formatada)
        print()
        
        # menu de escolha
        while True:
            print(f'{cor["roxo"]}QUANTAS PROPOSIÇÕES DESEJA?{cor["limpa"]}')
            print(f'{cor["verde"]}[ 1 ]{cor["limpa"]} {cor["branco"]}UMA PROPOSIÇÃO: ["a"]{cor["limpa"]}')
            print(f'{cor["verde"]}[ 2 ]{cor["limpa"]} {cor["branco"]}DUAS PROPOSIÇÕES: ["a", "b"]{cor["limpa"]}')
            print(f'{cor["verde"]}[ 3 ]{cor["limpa"]} {cor["branco"]}TRÊS PROPOSIÇÕES: ["a", "b", "c"]{cor["limpa"]}')
            print(f'{cor["verde"]}[ 4 ]{cor["limpa"]} {cor["branco"]}QUATRO PROPOSIÇÕES: ["a", "b", "c", "d"]{cor["limpa"]}')
            print(f'{cor["vermelho"]}[ 0 ]{cor["limpa"]} {cor["branco"]}VOLTAR AO MENU PRINCIPAL{cor["limpa"]}')
            print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
            escolha_str = input(f'{cor["roxo"]}DIGITE AQUI: {cor["limpa"]}').strip()

            if not escolha_str.isdigit():
                print(f'{cor["vermelho"]}UTILIZE APENAS NÚMEROS.{cor["limpa"]}')
                input(f'{cor["branco"]}PRESSIONE ENTER PARA CONTINUAR...{cor["limpa"]}')
                limpatela()
                print(data_formatada)
                print()
                continue

            escolha = int(escolha_str)

            if escolha == 0:
                return  
            elif 1 <= escolha <= 4:
                break
            else:
                print(f'{cor["vermelho"]}VALOR INVÁLIDO! UTILIZE VALORES DE 1 ATÉ 4\n'
                      f'{cor["vermelho"]}OU 0 PARA RETORNAR PARA O MENU PRINCIPAL{cor["limpa"]}')
                input(f'{cor["branco"]}PRESSIONE ENTER PARA CONTINUAR...{cor["limpa"]}')
                limpatela()
                print(data_formatada)
                print()
                continue

        props = proposicoes_disponiveis[:escolha]
        
        print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
        for c in range(4):
            print(f'\r\033[1;95m{"PROCESSANDO" + "." * c:^25}\033[0m', end="", flush=True)
            sleep(1.5)
        print()
        print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
        print(f'{cor["verde"]}RESULTADO{cor["limpa"]}')

        tabela = ttg.Truths(props, ascending=True)
        tabela_str = str(tabela).replace("1", "V").replace("0", "F")
        
        tabela_colorida = (
            tabela_str
            .replace("F", f'{cor["vermelho"]}0{cor["limpa"]}')
            .replace("V", f'{cor["verde"]}1{cor["limpa"]}')
            .replace("|", f'{cor["amarelo"]}|{cor["limpa"]}')
            .replace("+", f'{cor["amarelo"]}+{cor["limpa"]}')
            .replace("-", f'{cor["ciano"]}-{cor["limpa"]}')
        )
        for p in props:
            tabela_colorida = tabela_colorida.replace(p, f'{cor["branco"]}{p}{cor["limpa"]}')

        print(tabela_colorida)
        print(f'{cor["branco"]}─{cor["limpa"]}' * 25)

        if not perguntar_continuar(cor, data_formatada, "DESEJA VISUALIZAR OUTRA TABELA?", "SAINDO DA TABELA VERDADE"):
            break