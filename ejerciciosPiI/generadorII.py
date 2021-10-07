#Generador con yieldfrom
#Sería como los arrays bidemensionales.
#Un for para controlar el pader, y el otro para controlar los hijos o elementos

def devuelve_cuidades(*argv):
    """ Devuelve las cuidades, *ciudades en la funcion nos esta 
    dediendo, que le pasare una serie de argumentos """    
    for elemento in argv:
            yield  from elemento
        
cuidades_devueltas=devuelve_cuidades("Madrid","Barcelona","Alicante","Valencia","Salamanca",)
print(next(cuidades_devueltas))
print("Pausa--------")
print(next(cuidades_devueltas))
print("pausa---------")
#Como podemos observa con  yield from, es como hacer un for dentro de otro for 