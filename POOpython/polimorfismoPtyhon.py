#Polimorfismo en python, ese objeto, puede cambiar de forma, cambiando de estado
#Es sencilla de utilizar de tipado dinamico, como no especificamos el tipo de dato en Python.
class Coche():
    
    def desplazamiento(self):
        print("Me desplazo utilizando 4 ruedas")
        
class Moto():
    
    def desplazamiento(self):
        print("Me desplazo con dos ruedas")
        
class Camion():
    
    def desplazamiento(self):
        print("Me desplazo utilizando 6 ruedas")
        
        
#Creo un metodo para imprimir el desplazamiento de los objetos y ver el polimorfismo
#Como podemos ver, no es necesario indicar el tipo de objetos.

def desplazamiento_vehiculo(vehiculo):
    """metodo para imprimir el desplazamiento de los vehiculos

    Args:
        vehiculo ([obj]): Objetos de tipos vehiculos, ya sea moto, coche o camion
    """
    vehiculo.desplazamiento()
        
mi_vehiculo = Moto()
desplazamiento_vehiculo(mi_vehiculo)

mi_vehiculo2 = Coche()
desplazamiento_vehiculo(mi_vehiculo2)

mi_vehiculo3 = Camion()
desplazamiento_vehiculo(mi_vehiculo3)