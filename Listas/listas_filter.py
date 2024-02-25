""" Ejercicio:
Dada una lista de números creadas de manera aleatoria, podemos hacer un filtro de los números pares
Número Par: Todo número es par cuando se divide entre dos, y el resto de la division es 0(cero)
Ejemplo: 10/2 = 5, y el resto es 0

Dada una lista de Nombres, se tiene que crear un filtro donde obtenga un lista de los nombres que comience con la 
letra A.
Para ello podemos usar la funcion stratwith( ), o accediendo a la primera posicion de la palabra [0] """

import random
if __name__=='__main__':
    random_numeros = [random.randint(1, 10000) for _ in range(100)]
    # Se filtra la lista de los números pares
    numeros_pares = list(filter(lambda x : x % 2 == 0, random_numeros))
    print(f" Numeros pares = {numeros_pares}")
    # Se filtra la lista de los números impares
    numeros_impares = list(filter(lambda x: x %2 !=0, random_numeros))
    print(f"Numeros Impares = {numeros_impares}")

    #Parte dos 
    nombres_lista = ["Anna", "Jose", "Carlos", "Arturo", "Migel", "Adolfo"]
    filtro_lista = list(filter(lambda x: x.upper().startswith("A"), nombres_lista))
    print(f"Lista de nombres = {filtro_lista}")
    filtro_nombres = list(filter(lambda x: x[0].upper() == "A", nombres_lista))
    print(filtro_nombres)


    ## Problemas que presenta esto
    # Si todos son minúsculas ?
    # Si estamos comparando con 'a'