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
media_depois = df['Valor_Desconto'][df['Desconto']==0.15].mean()
media_antes = df['Valor_Venda'][df['Desconto']==0.15].mean()

print("A media antes do desconto é de :R$",np.round(media_antes,2))
print("A media depois do desconto é de :", np.round(media_depois,2))
