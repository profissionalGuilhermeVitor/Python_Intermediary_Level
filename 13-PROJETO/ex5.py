import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sea

def autopct_format(values):
    def my_format(pct):
        total = sum(values)
        val = int(round(pct*total/100.00))
        return '$ '+'{v:d}'.format(v=val)
    return my_format

arq = pd.read_csv('dados/dataset.csv')
plt.figure(figsize=(10,6))
df = pd.DataFrame(arq)
seg_vendas = df.groupby('Segmento')['Valor_Venda'].sum().reset_index().sort_values(by='Valor_Venda',ascending=False)
pie_data = seg_vendas['Valor_Venda']
plt.pie(x=pie_data,labels=seg_vendas['Segmento'],colors=['b','y','m'],autopct=autopct_format(pie_data))
center = plt.Circle((0.0),0.82,fc='white')
centre_circle = plt.Circle((0, 0), 0.82, fc = 'white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

plt.show()


print(autopct_format(pie_data)) 
