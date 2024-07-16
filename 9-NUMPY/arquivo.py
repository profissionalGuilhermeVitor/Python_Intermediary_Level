from platform import python_version
import numpy as np
import os
filename = os.path.join('Barra_de_Navegação_com_FlexBox')
arq = np.loadtxt(filename,delimiter=',',usecols=(0,1,2,3),skiprows=1,unpack=True)
print((arq)) #media
print(np.std(arq)) #desvio
print(np.var(arq)) # variancia
#operações
print(np.sum(arq))
print(np.prod(arq))
