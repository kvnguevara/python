from concurrent.futures import ThreadPoolExecutor

def tarea(nombre):
    print(f"Iniciando {nombre}")
    return f"Resultado de {nombre}"


if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=2) as executor:
        futuros = [executor.submit(tarea, f"Tarea {i}") for i in range(5)]
        for futuro in futuros:
            print(futuro.result())