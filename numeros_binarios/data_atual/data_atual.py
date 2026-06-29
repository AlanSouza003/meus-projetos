from datetime import date

def data_atual(cor):
    hoje = date.today()
    data_formatada = f'{cor["verde"]}DATA: {hoje.day:02d}/{hoje.month:02d}/{hoje.year}{cor["limpa"]}'
    return data_formatada
    