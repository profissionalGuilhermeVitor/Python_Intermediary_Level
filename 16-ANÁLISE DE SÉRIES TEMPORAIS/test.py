import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.holtwinters import SimpleExpSmoothing

file = pd.read_csv('dataset.csv')
df = pd.DataFrame(file)
df['Data'] = pd.to_datetime(df['Data'])
serie = df.set_index('Data')['Total_Vendas']
serie = serie.asfreq('D')
modelo = SimpleExpSmoothing(serie)
modelo_ajustado = modelo.fit(smoothing_level = 0.7)
suavizacao_exponencial = modelo_ajustado.fittedvalues
plt.figure(figsize = (12, 6))
plt.plot(serie, label = 'Valores Reais')
plt.plot(suavizacao_exponencial, label = 'Valores Previstos', linestyle = '--')
plt.xlabel('Data')
plt.ylabel('Vendas')
plt.title('Modelo de Suavização Exponencial')
plt.legend()
plt.show()
