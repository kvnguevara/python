#Manipulacion de obtener datos con JSON
import json 
from urllib import request

url = 'https://my.api.mockaroo.com/personas.json?key=ca8d8da0'
respuesta = request.urlopen(url)
#print(respuesta)
contenido = respuesta.read() #Leemos la repuesta que obtenemos de la conexión a la appi
#print(contenido)
#Para obtemer eñ JSON, de forma que conozcamos los acentos, y demás.
#Tenemos que descodificarlo, con json.loads(contenido.decode(utf-8))
json_obtenido = json.loads(contenido.decode('utf-8'))
#print(json_obtenido)
#Presentarlo en consola, o maquetar los datos obtenidos
#Recorremos el objeto json, con el bucle for y maquetamos la información a mostrar

for persona in json_obtenido:
    print("############################")
    print(f"Nombre: {persona['nombre']}\nApellidos: {persona['apellidos']} \nMail: {persona['email']}")
    print("############################")
    print()