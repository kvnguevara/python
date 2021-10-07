#Programa de becas
#

print("Programa de becas")
distanciaEscuela = int(input("Introduzca la distancia a la escuela (km):"))
numeroHermanos = int(input("Introduzca el nº de hermanos:"))
salarioFamiliar= int(input("Introduzca el salario bruto: "))
if distanciaEscuela > 40 and numeroHermanos > 2 and salarioFamiliar <= 20000:
    print("Tienes derecho a becas")
else: 
    print("No tiene beca")