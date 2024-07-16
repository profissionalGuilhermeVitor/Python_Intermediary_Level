import matplotlib.pyplot as plt
import numpy as np


l1 =[22,65,45,55,21]
l2 = np.linspace(0,100,len(l1))
x2 = [1,2,3,4,5]
y2 = [7,8,2,4,2]

plt.scatter(l1,l2,label='Scatter',color='b',marker='+')
plt.stackplot(l1,l2,x2,y2,colors=['y','m','r','v'])
plt.legend()
plt.show()
plt.close()
plt.pie(l1,labels=['velho','idoso','jovem','ferrado','tranquilo'],startangle=0,shadow=True,explode=[0,0,0.4,0.5,0])
plt.legend()
plt.show()