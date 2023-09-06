import AcessaApiDeCotacao
import acessaGoogleSheet
import EnviaEmailGmail
import AnaliseValores

#ACESSO A API DE COTACAO DE MOEDAS
cotacaoDolarComercial, cotacaoDolarTurismo, timestamp = AcessaApiDeCotacao.acessaCotacaoDolar()
dolar = 'Dolar Comercial'
dolart = 'Dolar Turismo'
str_timestamp = str(timestamp)   #converte para string, pois o json nao funciona com timestamp

cotacaoEuro, timestampEuro = AcessaApiDeCotacao.acessoCotacaoEuro()
euro = 'Euro'
str_timestampEuro = str(timestampEuro)   #converte para string, pois o json nao funciona com timestamp

#CONECTA AO GOOGLESHEET 
acessaGoogleSheet.conectar()

#OBTEM A QUANTIDADE DE REGISTROS NA BASE, PARA GRAVAR NO REGISTRO VAZIO SEGUINTE
lista = acessaGoogleSheet.read()
quantidadeItensLista = len(lista)

listaAtualizacao = [[dolar,cotacaoDolarComercial,str_timestamp],
                    [dolart,cotacaoDolarTurismo,str_timestamp],
                    [euro,cotacaoEuro,str_timestampEuro]]

#GRAVA NA BASE DE DADOS
acessaGoogleSheet.write(quantidadeItensLista, listaAtualizacao)

#Analisa os valores e monta o Grafico para enviar por email
AnaliseValores.analiseDolar()

#Envia Email
EnviaEmailGmail.enviar_email(cotacaoDolarComercial, cotacaoEuro)
