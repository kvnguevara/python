#Vamos a pedir la edad de un usuario para saber si es mayor de edad
# > 18 es mayor de edad, <18 es menor y mostraremos un mensaje de no pasar
print("Progrma para saber si es mayor de edad")

def mayorEdad(edad):
    if edad<18:
        print("Es menor de edad")
    elif edad>100:
        print("Edad incorrecta")
    else:
        print("Es mayor de edad")
        
edad = int(input("Introduzca la edad:"))
mayorEdad(edad)
print("Fin del programa")