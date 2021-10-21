import pickle
class Vehiculo():
    def __init__(self,marca,modelo):
        """Constructor de vehiculo

        Args:
            marca ([variable]): [Es la marca del vehiculo]
            modelo ([variable]): [Modelo del vehiculo]
        """
        self.marca = marca
        self.modelo = modelo
        self.enmarcha=False
        self.acelera=False
        self.frena=False
    
    def arrancar(self):
        """metodo para modificar el arrancar
        """
        
        self.enmarcha = True
        
    def acelera(self):
        """Metodo que cambia acelerar
        """
        self.accelera = True
    def frenar(self):
        """Metodo que cambia el estado de frenar
        """
        self.frena = True
    def estado(self):
        """[Muestra el estado del vehiculo]
        """
        print("Marca: ",self.marca,"\nModelo: ",self.modelo,"\nEn Marcha: ",self.enmarcha ,"\nAcelaerando: ", self.acelera,  "\nFrenando: ",self.frena)
        
coche1 = Vehiculo("Mazda","MX5")
coche2 = Vehiculo("Seat","Leon")
coche3 = Vehiculo("Renault","Megan")
coche4 = Vehiculo("toyota","Corolla")
#la meteremos en una lista 
lista_coche=[coche1,coche2,coche3,coche4]
#Abirmos el fichero de escritura
f= open("ficheroBinarioCoches","wb")
pickle.dump(lista_coche,f)
f.close()
del(f)
print("Fichero Creado...")

