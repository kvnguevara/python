from io import open
archivo_texto = open("archivo.txt","r")
texto = archivo_texto.readlines()
archivo_texto.close()
for h in texto:
    print(h)