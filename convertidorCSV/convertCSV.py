import re
import numpy as np
import pandas as pd
from datetime import datetime,date
import openpyxl

locExcel= (r"C:\\Users\\kguevara\\Downloads\\Libro3.xlsx")
localCSV = (r"C:\Users\kguevara\\Desktop\PruebaCSV\csv\libroPruebas3.csv")

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
print(df['fechaProximaEntrevista'].dtype)
print(df['fecha_incorporacion'].dtype)


print(df[['fechaProximaEntrevista','fecha_incorporacion']])

#voy a crear una nueva columma en el dataFrame para agreagar los comentarios
#que ya están formateados
#tengo que establecer un patron para que cumpla dichos complementarios:
list_caracteres = ['.','•','-']
expr_regular='[' +re.escape('\n'.join(list_caracteres))+']'

df['nuevos_comentarios']=
df1 = df['nuevos_comentarios']
print(df['nuevos_comentarios'])
print(df)
df1.to_csv(localCSV,index=False)
df1
df
