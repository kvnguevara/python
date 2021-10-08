#ejercico para evaluar la edad y controlar las excepciones
#Novedad raise TypeError...."para controlar otra forma "

def evaluaEdad(edad):
    
    if edad < 0:
        raise TypeError( "Edad no permitida")
    if edad<20:
        return "eres muy joven"
    elif edad<40:
        return "eres joven"
    elif edad<65:
        return "Eres maduro"
    elif edad <100:
        "cuidate..."
        
print(evaluaEdad(-15))
print("continuacion del programa")