import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm

file = pd.read_csv('14-STATSMODELS/dataset.csv')
df = pd.DataFrame(file)
print(df.columns)
print(df.info())
