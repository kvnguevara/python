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
        
f = open("ficheroBinarioCoches", "rb") 
misCoches = pickle.load(f)
f.close()
for c in misCoches:
    print(c.estado)
        
del(f)