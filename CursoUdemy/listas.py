#Las listas en python son como los array en java
#cosas importantes en las listas[0:4]-> se trocea la lista, es decir, que de vuelve una nueva 
#list(reversed(lista)): muestra la lisa alreves, pero mantiene la original
#lista.reverse(), modifica la lista, y la muestra alreves
#Añadir al final lista.append('element nuevo')
#Crear una lista vacia nueva_lista= []
#añadir en una posicion en concreto lista.insert(posicion,'element nuevo')
#Para eliminar el ultimo elemento de la lista con pop()-->lista.pop()
#Mostrar lista alreves
#Para añadir otra lista o funcionar dos lista, con list.extend
#Para eliminar valores de una lista, tenemos :
#dos funciones remove(), del(lista[])--> lista.remove(3), del(lista[3])
#remove(), solo borra la primera concurencia, si hay más valores en la lista no las borra
#Dejar una lista en blanco o borra toda la lista, tenemos clear()
#otra forma de vaciar la lista es: lista = []
#Busca elementos en una lista con index lista.index('5'), pero nos dara un error, si no se encuentra
#Otra forma de buscar los elementos, es con la funcion in, está devuelve true, si existe, y false, si no esta
#La funcion isalpha()-> nos dice si la cadena o lista, esta formada solo por letras, sin espacios
#isdigit()--> si la cadena es numerico
#isalnum()--> si es alfanumerica
lista = [25,85,44,25]
lista.reverse()
print(lista) #Modfica la lista

print(list(reversed(lista)))
lista.append('casa')
print(lista)
nueva_lista=[]
#añadir numeros pares del 0-20
for i in range(20):
    if i%2==0:
        nueva_lista.append(i)
print(nueva_lista)
nueva_lista.insert(7,500)
print(nueva_lista)
#Eliminar el ultimo elemento de la lista
nueva_lista.pop()
print(nueva_lista)
nueva_lista.extend(lista)
print(nueva_lista)
nueva_lista.remove(25)
print(nueva_lista)
nueva_lista.clear()
print(nueva_lista)
#Buscar un elemento en la lista.
print (85 in lista)
