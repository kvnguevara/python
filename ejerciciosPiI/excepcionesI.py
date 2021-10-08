#Programa para gestionar las excepcion es python 
#Para ello haremos un programa para ver su funcionamiento

#Programa de resta, multiplicacion,suma y division 
#Gestionando así las Excepciones en python

#captura o control de excepcion, lo utilizamos para que el programa no tenga problema de ejecucion 
#como por ejemplo division o.
#Asi evitamos que el programa no caiga 

def suma(num1,num2):
    """ Funcion para sumar dos números"""
    return num1+num2
def resta(num1,num2):
    """Funcion para restar dos numeros """
    return num1-num2
def multiplicar(num1,num2):
    """Funcion para multiplicar dos numeros"""
    return num1*num2
def division(num1,num2):
    """Funcion para dividir dos numeros"""
    #Capturamos la excepcion de la division *0
    try:    
        return num1/num2
    except ZeroDivisionError:
        print("no se pude la division")
        return "Operacion Erronea"
while True:
    try: 
        op1=int(input("Introduzca el primer numero: "))
        op2= int(input("Introduzca el segundo numero:"))
        break
    except ValueError:
     print("Valores introducidos no correctos")
    


operacion=input("Introduzca la operacion a realizar(suma,division,resta,multiplicar)")
if operacion=="suma":
    print(suma(op1,op2))
elif operacion=="resta":
    print(resta(op1,op2))
elif operacion=="multiplicar":
    print(multiplicar(op1,op2))
elif operacion=="division":
    print(division(op1,op2))
else:
    print("Operacion no valida")
    
print("Ejecucion de la Operacion.....continuacion del programa !!!")
        
