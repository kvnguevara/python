import io

#Abrir el archivo
archivo_texto = open("archivo.txt","a")
linea = input("Introduzca un texto: ")
archivo_texto.write("\n"+linea)
print("Se ha agregado info, nueva al archivo")

#Mostramos el archivo.txt"
archivo_texto = open("archivo.txt","r") #Para leer
lineas = archivo_texto.readlines()

index = 1
for  l in lineas:
    print(index,"  :",l)
    index+1
    
archivo_texto.close()
  
    