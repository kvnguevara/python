#Convertir o sustituir la siguiente cadena 12/31/20 a 31-12-2020
fecha = '12/31/20'.split("/")
nueva_fecha = '{}-{}-{{'20'}}'.format(fecha[1],fecha[0],fecha[2])
print(nueva_fecha)