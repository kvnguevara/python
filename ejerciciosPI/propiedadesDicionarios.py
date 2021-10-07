#Las funciones que tiene cada diccionar son las siguientes:
#Longuitud,claves

diccJordan = {23:"Jordan","Nombre":"Michael","Equipo":"Bulls","anillos":
{"Temporadas":[1991,1992,1993,1996,1997,1998]}}

#Para saber su longuitud
print(len(diccJordan))

#Para saber las claves del diccionario
print(diccJordan.keys())

#Para ver los valores de las claves del diccionario
print(diccJordan.values())

#funcion in, para saber si hay una clave(solo en la clave)

print("anillos" in diccJordan)