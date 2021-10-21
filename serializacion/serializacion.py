#importar la libreria 
import pickle

lista_nombres = ["Pedro","Ana","Maria","Juan"]

fichero_binario = open("ficheroBinario","wb")  #Abrir el fichero binario

#hacemos el volcado al fichero
pickle.dump(lista_nombres,fichero_binario)

print("Se realizado el volcado")


