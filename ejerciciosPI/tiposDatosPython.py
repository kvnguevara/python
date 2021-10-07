#En este programa vamos a ver Tipos de operadores y variables 
#Los tipos de Datos en python son:
# 1. Numericos-->  Enteros(int) , Coma Flotante(float) Complejos
# 2. Textos--> "", '', pueden ir den cualquier manera
# 3. Booleanos--> false(falso)/true(verdadero)
# 4 Comparación (==), (!=), (>),(<),(<=),(=<)
# 5.Logicos AND, OR XOR
# 6. Asignación Igual (=), Incremento (+=), Decremento(-=)
#  /= divison, **, %= resto,//=
#  7 Especiales: IS, IN, IS NOT, NOT IN 
# 8. La funcion para redonder los numeros es round(numero,nº decimal)


#Para saber el tipo de valor de una variable, tenemos la funcion type para realizar dicha funcion.
#Con está función podemos decir, que Python es un lenguaje Objetos, todo lo trata como si fuera objetos
#El uso de las 3 comillas (" " "), lo utlizamos para hacer los saltos de lineas

print("Esto es una suma 5+6=",(5+6))
print("Esto es una resta 14-4 = ",(14-4))
print("Esto es un Division 10/2 = ",(10/2))
print("Esto es una multiplicación 4 x 4 =",(4+4))
print("Exponen 5^3 = ",(5**3))
print("La division entera 9/2 = ",(9//2))

#Declaracion de variables
nombre = "Armando Carrasco"
suma  = 5+9
suma =9.4
suma = """ Esto es un mensaje con 
3 saltos de lineas
por eso, utilizamos las tres comillas """
print(type(nombre))
print(type(suma))
print(type(suma))
print(suma)
print(round(3.756,2))
print("-----------------------")

#String/ cadenas en python, tiene muchas funcionalidades.
# Podemos observar, que una cadena de caracteres, la gestiona directamente como array de String,
# Además los arrays de String, podemos darles números negativos, para leerlos al reves

cadena  = "Python"
print(cadena[1:4])  
