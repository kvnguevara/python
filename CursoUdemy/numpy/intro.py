#Clase 1 de numpy
import numpy as np

lista_num =[1,2,3,4,5,6,7,8,9,10,11]
#Convertir lista a array
array_num = np.array(lista_num)
print(type(array_num))
print("Impresion de Array")
print(array_num)
print("Impresion de Lista")
print(lista_num)
list_num2 =[[1,2,3],[3,4,5,],[6,7,8,],[9,10,11]]
array_num2 = np.array(list_num2)
print(array_num2)
#Crear un array de rango.

arr_num =np.arange(6)
print("Array obtenido de rango hasta 6")
print(arr_num)


#array generador de rango, con intervalos 
print("Array Rango, con intervalos")
arr_num = np.arange(2,26,3)
print(arr_num)
#Crear una matriz de cero
m_zeros = np.zeros((3,4))
print(f"Matriz de 0: {m_zeros}")

#Crear matriz de 1
m_zeros = np.ones((3,4))
print(f"Matriz de 1---{m_zeros}")
#Crear Matriz identidad 
m_identidad= np.eye(7)
print(m_identidad)
#numeros aleatorias
m_aleatorias = np.random.rand(3,4)
print(m_aleatorias)
#Para crear array de numeros enteros
m_aleatorias = np.random.randint(1,51,20)
print(m_aleatorias)
#Dar forma a los arrays
m_aleatorias = m_aleatorias.reshape(2,10)
print(m_aleatorias)
#Encontrar el maximo
print(f"El valor maximo es{m_aleatorias.max()}")
#Para obtener la posicion,con el argumento argmax
print(f"La posicion del maximo es {m_aleatorias.argmax()}")
#Para sacar el mino, tenemos que usar min, y la posicion argmin()
print(f"El minimo es {m_aleatorias.min()} y su posicion es {m_aleatorias.argmin()}")
#Para obetener partes de un array, se tiene que utilizar [n:m],[n:]-->indicamos las ultimas posiciones [:m]-->primeras posiciones
arr_num = np.arange(1,11)
print(arr_num)
#mostrar los primeros 5 elementos
print(f"Los primeros elementos: {arr_num[:5]}")
#Los ultimos elementos
print(f"Los ultimos 5 elementos:{arr_num[5:]}") 
#Hacer una copia del array 
copy_arr = np.copy(arr_num)
print(copy_arr)
copy_arr[3]=8
print(f"Copia: {copy_arr}")
print(f"Array original: {arr_num}")