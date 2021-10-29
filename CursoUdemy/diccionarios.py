#Diccionarios en Python son un conjunto de datos, que están asociadas por clave,valor

diccionario = {"kevin":"guevara", "Luis":"Carrasco","Jorge":"Nolasco"}
#mostrar
print(diccionario)
print(diccionario.keys())
print(diccionario.values())
#eleminar con pop, elimina lo que le pasamos, tiene que ser la clave
# diccionario.pop('kevin')
print(diccionario)
#Copiar diccionario 
copy_diccinario = diccionario.copy()
print(f"Copia del dicionado {copy_diccinario}")
dicc02 = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6}
print(dicc02)
#Modificar los valores de las claves del diccionario
dicc03 = dict.fromkeys(['a','b','c','d','e','f'],25) #Con dict.fromkeys([keys],valor nueno)
print(dicc03)
#Creando dos duplas en una va la clave y en otra el valor 
#tupla paises, capital 
t_pais = ('Francia','Honduras','Mexico','España')
t_capital = ('Paris','tegucigalpa','Mexico D.F','Madrid')
t_todo= zip(t_pais,t_capital)

dico4  =  dict()
#Creando el diccionario 
dic04 = dict((t_todo))
print (dic04)