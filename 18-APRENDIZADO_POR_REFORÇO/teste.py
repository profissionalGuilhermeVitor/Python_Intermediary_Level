import random
import plotly.graph_objects as go
import pandas as pd
import numpy as np
from datetime import datetime

df = pd.read_csv('finance-charts-apple.csv')
fig = go.Figure(data = [go.Candlestick(x = df['Date'],
                                       open=df['AAPL.Open'],
                                       high=df['AAPL.High'],
                                       low=df['AAPL.Low'],
                                       close=df['AAPL.Close']
)])
precos = df['AAPL.Close'].values
acoes = ['comprar','vender','manter']
saldo_inicial = 1000
num_acoes = 0

def executar(estado,acao,saldo,num_acoes,preco):
    if acao ==0:
        if saldo >= preco:
            num_acoes +=1
            saldo -= preco
    elif acao ==1:
        if num_acoes >0:
            num_acoes -= 1
            saldo+=preco
    
    lucro = saldo + num_acoes *preco - saldo_inicial
    
    return (saldo,num_acoes,lucro)



