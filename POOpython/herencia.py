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


class Furgonetar(Vehiculo):
    """[Clase Furgoneta, que hereda de Vehiculo]

    Args:
        Vehiculo ([Class]): Clase padre que le hereda sus atributos y sus metodos
    """
    def carga(self,cargar):
        self.cargado=cargar
        if(self.cargado):
            return "La furgoneta esta cargada"
        else: 
            return "La furgoneta no esta cargada"
class VElectricos(Vehiculo):
    """Clase de vehiculos Electricos, que no hereda de vehiculos
    """
    
    def __init__(self,marca,modelo):
        """Constructor 
        """
        super().__init__(marca,modelo)
        self.autonomia=1000
        
        
        
    def cargarEnergia(self):
        self.cargando=True
        
#En python existe la herencia multiple, para hacerlo, tenemos que poner las class padres con comas.
#Python le da prioridad al constructor de la izquierda BicicletaElectrica(VElectricos,Vehiculo)--> el constructor por defecto, sería el de VElectricos
class BicicletaElectrica(VElectricos):
    pass
    
            
        
        
print("-----------------------Moto---------------------")       
mi_moto=Moto("Honda","CBR")
mi_moto.caballito()
mi_moto.estado()
print("---------------------Furgoneta-------------------")
mi_furgoneta=Furgonetar("Ranault","Kango")
mi_furgoneta.arrancar()
mi_furgoneta.estado()
print(mi_furgoneta.carga(True))

print("---------------Coches electricos----------------")
mi_bicicleta=BicicletaElectrica("orbea","Ihj")
mi_bicicleta.estado() #Metodo que es heredado por la clase padre, que muestra el estado de los vehiculos
        