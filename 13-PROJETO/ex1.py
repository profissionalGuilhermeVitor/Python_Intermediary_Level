import pandas as pd
import os

superstore_file = pd.read_csv('dados/dataset.csv')
df = pd.DataFrame(superstore_file)
filtro = df[['Cidade','Valor_Venda','Categoria']]
office_filtro = filtro[filtro['Categoria']=='Office Supplies']
office_filtro_total =  office_filtro.groupby('Cidade')['Valor_Venda']
print("Cidade com maior Valor de Venda em Office Supplies: ",office_filtro_total.sum().idxmax())