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
            return "El coche esta en marcha"
        else:
            return "el coche esta parado "
    def estado(self): #Hace referencia a la instancia
        """Funcion donde nos indica la info del coche"""
        print("El coche tiene ",self.__ruedas," ruedas. Un ancho de ", self.__anchoChasis,
              " y un largo de  ",self.__largoChasis)
        
    
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