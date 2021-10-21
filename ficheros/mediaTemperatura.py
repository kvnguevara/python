from io import open
#ejercio leer el fichero de temperaturas, y sacar la media de cada mes 
#escrbir las temp media en un fichero..avgtemps.txt


list_media=[]
dias = 0
suma =0
##Lectura del fichero temperaturas
with open("temperatures.txt","r")  as f: 
    for line in f:
        arrTemp = [int (line)  for line in line.strip().split(',')]
        suma =sum(arrTemp)
        list_media.append(suma / len(arrTemp))
with open("avgtemps.txt","w") as f: 
       for media in list_media:
           f.write(str(media)+"\n")
print("Se ha creado el fichero avgtemps.txt")