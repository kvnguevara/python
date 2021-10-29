class Vehiculo:
    def __init__(self,color,velocidad,marca):
        self.color = color
        self.velocidad = velocidad
        self.marca = marca
    
    def arrancar(self):
        print('Arrancado')
    def acelerar(self):
        if self.velocidad== 0:
            self.velocidad = 10
        else:
            self.velocidad +=10
        print(f"La velocidad ={self.velocidad}")
    def frenar(self):
        if self.velocidad > 10:
            self.velocidad -= 10
        else:
            self.velocidad = 0
        print(f"Velocidad={self.velocidad}")
    def estado(self):
        print(f"Marca: {self.marca}, Color:{self.color}, Velocidad Max:{self.velocidad}")

mi_vehiculo = Vehiculo('Negro',250,'Peugeot')
#informacion del primer Vehiculo
mi_vehiculo.estado()
mi_vehiculo.arrancar()
mi_vehiculo.frenar()
mi_toyota = Vehiculo("Blanco",250,'Toyota')
#informacion del segundo vehiculo
mi_toyota.estado()
