import pickle
from io import open
 
fb = open("ficheroBinario","rb") 
lista = pickle.load(fb)
print(lista)