import pandas as pd 
from pandas import DataFrame
dicionario = {
    'Estados':['Minas Gerais','Rio de Janeiro','Espirito santo','Amazonas','Goiás','Rio Grande do Sul'],
    'Time mais popular':['Flamengo','Vasco','Corinthians','Cruzeiro','Atlético','Internacional'],
    'Habitantes':[10000,30000,1000000,15000,10000,100000]
}

df = pd.DataFrame(dicionario,columns=['Time mais popular','Estados','Habitantes','Ano'],index=['e1','e2','e3','e4','e5','e6'])
print(df.head())
print(df.values)
print(df[['Estados','Habitantes']])
print(df.filter(items=['e1','e2'],axis=0))
