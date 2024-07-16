import matplotlib.pyplot as plt
import numpy as np


l1 = ['Vikings','Game of Thrones','Succession','Better Call Saul','Watchmen']
l2 = np.linspace(0,100,5)
x2 = ['Viking','Game of Throne','Succession','Better Call Saul','Watchmen']
y2 = [7,8,2,4,2]

plt.bar(l1, l2, label = 'Barras',color='green')
plt.bar(x2, y2, label = 'Barras2',color='b')
plt.legend()
plt.show()