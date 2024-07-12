import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm


file = pd.read_csv('14-STATSMODELS/dataset.csv')
df = pd.DataFrame(file)

y = df['valor_aluguel']
x = df['area_m2']

X = sm.add_constant(x)
modelo = sm.OLS(y,X)
c = sm.datasets.load_iris()
resultado = modelo.fit()
print(c)