from platform import python_version
import numpy as np

print(np.__version__)
lista = [1,2,3,4,5,6,7,8,9]
array = np.array(lista)
print(array)#Dados organizados em array sem virgula
print(array.shape)#(9,)
lista2d = [[1,2,3,4,5,6],[9,8,7,6,5,4]]
array2d = np.array(lista2d)
print(array2d.itemsize)#4
print(array2d)
print(array2d.shape)#(2,6)

#Fatiamento
print(array[2:])#[3 4 5 6 7 8 9]
print(array[2:6])#[3 4 5 6]
#Mascara
mask = (array >3)
print(mask)
print(array[mask])
#Funções
print(np.cumsum(array))
print(np.cumprod(array))
print(np.arange(10,50,1))
print(np.zeros(100))
print(np.diag(array))#Cria matriz com elementos da array
print(np.logspace(0,100,5))#[1.e+000 1.e+025 1.e+050 1.e+075 1.e+100]
#Matrizes
print(np.ones((2,3)))
matrix = np.matrix(array2d)
print(matrix)
print(np.array(lista2d,dtype=np.float64))#O tipo já mudou pra float
print(array.itemsize)
