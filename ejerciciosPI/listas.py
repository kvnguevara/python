#Los array en python es como los array en otros lenguajes
#Vamos a dar la funcionalidad , como crear, mostrar, añadir o modificar 
#Las funciones que le podemos dar uso a dichas listas

miLista = ["Maria","Luis","Carla","Lorena","Carolina"]
print(miLista)
#Podemos manejar numeros negativos en las listas
#Empieza a contar de -1, siempre que utlizamos los numeros negativos

#Podemos entrar a porciones de las listas

print(miLista[:3])

#Para acceder a las ultimas posicion inicial hasta el final, de esta forma lo hace array[2:]

miLista.append("Jocelyn")
print(miLista)


#Insert, es para insertar en la mitad o el indice de donde queremos añadir elementos en la lista
# array.insert(indicie,"elemento")

miLista.insert(2,"Manuela")

print(miLista)

#Para añadir mas objetos a las listas, tenemos la funcion extend
#array.extend(["elemento1","elemento2","elemento3"])
miLista.extend(["Luisa","Corina","Fabiola","Maria"])
print(miLista[:])

#Para buscar algun elemento en las listas, tenemos la funcion .index["elemento"], siempre devuelve el primero
#Si hay más de dos 
print(miLista.index("Maria"))

#Para saber si hay un elemento en la lista, tenemos in, que devuelve true (si lo encuentra)
#false(si no lo encuentra)  
bandera = "Luisa" in miLista

print(bandera)


#La gran potencia que tiene python, es que las listas pueden almancenar cualquier tipo de datos
# es decir, que puede tener, cadenas de caracteres, booleanos, números
listaMixta = [1,2,3,"Jose","Juan",True]
print(listaMixta)

#Para remover elementos en una lista tenemos la funcion remove[indice o elemento ] a borrar  
listaMixta.remove("Juan")
print(listaMixta[:])

#Para poder eleminar el ultimo elemento una lista utilizamos pop

miLista.pop()
print(miLista)

