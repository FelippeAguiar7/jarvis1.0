import requests
from datetime import datetime, timedelta


def acessaCotacaoDolar():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL")
    requisicaoDolar_dic = requisicao.json()
    cotacaoDolarComercial = requisicaoDolar_dic["USDBRL"]["ask"]
    
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRLT")
    requisicaoDolarTurismo_dic = requisicao.json()
    cotacaoDolarTurismo = requisicaoDolarTurismo_dic["USDBRLT"]["ask"]
    timestamp = datetime.now()
    
    return cotacaoDolarComercial, cotacaoDolarTurismo, timestamp


def acessoCotacaoEuro():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/EUR-BRL")
    requisicao_dic = requisicao.json()
    cotacaoEuro = requisicao_dic["EURBRL"]["bid"]
    timestamp = datetime.now()

    return cotacaoEuro, timestamp


#teste
#print (acessaCotacaoDolar())
#print (acessoCotacaoEuro())
