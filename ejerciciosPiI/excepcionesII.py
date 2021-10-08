#Programa para controlar las excepciones en python 
#En este caso será una funcion que nos pida dos numeros, y haga la division. controlando la division por CERO

#Programa Division
def division():
    """Funcion de division, con sus control de error con try/excepciones/finaly"""
    try:
        num1= float(input("Introduzca el primer numero:"))
        num2 = float(input("Introduzca el segundo numero"))
        print("La division es:",num1/num2)
    except ValueError:
        print("El valor introducido es erroneo")
    except ZeroDivisionError:
        print("Division *0")
    finally: #Siempre se ejecuta !!!
        #Aun cuando da error de ejecucion.
        print("Calculo ")
    
division()