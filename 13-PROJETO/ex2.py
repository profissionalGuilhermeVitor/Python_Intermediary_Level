import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


arq = pd.read_csv('dados/dataset.csv')
df = pd.DataFrame(arq)
print(arq.columns)
data_vendas = df[['Data_Pedido','Valor_Venda']]
gr_data_vend = data_vendas.groupby('Data_Pedido')['Valor_Venda'].sum()
index = list(gr_data_vend.index)
plt.figure(figsize=(20,6))
plt.bar(index,gr_data_vend)
plt.show()
