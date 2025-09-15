from concurrent.futures import ProcessPoolExecutor

def calcular_cuadrado(n):
    return n * n


if __name__ == "__main__":
    print("Se inicia el Proceso de Paralelismo")
    with ProcessPoolExecutor() as executor:
        resultados = executor.map(calcular_cuadrado, range(5))
        print(list(resultados))
