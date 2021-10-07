#En python no hay o no existe la forma de switch, pero si nos ofrece la forma de hacerlo
#con if y else, o concatenando condicionales, con diccionarios.
#Todas estas formas serían para suplantar el switch 
#El flujo de la lectura es de izquierda a derecha, como si estuvieras leyendo un libro
edad = 145
if 0 < edad < 100:
    print("Edad correcta")
else:
    print("Edad incorrecta")


#Vamos hacer un ejerccio donde se compara el salario de un admini, jefe, director
#Y mostrar el mensaje 

salario_presidente=int(input("Introduzca el salario de Presidente: "))
print("Salario presidente",salario_presidente)
salario_director = int(input("Introduzca el salario del director: "))
print("Salario Director:",salario_director)
salario_jefeArea = int(input("Introduzca el salario del jefe de Area: "))
print("Salario del Jefe de Area: ",salario_jefeArea)
salario_administrativo= int(input("Introduzca el salario del administrativo: "))
print("Salario de Administrativo: ",salario_administrativo)

#La evaluacion de los sueldos, con la comparacion de if 
if salario_administrativo<salario_jefeArea<salario_director<salario_presidente:
    print("Todo funciona bien")
else:
    print("Algo falla")