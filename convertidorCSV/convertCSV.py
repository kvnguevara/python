import numpy as np
import pandas as pd
from datetime import datetime,date
import openpyxl

locExcel= (r"C:\\Users\\kguevara\\Downloads\\Libro3.xlsx")
localCSV = (r"C:\Users\kguevara\\Desktop\PruebaCSV\csv\libroPruebas3.csv")

dateFormatters ="%d/%m/%Y"
#formateador = str.format()
datos = pd.read_excel (locExcel, index_col=0)
df = pd.DataFrame(datos)

#fechaProximaEntrevista= obj
#fecha_incorporacion =datatime64

#Para cambiar de tipo las columnas para
df['fechaProximaEntrevista']=pd.to_datetime(df['fechaProximaEntrevista'])
df['fecha_incorporacion']=pd.to_datetime(df['fecha_incorporacion'])




#df.fechaProximaEntrevista = pd.to_datetime(df.fechaProximaEntrevista).strftime(df.fechaProximaEntrevista, '%d/%m/%Y')
#df.fecha_incorporacion =  datetime.strptime(df['fecha_incorporacion'],'%d/%m/%Y')
print(df['fechaProximaEntrevista'].dtype)
print(df['fecha_incorporacion'].dtype)


print(df['fechaProximaEntrevista'])
print(df['fecha_incorporacion'])
print(df.head())

