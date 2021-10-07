#Funcion Range, en python, nos permite iterrar con una lista o rango de números
#Para ello tenemos que usar range(),(indice,numeroTotal,iterracion)(5,50,3)
#empieza del 5 hasta 49 y va de 3 en 3
for i in range(len("juan")):
    print(f"valor de la variable {i}")
#Podemos utlizar len(), para saber la longuitud de la lista, tuplas o diccionario
lista = list(range(1,10))
print(lista)
a = ['Maria','Carlos','Bea','Elias']
for i in range(len(a)):
    print(i, a[i],end=",")