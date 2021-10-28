#Listas de compresion,es una tecnica para crear listas basandose en el conecpto matematico de conjuntos definidos
#[<expresion> for <value> in <iterable> if condicion]
#Ejemplo
palabra ="1,2,1,33,454,47"
#forma con lista de compresion.
lista_numeros =[int(v) for v in palabra.split(",")]
print(lista_numeros)
#Lista de numeros que empiecen por el 4
#Lista de numeros que acaben por 0
values = '42,80,40,65,25,17,13,77,100' #42,40,
lista_num1 = [int(x) for x in values.split(',') if x.startswith('4')]#42,40
lista_num2 = [int(x) for x in values.split(',') if x.endswith('0')] #80,40,100
print(f"Lista de numeros, que comienza por 4: {lista_num1}")
print(f"Lista de numeros, que terminen por 0: {lista_num2}")

#Hacer una lista que comprenda  f(x)=3x+2  para x∈[0,20).
values = [3*x+2 for x in range(20)]
print(f"Valores: {values}")

#Sacar la serie de las posibles combinaciones de la lista
num = '32,45,11,87,20,48'
serie = [f'{v1}x{v2}'for v1 in num.split(',') for v2 in num.split(',')]
print(serie)