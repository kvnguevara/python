#Programa que calcula la raiz cuadra de un numero
#Controlando las excepciones, ya que la raiz cuadrada de un numero negativo, no existe
import math
def rCuadrada(num1):
    """funcion que calcula la raiz cuadrad"""
    if num1<0:
        raise ValueError("el numero no puede ser negativo")
    else:
        return math.sqrt(num1)

op1 = int(input("Introduzca un numero para su raiz cuadrada: "))
try:
    
    print(rCuadrada(op1))
except ValueError as ErrorDeNumeroNegativo:
    print(ErrorDeNumeroNegativo)
    
print("Programa finalizado...")