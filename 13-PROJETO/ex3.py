import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sea

arq = pd.read_csv('dados/dataset.csv')
df = pd.DataFrame(arq)

gr_est = df.groupby('Estado')['Valor_Venda'].sum().reset_index()
index = gr_est.index

plt.figure(figsize=(20,6))
sea.barplot(data=gr_est,x='Estado',y='Valor_Venda').set(title='Vendas por Estado')
plt.xticks(rotation=80)
plt.show()