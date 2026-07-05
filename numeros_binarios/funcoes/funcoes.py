# TODO: FUNÇÕES
import os
from time import sleep

def limpatela():
    return os.system("cls" if os.name == "nt" else "clear")

def perguntar_continuar(cor, data_formatada, mensagem="DESEJA CONTINUAR CONVERTENDO?", mensagem2="SAINDO DA CONVERSÃO"):
    titulo_deseja_continuar = f'{cor["amarelo"]}{mensagem}{cor["limpa"]}'
    while True:
        print()
        print(titulo_deseja_continuar)
        continuar = input(
            f'\n{cor["branco"]}DIGITE{cor["limpa"]} {cor["verde"]}[S]{cor["limpa"]}'
            f' {cor["branco"]}PARA SIM OU {cor["limpa"]}'
            f'{cor["vermelho"]}[N]{cor["limpa"]} '
            f'{cor["branco"]}PARA NÃO: {cor["limpa"]}'
        ).upper().strip()
        print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
        if continuar in ["S", "SIM"]:
            return True
        elif continuar in ["NÃO", "NAO", "N"]:
            print(f'{cor["ciano"]}{mensagem2}{cor["limpa"]}', end="")
            for c in range(3):
                print(f'{cor["ciano"]}.{cor["limpa"]}', end="", flush=True)
                sleep(1)
            return False
        else:
            print(f'{cor["vermelho"]}OPÇÃO INVALIDA! TENTE NOVAMENTE.{cor["limpa"]}')
            print(f'{cor["branco"]}─{cor["limpa"]}' * 25)
            print()
            input(f'{cor["branco"]}PRESSIONE ENTER PARA CONTINUAR...{cor["limpa"]}')
            limpatela()
            print(data_formatada)
            continue
