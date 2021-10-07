#Vamos a concocer ¿qué es un diccionario en python?,¿Como se utilizan ?
#Son estructuras de datos, que tienen {clave, valor} para cada elemento almacenado
# El orden en el que se alamcena da igual, se re corre igual 
# Podemos añadir un diccionario a otro diccionario

midiccionario = {"Alemania":"Berlín","Francia":"Paris","España":"Madrid","U.k":"Londo"}
print(midiccionario["Francia"])
print(midiccionario["España"])

#Para añadir nuevos elementos en el diccrionario lo hacemos de la siguiente manera
midiccionario["Italia"] = "Lisboa"
print(midiccionario)
#Para poder modificar algun valor de una clave, nos situamos en la clave y modificamos el valor
midiccionario["Italia"] = "Roma"
#Para imprimir todo el diccionario, solo con el nombre
print(midiccionario)

#Eliminar de un diccionario 
#El metodo del nombredeldiccionar["clave"]

del midiccionario["U.k"]
print(midiccionario) 

#Diccionario con Distintos valores 
diccionarioEjemplo ={"Alemania":"Berlin",23:"Jordan","Mosqueteros":3}
print(diccionarioEjemplo)

#Podemos utilizar un tupla para poder darle las claves a los diccionarios
#mitupla[indice]:valor
tuplaPaises =("España","Francia","U.k","Alemania")
diccionarioPais={tuplaPaises[0]:"Madrid",tuplaPaises[1]:"Paris",tuplaPaises[2]:"London",tuplaPaises[3]:"Berlin"}
print(diccionarioPais["Francia"])

#Para añadir una tupla a un diccionario 
diccJordarn = {23:"Jordan","Nombre":"Michael","Equipo":"Bulls","anillos":[1991,1992,1993,1996,1997,1998]}
print(diccJordarn)

#Para que exista un diccionario, dentro de otro diccionario 
diccJordan = {23:"Jordan","Nombre":"Michael","Equipo":"Bulls","anillos":
{"Temporadas":[1991,1992,1993,1996,1997,1998]}}

print(diccJordan)