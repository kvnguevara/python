#importacion de la biblioteca
from io import open
#Tenemos que decir la forma de abrirlo 
archivoTexto = open("archivo.txt","w") #Forma de abrir el archivo, w->escribir
frase = "A por el jueves "
archivoTexto.close()
#Tenemos que escribir en el archivo y luego cerrarlo, para que no de error

print("Se ha creado el archivo.txt")
