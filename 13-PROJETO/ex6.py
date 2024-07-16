import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sea
import datetime as dt

arq = pd.read_csv('dados/dataset.csv')
df = pd.DataFrame(arq)
#df['Ano'] = df['Data_Pedido'].str.split('/').str[2]
df['Ano'] = pd.to_datetime(df['Data_Pedido'],dayfirst=True)
df['Ano'] = df['Ano'].dt.year
seg_year_vendas = df[['Segmento','Ano','Valor_Venda']]
print(seg_year_vendas.groupby(['Ano','Segmento'])['Valor_Venda'].sum())
