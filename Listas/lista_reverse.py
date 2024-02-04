""" Ejercicio de práctica
    Dada una lista de numeros enteros o cadena de string, tenemos que dar la vuelta, este ejercicio 
    no se recomienda los métodos que tiene python, para dar vuelta a las listas
    Ejemplo: lista_numeros [1, 2, 3, 4, 5, 6] -> método reves: [6, 5, 4, 3, 2, 1]
    Realice los metdos que sean necesario
    """

def list_reverse(lista_numeros):
    return lista_numeros[::-1]

def other_reverse(lista_numeros):
    return [x for x in range(len(lista_numeros), 0,-1)]

if __name__ == '__main__':
    lista_numeros = [1, 2, 3, 4, 5, 6]
    print(f'{list_reverse(lista_numeros)}')
    print(f'Other_Reverse {other_reverse(lista_numeros)}')
