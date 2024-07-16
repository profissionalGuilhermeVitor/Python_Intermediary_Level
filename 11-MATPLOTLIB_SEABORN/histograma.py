import matplotlib.pyplot as plt
import numpy as np


l1 =[22,65,45,55,21,22,34,42,41,4,99,101,120,122,130,111,115,80,75,54,44,64,13,18,48]
l2 = np.linspace(0,100,len(l1))
x2 = [1,2,3,4,5]
y2 = [7,8,2,4,2]

plt.hist(l1, l2, histtype='bar',rwidth=0.8,color='green')

plt.legend()
plt.show()