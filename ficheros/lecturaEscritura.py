from io import open

archivo_texto = open("archivo.txt","r+")
#print(archivo_texto.readlines())

#Vamos a poner una linea en la mitad
lineas = archivo_texto.readlines()
lineas[1] = "Ojo que nos queremos que se concatene...\n"

#Ahora nos posicionamos al principipo del archivo, para hacer un volcado

archivo_texto.seek(0) #Posicion 0, del fichero

archivo_texto.writelines(lineas) #Hacemos el volcado
#cerramos el fichero 
archivo_texto.close()
print("El archivo se ha modificado")

