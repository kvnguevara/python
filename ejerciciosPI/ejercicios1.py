#Ejerjcio 1
# Pedir dos numeros y mostrar el mayor de los dos
#con una funcion que devuelve el mayor de los numeros

def numeroMayor(num1, num2):
    if num1>num2:
        return num1
    else:
        return num2
#Pido los datos para llamar a la funcion
num1 = int(input("Introduzca el primer numero:"))
num2 = int(input("Introduzca el segundo numero:"))

print("El mayor numero es: ",numeroMayor(num1,num2))


#Ejercicio 2
#Vamos a pedir datos personales, nombre, direccion, tlf y mostrarlos por pantalla
def pedirdatos():
    nombre=input("Introduzca Nombre:")
    direccion = input("Introduzca Direccion:")
    tlf = input("Introduzca Telefono: ")
    diccDatos ={"nombre":nombre,"direccion":direccion,"tlf":tlf}
    print("Los datos personales son ",diccDatos)
pedirdatos()

#Ejercicio 3
#Pedir 3 numeros y mostrar la media
def mediaAritmetica():
    n1=int(input("Intro numero1:"))
    n2 = int(input("Introduzca el numero2:"))
    n3 = int(input("Introduzca el tercer numero: "))
    return (n1+n2+n3)/3
print("La media Aritmetica es: ",mediaAritmetica())