import numpy as np
import pandas as pd
from datetime import datetime,date
import openpyxl

locExcel= (r"C:\\Users\\kguevara\\Downloads\\Libro3.xlsx")
localCSV = (r"C:\Users\kguevara\\Desktop\PruebaCSV\csv\libroPruebas3.csv")

dateFormatters ="%d/%m/%Y"
datos = pd.read_excel (locExcel, index_col=0)
df = pd.DataFrame(datos)

#Para cambiar de tipo las columnas para
df.astype({'fechaProximaEntrevista':'str','fecha_incorporacion':'str'})
#df.fechaProximaEntrevista = df.fechaProximaEntrevista.strptime('%d/%m/%Y')
#df.fecha_incorporacion = pd.to_datetime(df["fechaProximaEntrevista"].astype(str), '%x')

#df.fechaProximaEntrevista = pd.to_datetime(df.fechaProximaEntrevista).strftime(df.fechaProximaEntrevista, '%d/%m/%Y')
df.fecha_incorporacion =  datetime.strptime(str(df['fecha_incorporacion']), '%d/%m/%Y')
print(df['fechaProximaEntrevista'].dtype)
print(df['fecha_incorporacion'].dtype)

#Para convertir un cadena a objeto datatime64, que es la fecha que utiliza pandas
"""df['fechaProximaEntrevista'].strftime(df['fechaProximaEntrevista'], errors="coerce", format='%d/%m/%Y')
df['fecha_incorporacion'].strftime(df['fecha_incorporacion'], errors="coerce", format='%d/%m/%Y') """

fecha = datetime.now().strftime(format='%d/%m/%Y')
print(df['fechaProximaEntrevista'])
print(df['fecha_incorporacion'])
print(fecha)
print(df.head())
#print(pd.to_datetime(fecha, format='%Y-%d-%m'))
