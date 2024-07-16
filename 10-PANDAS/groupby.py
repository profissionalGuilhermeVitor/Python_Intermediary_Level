import pandas as pd 
from pandas import DataFrame

arq = pd.read_csv('dataset.csv')
df = pd.DataFrame(arq)
media_IDP_IDC = df[['ID_Pedido','ID_Cliente','Valor_Venda']].groupby(['ID_Pedido','ID_Cliente']).mean()
print(media_IDP_IDC)
agg_IDP_IDC = df[['ID_Pedido','ID_Cliente','Valor_Venda']].groupby(['ID_Pedido','ID_Cliente']).agg(['mean','std','count'])
print(agg_IDP_IDC)
print(df[df.ID_Pedido.str.startswith('CA')])
ano_pedido = df['ID_Pedido'].str.split('-').str[1]
print(df['ID_Pedido'].str.lstrip('CA-'))
print(df['ID_Pedido'].str.replace('CA','BR'))
df['ID'] = df['ID_Pedido'].str.cat(df['ID_Cliente'],sep='+')
print(df['ID'])