import matplotlib.pyplot as plt
from matplotlib.pylab import *
import numpy as np


# Dados
x = np.linspace(0, 5, 10)
y = x ** 2

# Cria a figura
fig = plt.figure()


# Define a escala dos eixos
axes = fig.add_axes([0, 0, 1, 1])

# Cria o plot
axes.plot(x, y, 'r')
axes.set_title('U')
fig.show()
fig.savefig('file.png')
