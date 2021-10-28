#Dado una serie de numeros introducidos por comando, sacar la media con dos decimales
import sys
lista_numeros = sys.argv
lista_numeros.pop(0)
suma  = 0
cont = 0
for v,num in enumerate(lista_numeros):
    print(v, num)
    suma +=int (num)
   
print(f" Total {suma/len(lista_numeros):.2f}")