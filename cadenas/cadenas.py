#Vamos a ver el tratamiento de cadenas en python
#Para ello hay una serie de funciones que nos ayudaran con el tratamiento de dichas cadenas.
# upper()--> mayusculas lower()-->minusculas capitalize()->Pone en Mayuscula la primera count()->cuenta cuantass veces a parece dicha letra fin()->busca si hay alguna letra isdigit()-> es valor numerico isalum()-> alfanumericos isalpha()-> si solo hay letras, los espacio no cuentan split()->separa por palabras por espacio replace()->reemplaza una letra por otra rfind()->
from typing import Counter


nombre_usuario = "Kevin"
print("Mayusculas: ",nombre_usuario.upper())
print("minusculas: ",nombre_usuario.lower())
nombre_usuario = "armando"
print("capitalize: ",nombre_usuario.capitalize())
print("a: ",nombre_usuario.count('a'))

#isalum 
edad = input("Edad: ")

while(edad.isdigit()==False):
    print("Introdzuca un valor numerico: ")
    edad = input("Edad: ")
    
if int(edad) < 15:
    
    print("No puedes pasar")
    
else:
    print("Puede pasar")