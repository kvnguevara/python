class Coche():
    #Constructores en python se define de __init__ es el estado inicial del
    #Encapsula es proteger las propiedas del objeto/clase, y así no puedan manipularas desde fuera de 
    #Clase
    
    #Para ello vamos a encapsular las propiedas de Coche __(dos guines bajos)
    def __init__(self):
        """Constructor por defecto de la clase coche"""
        self.__largoChasis=250
        self.__anchoChasis=120
        self.__ruedas=4
        self.__enmarcha=False        
   
    def arrancar(self,arrancamos): #Hace referencia a la instancia referencia al objeto
        #es igual a this, hacer referencia al objeto
        self.__enmarcha=arrancamos
        if(self.__enmarcha):
            chequeo=self.__chequeo_interno()
            
        if(self.__enmarcha and chequeo):
            return "El coche esta en marcha"
        elif(self.__enmarcha and chequeo==False):
            return "algo ha ido mal en el chequeo, no podemos arrancar"
        else:
            return "el coche esta parado "
    def estado(self): #Hace referencia a la instancia
        """Funcion donde nos indica la info del coche"""
        print("El coche tiene ",self.__ruedas," ruedas. Un ancho de ", self.__anchoChasis,
              " y un largo de  ",self.__largoChasis)
    #Meotod para saber que le hace falta en el coche 
    def __chequeo_interno(self): #Encapsulado de una funcion 
        """Metodo que nos indica si falta algo, en esto vemos que es una
        funcion encapsulada, que solo se puede llamar desde la propia clase y no de fuera"""
        print("Chequeo interno----")
        self.gasolina ="ok"
        self.aceite = "ok"
        self.puertas="cerradas"
        if (self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas"):
            return True
        else :
            return False
        
        
    
miCoche=Coche()
print(miCoche.arrancar(True))
miCoche.estado()

print("--------------------Segundo coche(objeto)----------------")
miCoche2=Coche()
print(miCoche2.arrancar(True))
miCoche2.ruedas=5 #Esto no se podría dejar, ya que hay ciertas propiedas tiene que estar ocultas.
#Python ve como si fuera otra variable 
miCoche2.estado()
print()