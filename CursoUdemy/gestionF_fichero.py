import os 
carpeta = r'D:\RespositoryPython\python\CursoUdemy\archivos'
#imprimimos para saber los archivos 
print(carpeta)
listado = os.listdir(carpeta)
print(listado)
print(type(listado))
#Filtrado de archivos, buscar por un tipo de extensión
for x in listado:
    if x.endswith(".pdf"):
        print("fichero encontrado!!")
        print(f"Nombre del fichero: {x}")
#Otra forma de filtra
filtrado =[ x for x in listado if x.endswith(".txt")]
print(type(filtrado))
print(filtrado)
#cambio de directorio
os.chdir(r'D:\RespositoryPython\python\CursoUdemy\archivos')
#Renombra archivos ("nombre archivo","nuevonombre")
#os.rename('documento - copia.txt',"renombrado1.txt")
#Para borrar un archivo
#os.remove('documento - copia (2).txt')
#Renombrar varios archivos a la vez
# cont=1
documento="documento"
""" for x in os.listdir():
    nombre,extension = os.path.splitext(x)
    print(nombre, extension)
    nuevo_nombre=f'{str(cont)}-{documento}{extension}'
    cont+=1
    os.rename(x,nuevo_nombre)
listado = os.listdir(carpeta); """
print(listado)