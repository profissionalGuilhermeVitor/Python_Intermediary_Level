import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sea
import datetime as dt

arq = pd.read_csv('dados/dataset.csv')
df = pd.DataFrame(arq)

filtro = df[['Categoria','SubCategoria','Valor_Venda']]
vend_cat_subcat = filtro.groupby(['Categoria','SubCategoria'])['Valor_Venda'].sum()
fr_cat_subcat = vend_cat_subcat.reset_index().sort_values(by='Valor_Venda',ascending=False)[:12]
cat = fr_cat_subcat['Categoria']
subcat =fr_cat_subcat['SubCategoria']
valor = fr_cat_subcat['Valor_Venda']
plt.figure(figsize=(20,10))
sea.barplot(data=fr_cat_subcat,x=subcat,y=valor,hue=cat)
plt.show()
print(cat)