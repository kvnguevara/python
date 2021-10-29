import sqlite3 

def conectar():
    conexion = sqlite3.connect("miBD.db") #Conecta con la base de datos o la crea
    cursor = conexion.cursor() #Establecemos la conexion
    return conexion, cursor #retorna en una tupla conexion y cursor

def crearTabla():
    conexion,cursor= conectar()
    sql = """
        CREATE TABLE IF NOT EXISTS agenda(
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            nombre VARCHAR(20) NOT NULL,
            telefono VARCHAR(14) NOT NULL            
        )
    """
    if(cursor.execute(sql)):
        print("tabla creada")
    else:
        print("No se ha creado la tabla")
    conexion.close() #Cierre de la conexion
    
def insert(datos):
    conexion, cursor = conectar()
    sql = """ 
    INSERT INTO agenda(nombre,telefono) VALUES (?,?)
    """
    if(cursor.execute(sql,datos)): 
        print("Datos Guardados")
    else:
        print("No se pudo guardar datoss")
    conexion.commit() #los datos guardos y actualizar    
    conexion.close()
def consultar():
    #establecemos la conexion
    conexion, cursor =conectar()
    cursor.execute("SELECT * FROM agenda")
    for f in cursor:
        print(f"ID: {f[0]} \nNombre:{f[1]}\nTelefono: {f[2]}\n")
    conexion.close()
#Modificar datos 
def modificar(id, telefono):
    #Muy importante, siempre poder establecer la conexion con la BBDD
    #Cerrar el cursor, siempre que sea actualización 
    #Hacer el commit, para actualizar la BBDD
    #Cerrar la conexion
    conexion,cursor = conectar()
    sql = "UPDATE agenda SET telefono="+telefono+" WHERE id="+id
    cursor.execute(sql)
    cursor.close()
    conexion.commit()
    conexion.close()
def borrar(id):
    #Conexion
    #ejectumos la consulta
    #Hacemos commit
    #Cerramos conexiones(conexion, cursos)
    conexion,cursor = conectar()
    sql = "DELETE FROM agenda WHERE id=+"+id
    cursor.execute(sql)
    cursor.close()
    conexion.commit()
    conexion.close()
    
crearTabla()
#Insertar Datos en nuestra BBDD
# datos = ("Jenifer","923257899")
# insert(datos)
# datos = ("Judith","923454578")
# insert(datos)
#Modificar
modificar("4","92354000")
consultar()
borrar("3")
consultar()


