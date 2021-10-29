#Errores en python, se puden manejar siempre y cuando sepamos donde tratar el error 
#Para conseguir manipular o gestionar los erroes/ excepciones en python, se utiliza try-except-final
#En try: se pone el codigo, que está más subsentible a errores
#except: mostrar el mensaje si ocurre un error, hay que poner el tipo de error que lanza
#finally: Siempre se ejecuta, de o no el error/excepcion

#Primero error a tratar la Division 0
import os
numero = 45
numero2 = 0
try:
    result = numero/numero2
    print(result)
except:
    result = 0
    print("La division por 0, no se pude realizar")
finally:
    print(result)
    print("Se ejecuta siempre")
    
#error de borrar un archivo 
try:
    os.remove(os.getcwd()+"/archivo54.txt")
except FileNotFoundError:
    print("El archivo no se encuentra en el directorio")
finally:
    print("Fin de la Ejecucion")
