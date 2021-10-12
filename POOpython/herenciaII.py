#En este caso vamos a usar el constructor super(), para llamar al constructor padre.
#isinstance()--> para saber si pertenece a una clase determinada
class Persona():
    #La clase persona, tendra nombre, edad, y dirrecion 
    
    def __init__(self, nombre, edad, lugar_residencia):
        """constructor

        Args:
            nombre ([string]): Nombre de la persona
            edad ([int]): edad de la persona
            lugar_residencia ([string]): [dirrecion]
        """
        self.nombre = nombre
        self.edad = edad
        self.lugar_residencia = lugar_residencia
    
    def descripcion(self):
        print("Nombre: ",self.nombre," Edad: ",self.edad," Lugar: ",self.lugar_residencia)

class Empleado(Persona):
    
    def __init__(self, salario, antiguedad, nombre, edad, lugar_residencia):
        """constructor de Empleado

        Args:
            salario ([int]): [salario del empleado]
            antiguedad ([int]): [cuantos años lleva en la empresa]
        """
        super().__init__(nombre, edad, lugar_residencia) #Pasamos los datos de la persona al constructor padre
        
        self.salario = salario
        self.antiguedad = antiguedad
        
    def descripcion(self):
        """sobrecarga del metodo descripcion del metodo padre
        """
        super().descripcion() #Llamada al metodo super de la clase padre
        print("Salario: ",self.salario," Antiguedad :",self.antiguedad)
        
antonio = Empleado(1500,15,"Antonio Fuente",55,"España")
antonio.descripcion()
manuel = Persona("Manuel",28,"España")

print(isinstance(antonio, Persona)) #Para saber si un objeto, pertenece a una clase.
print(isinstance(manuel,Empleado))
    