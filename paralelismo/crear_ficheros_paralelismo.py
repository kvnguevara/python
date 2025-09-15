import os
from concurrent.futures import ThreadPoolExecutor

def crear_fichero(nombre_fichero):
    """ Funcion que crea los ficheros """
    print(f"Iniciando la creación del {nombre_fichero}")
    #Creamos los ficheros
    with open(nombre_fichero,'w') as arch:
        arch.write("")
    print(f"Tarea Finalizada, {nombre_fichero} creado...")

if __name__ == "__main__":
    print("Creando ficheros")
    with ThreadPoolExecutor(max_workers=2) as executor:
        futuros = [executor.submit(crear_fichero, f"Fichero{i}.txt") for i in range(950)]
        for futuro in futuros:
            print(futuro.result())
