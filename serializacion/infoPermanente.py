import pickle

class Persona:
    def __init__(self,nombre,genero,edad):
        self.nombre = nombre
        self.genero = genero
        self.edad = edad
        print("Se ha creado una persona nueva: ", self.nombre)
    
    def __str__(self):
        return " {},{},{}".format(self.nombre, self.genero, self.edad)

class ListaPersona:
    personas = []
    def __init__(self):
        listPersona = open("ficheroexterno","ab+")
        listPersona.seek(0)
        
        try:
            self.persona = pickle.load(listPersona)
            print("Se cargo {} personas del fichero externo".format(len(self.personas)))
        except:
            print("El fichero esta vacio")
        finally:
            listPersona.close()
            del(listPersona)
    
    def agregar_personas(self,p):
        self.personas.append(p)
        self.guardar_fichero()
        
    def mostrar_personas(self):
        for p in self.personas:
            print(p)
            
    def guardar_fichero(self):
        listPersona = open("ficheroexterno","wb")
        pickle.dump(self.personas,listPersona)
        listPersona.close()
        del(listPersona)
        
    def mostra_infoFichero(self):
        print("-----------INFO--------------")
        for p in self.personas:
            print(p)
        
miLista = ListaPersona()

p = Persona("Loreana","Femenino",33)
miLista.agregar_personas(p)

p1 = Persona("Victoria","Femenino",63)
miLista.agregar_personas(p1)
miLista.mostra_infoFichero()

p2 = Persona("Corina","Femenino",53)
miLista.agregar_personas(p2)
miLista.mostra_infoFichero()

p3 = Persona("Alejandra","Femenino",30)
miLista.agregar_personas(p3) 
miLista.mostra_infoFichero()
#Se creara una lista para luego se añade al fichero externos