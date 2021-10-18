import re
import numpy as np
import pandas as pd
from datetime import datetime,date
import openpyxl

locExcel= (r"C:\\Users\\kguevara\\Downloads\\LpComentarios.xlsx")
localCSV = (r"C:\Users\kguevara\\Desktop\PruebaCSV\csv\lppruebas.csv")

dateFormatters ="%d/%m/%Y"
#formateador = str.format()
datos = pd.read_excel (locExcel)
df = pd.DataFrame(datos)

#fechaProximaEntrevista= obj
#fecha_incorporacion =datatime64

#Para cambiar de tipo las columnas para
df['fechaProximaEntrevista']=pd.to_datetime(df['fechaProximaEntrevista'])
df['fecha_incorporacion']=pd.to_datetime(df['fecha_incorporacion'])
# '%d/%m/%Y'




#df.fechaProximaEntrevista = pd.to_datetime(df.fechaProximaEntrevista).strftime(df.fechaProximaEntrevista, '%d/%m/%Y')
#df.fecha_incorporacion =  datetime.strptime(df['fecha_incorporacion'],'%d/%m/%Y')
""" print(df['fechaProximaEntrevista'].dtype)
print(df['fecha_incorporacion'].dtype)
 """

df['Resumen_candidato'] = df['Resumen_candidato'].str.replace('.', '\n', regex=True)
#print(df['nuevos_comentarios'])
df.to_csv(localCSV,index=False)
print("Fichero Creado..")
df
