#El bucle while, en python se parece al resto de lenguajes
#funcion de fibonacci
import math
def fib(n):
    """" Imprime la funcion de fibonacci"""
    a,b = 0,1
    while(a<n):
        print(a,end=",")
        a,b=b,a+b
#Llamamos a la funcion 
fib(20)
#funcion para saber la raiz cuadrada de un número
def raizCuadrada():
    print("Programa de calculo de la raiz cuadra")
    numero = int(input("Introduzca un numero: "))
    intentos = 0
    while numero < 0:
        print("No se puede hallar la raiz cuadrada de un numero negativo")
        if intentos == 2:
            print("Ha superado el numero de intentos")
            break;
        numero = int(input("Introduzca un numero: "))
        if numero < 0:
            intentos+=1
    else:
        solucion = math.sqrt(numero)
        print("La raiz cuadrada de ",numero," es ",solucion)
#Llamada de la funcion
raizCuadrada()

#While con continue
def whContinue(num):
    while num > 0:
        num-=1
        if num == 5: 
            continue
        print(f"Valor actual de la variable {num}")
print()
#Llamada a la funcion
whContinue(10)    