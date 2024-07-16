import pandas as pd 
from pandas import DataFrame
dicionario = {
    'Estados':['Minas Gerais','Rio de Janeiro','Espirito santo','Amazonas','Goiás','Rio Grande do Sul'],
    'Time mais popular':['Flamengo','Vasco','Corinthians','Cruzeiro','Atlético','Internacional'],
    'Habitantes':[10000,30000,1000000,15000,10000,100000]
}

df = pd.DataFrame(dicionario,columns=['Time mais popular','Estados','Habitantes','Ano'],index=['e1','e2','e3','e4','e5','e6'])

print(df.describe())
print(df.isna())
print(df['e1':'e4'])
print(df[df['Habitantes']>15000])
print(df[['Estados','Habitantes']])
arq = pd.read_csv('dataset.csv')
df2 = pd.DataFrame(arq)
print(df2.isna().sum())
moda = df2['Quantidade'].value_counts().index[0]
df2['Quantidade'].fillna(value=moda,inplace=True)
print(df2.isna().sum())