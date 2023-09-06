import acessaGoogleSheet as planilha
import matplotlib.pyplot as plt
import matplotlib.dates as mdates 
import numpy as np
import pandas as pd
from datetime import date

def analiseDolar():
    basePandas = pd.DataFrame(planilha.read())

    basePandas.columns = basePandas.iloc[0]
    basePandas = basePandas.iloc[1:]
    basePandasDolar = basePandas[basePandas['Moeda'] == 'Dolar Comercial'].copy()
    basePandasDolarT = basePandas[basePandas['Moeda'] == 'Dolar Turismo'].copy()
    basePandasEuro = basePandas[basePandas['Moeda'] == 'Euro'].copy()
    
    #tratamento Campo Timestamp
    # Converte a coluna 'Timestamp' para formato datetime
    basePandasDolar['Timestamp'] = pd.to_datetime(basePandasDolar['Timestamp'])
    basePandasDolarT['Timestamp'] = pd.to_datetime(basePandasDolarT['Timestamp'])
    basePandasEuro['Timestamp'] = pd.to_datetime(basePandasEuro['Timestamp'])

    # Reformatar a coluna 'Timestamp' para AAAAMMDD
    basePandasDolar['Timestamp'] = basePandasDolar['Timestamp'].dt.strftime('%Y%m%d')
    basePandasDolarT['Timestamp'] = basePandasDolarT['Timestamp'].dt.strftime('%Y%m%d')
    basePandasEuro['Timestamp'] = basePandasEuro['Timestamp'].dt.strftime('%Y%m%d')
   
    #Converte a coluna "Cotacao" para valores numéricos
    basePandasDolar['Cotacao'] = pd.to_numeric(basePandasDolar['Cotacao'])
    basePandasDolarT['Cotacao'] = pd.to_numeric(basePandasDolarT['Cotacao'])
    basePandasEuro['Cotacao'] = pd.to_numeric(basePandasEuro['Cotacao'])

    # Converte a coluna 'Timestamp' de volta para formato datetime
    basePandasDolar['Timestamp'] = pd.to_datetime(basePandasDolar['Timestamp'], format='%Y%m%d')
    basePandasDolarT['Timestamp'] = pd.to_datetime(basePandasDolarT['Timestamp'], format='%Y%m%d')
    basePandasEuro['Timestamp'] = pd.to_datetime(basePandasEuro['Timestamp'], format='%Y%m%d')

    plt.plot(basePandasDolar["Timestamp"], basePandasDolar["Cotacao"], color = 'g', ls='--', lw="2", marker = 'o', label = 'Dolar Comercial')
    plt.plot(basePandasDolarT["Timestamp"], basePandasDolarT["Cotacao"], color = 'r', ls='--', lw="2", marker = 'o', label = 'Dolar Turismo')
    plt.plot(basePandasEuro["Timestamp"], basePandasEuro["Cotacao"], color = 'b', ls='--', lw="2", marker = 'o', label = 'Euro')
    plt.legend(loc = 2, fontsize = 18)
    plt.xlabel("Data")
    plt.ylabel("Cotação (R$)")
    plt.title("Gráfico Dolar/EURO 2023")
    plt.legend()
    
    #Formatar eixo de datas
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=1))  # Define intervalo entre os dias
    plt.gcf().autofmt_xdate()  # Formatação automática das datas para evitar sobreposição
    
    #Inclinar rótulos no exio X
    plt.xticks(rotation=45)

    #Adicionar Grid 
    plt.grid(True)

    # Salvando a figura
    plt.tight_layout()  # Melhora a disposição dos elementos no gráfico

    plt.savefig('graficoDolarEuro.png', format='png')

    #plt.show()


#Testes
#analiseDolar()

