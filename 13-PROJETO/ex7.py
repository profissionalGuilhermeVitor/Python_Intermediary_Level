import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sea
import datetime as dt

arq = pd.read_csv('dados/dataset.csv')
df = pd.DataFrame(arq)
df['Desconto'] = np.where(df['Valor_Venda']>1000,0.15,0.1)
df['Valor_Desconto'] = (1-df['Desconto'])*(df['Valor_Venda'])
num_desc = df[df['Desconto']==0.15].value_counts()
print("Existem",num_desc.count(),"Valores com 15% de desconto")
