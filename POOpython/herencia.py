#En este documento, vamos a tratar la herencia.
#Principalmente, es la gran herrramiento en los lenguajes orientados a objetos.

#Vamos a crear la clase padre vehiculo. de el van a hereder los distintos métodos creados

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
        
class Moto(Vehiculo):
   hcaballito=""
   def caballito(self):
        hcaballito="Voy haciendo el Caballito"
   def estado(self):
       """[Sobrecarga del metodo estado, informado que la moto esta haciendo el caballito]
       """
       print("Marca: ",self.marca,"\nModelo: ",self.modelo,"\nEn Marcha: ",self.enmarcha ,"\nAcelaerando: ", self.acelera,  "\nFrenando: ",self.frena,"\n Caballito: ",self.hcaballito)
mi_moto=Moto("Honda","CBR")
mi_moto.estado();
        