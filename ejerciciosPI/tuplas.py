#Las tuplas son listas pero solo que no se puede modificar, son estaticas, es decir, que una vez creadas 
# No se puede modificar.
# La sintaxis de una tupla van en parentesis  tupla(1,2,3,)

mitupla = ("Juan",13,1,1995)
print(mitupla[2])

#Para convertir una tupla a una lista, tenemos el método list
milista = list(mitupla)
print(milista)
print(mitupla)

#Para convertir una lista a tupla, tenemos el método tuple
lista =["Juan",14,12,1987]
tuplaEjemplo = tuple(lista)
print("Juan" in tuplaEjemplo) #Para buscar un elemento en la tupla

#count, nos indica cuantos elementos, hay dicho elemento en la tupla

print(tuplaEjemplo.count(14))

#Metodo len(), nos indica la longuitud de tupla o lista
print(len(tuplaEjemplo))

#Para indicar que la tupla será unitaria, tenemos que poner ("Elemento unico",)
#Con la ("", ) le estámos diciendo que solo tendrá un único elemento 
tuplaUnitaria = ("Carlos",)
print(tuplaUnitaria)

#Desempaquetado de tuplas, es asignar valores a distintas variables.
nombre, dia, mes, agno = tuplaEjemplo
print (nombre, agno, dia , mes)

