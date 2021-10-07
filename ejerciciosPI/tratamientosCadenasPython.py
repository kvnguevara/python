#Una de las cosa que tiene python, es el tratamiento que le da a las cadenas
#Podemos observar, que cadena cadena, los trata como si fueran arrays de string.
#Vamos a observar, que podemos utilizar valores negativos en arrays de string en python


cadena  = "Python"

#Vamos a mostrar los dos ultimás letras de la cadena, que sería on
#Se puede hacer de dos maneras
print(cadena[3:]) #Esta es una forma indicar el lado negativo que queremos , cogera hasta el el numero maximo de la
#Cadena
print(cadena[4:]) #[0:4], es decir, desde una posicion incial, que sería cero hasta el final
#para saber la longitud de la cadena, tenemos la funcion len()
print(len(cadena))
#Nota muy importante las cadenas de texto, no se puede reemplazar, tendríamos que crear otra cadena
cadena[0] = 'j'
print(cadena)