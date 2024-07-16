import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sea
import datetime as dt

arq = pd.read_csv('dados/dataset.csv')
df = pd.DataFrame(arq)
df['Ano'] = pd.to_datetime(df['Data_Pedido'],dayfirst=True)
df['Mes'] = df['Ano'].dt.month
df['Ano'] = df['Ano'].dt.year

filtro = df[['Valor_Venda','Segmento','Ano','Mes']]
gr_filtro = filtro.groupby(['Segmento','Ano','Mes'])['Valor_Venda'].agg([np.sum,np.mean,np.median])
seg = gr_filtro.index.get_level_values(0)
ano = gr_filtro.index.get_level_values(1)
mes = gr_filtro.index.get_level_values(2)

sea.relplot(kind='line',data=gr_filtro,x=mes,y='mean',hue=seg,col=ano,col_wrap=4)
plt.show()
