#Vamos a ver los condicionales en python
print("Programa de evaluacion de notas de alumnos")

#Cualquier valor o cosa que nosotros introduzcamos a traves de consola, o input
#por eso utilizamos int() para convertir en parametro entero
nota_alumno = int(input("Introduce la nota del alumno:"))
def evaluacion(nota):
    valoracion = "aprobado" #Ambito de las variables, para las constantes, globales, tiene que ir en 
    #un clase o archivo python, que este allí y luego importarlas
    if nota < 5:
        valoracion = "suspenso"
    return valoracion

print(evaluacion(nota_alumno))