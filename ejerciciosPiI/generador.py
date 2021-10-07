#Funcionamiento de los generadores en python
#Son funciones que están devolviendo valores de uno en uno, donde se puede
#intenerar o manejar dicho generadores.
#El tiempo que tarda es menor, la reserva de memoria también es menor 
#Los acceso de datos son muchos más rápidos
# def genereaNumeros():
# yield numeros (se parece a return)

def generarPares(limite):
    """ Funcion para Generar Pares"""
    num = 1 
    milista=[]
    while num < limite:
        milista.append(num*2)
        num+= 1
    
    return milista
print(generarPares(10))


#El generador nos de va devolver los numeros pares, es decir, que devolvera 1 en 1
#Por eso no necesitamos la lista 
def genePares(limite):
    num=1
    while num<limite:
        yield num*2
        num+=1
devuelvePares = genePares(10)
#for i in devuelvePares:
 #   print(i, end=";")
#Para poder sacar de uno en uno, podemos ver su funcionamiento
# Si queremos ver el funcionamiento
print(next(devuelvePares))
print("Pausa...")
print(next(devuelvePares))
print("Pausa.....")
print(next(devuelvePares))

#Como podemos ver solo accedemos a los 3 primeros numeros, y por tanto no consumimos recurso