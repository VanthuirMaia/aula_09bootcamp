import requests


# criar um decorator calcular_tempo

def calcular_tempo(func):
    def wraper(*args, **kwargs):
        print('Vou pegar a cotação')
        return func(*args, **kwargs)
    return wraper


@calcular_tempo
def pegar_cotacao_dolar():
    link = f"https://economia.awesomeapi.com.br/last/USD-BRL"
    requisicao = requests.get(link)
    requisicao = requisicao.json()
    print(requisicao['USDBRL']['bid'])

pegar_cotacao_dolar()

@calcular_tempo
def soma(x,y):
    return print(x + y)

soma(3,5)