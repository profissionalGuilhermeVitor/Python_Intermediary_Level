import pandas as pd 
from pandas import DataFrame

arq = pd.read_csv('Barra_de_Navegação_com_FlexBox.csv')
df = pd.DataFrame(arq)
print(df['Nome'])