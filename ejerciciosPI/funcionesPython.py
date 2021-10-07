#En este clase vamos a tratar las funciones en Python.
#Desde como se crea, su llamado , y su funcionamiento, es decir, como se utilizan
# Para definir una funcion es def nombre_funcion(): 
# Declaracion de las instrucciones estás intruscciones tiene que estar identadas
# return ( opcional)

#def nombre_funcion(parametros):

def mensaje(): #definicion de la funcion
    print("Hola...mensaje 1") #Instrucciones de la funcion
    print("Hola...mensaje 2")
    print("Hola...mensaje 3")
    print("Hola...mensaje 4")
mensaje() #llamada de la funcion
def suma(num1,num2):   
    print(num1+num2)

def metodo_fibonacci():
    a,b = 0,1
    while a <100:
        print(a,end=",")
        a,b = b, a+b

def suma_return(num1,num2):
    return num1+num2


#funciones sin return
mensaje()
suma(3,6)
suma(82,32)
suma(3,7)
metodo_fibonacci()
#funciones sin return
print()
print(suma_return(2,9))


