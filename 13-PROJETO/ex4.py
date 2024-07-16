import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sea

arq = pd.read_csv('dados/dataset.csv')
df = pd.DataFrame(arq)
lp = np.linspace(0,10,10)

city_sails = df.groupby('Cidade')['Valor_Venda'].sum().reset_index().sort_values(by='Valor_Venda',ascending=False)
city_sails=city_sails[:10]
id_city = city_sails.index[:10]
plt.figure(figsize=(20,6))
sea.set_palette('coolwarm')
sea.barplot(data=city_sails,x='Cidade',y='Valor_Venda').set(title='Top 10 Cidades')
plt.xticks(rotation=90)
plt.show()
