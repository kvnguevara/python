#Los bucles en python son los siguientes:
#Tenemos for, se utiliza cuando sabes el numero de iterraciones que hara el programa
# bucle while: cuando no sabes cuantas iterraciones hara, pero si tenemos las herramientas para
#poder pararlo.
#For for variable in elemento a recorrer(rango)

def mostrarFor(num):
    for i in range(num):
        print(i,"x",num,"=",i*num)

print("Programa For")
numero = int(input("Introduzca el numero:"))
mostrarFor(numero)

#Mostrar Hola 
def imprimirHola():
    words = ['cat','window','elefante']
    for i in words:
        print(i,len(i))
imprimirHola()
#Comprobar un mail con for 
mail = False
for i in "kevinguevaracarrasco120@gmail.com":
    if(i=="@"):
        mail=True
if mail==True:
    print("El Mail es correcto")
else:
    print("El mail no es correcto")
    
print("@" in "kevinguevaracarrasco120@gmail.com")