import os
import shutil
from concurrent.futures import ThreadPoolExecutor

def copiar_archivo(ruta_origen, ruta_destino, fichero):
    print(f"Inicializando la copia de Ficheros {fichero}")
    path_origen = f"{ruta_origen}\{fichero}"
    path_destino = f"{ruta_destino}\{fichero}"

    if os.path.exists(path_origen):
        shutil.move(path_origen, path_destino)
        print(f"Archivo copiado de '{path_origen}' a '{path_destino}'.")
    else:
        print(f"El archivo '{path_origen}' no existe.")


if __name__ == "__main__":
    print("Creando ficheros")

    # Uso de la función
    ruta_origen = r"C:\Users\kevin\Documents\RepositorioKvn\python"
    ruta_destino = r"C:\Users\kevin\Documents\RepositorioKvn\python\copiarFicheros"

    # Crear la carpeta de destino si no existe
    os.makedirs(os.path.dirname(ruta_destino), exist_ok=True)
    with ThreadPoolExecutor(max_workers=2) as executor:
        futuros = [executor.submit(copiar_archivo, ruta_origen, ruta_destino, f"Fichero{i}.txt") for i in range(950)]
        for futuro in futuros:
            print(futuro.result())
