#ejercicio hay que eliminar los duplicados de las lista y ordendarlas de menor a mayor
# Hay que hacerlo de la manera más optima posible.

def delete_duplicate_list(arr1, arr2)->list:
    # hay que unificar las lista
    # Hay que ordenar la  lista
    return sorted(set(arr1 + arr2))



if __name__=='__main__':

    lista_numeros = [1,2,3,4,4,6,8]
    lista_numeros2 = [5,10,15,8,20,1]
    #Mostramos la informacion
    print(f"Lista ordenada {delete_duplicate_list(lista_numeros, lista_numeros2)}")
    # x = round(14.9,-1)
    # print(x)