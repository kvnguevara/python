#ficheros con punteros seek()
from io import open
archivo_texto = open("archivo.txt","r+")
#archivo_texto.seek(11) #Posiciona el punto, es decir, empieza en dicha posicion
print(archivo_texto.seek(11))
#print(archivo_texto.read(11))