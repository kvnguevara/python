import re
import numpy as np
import pandas as pd
from datetime import datetime,date, time
import string

locExcel= (r"C:\\Users\\kguevara\\Downloads\\Libro2.xlsx")
localCSV = (r"C:\Users\kguevara\\Desktop\PruebaCSV\csv\libro2ultimo.csv")

dateFormatters ="%d/%m/%Y"
formateador = string.Formatter()
datos = pd.read_excel (locExcel)
df = pd.DataFrame(datos)

#fechaProximaEntrevista= obj
#fecha_incorporacion =datatime64

# astype sirve para cambiar la fecha de los dataFrame 
df['fechaProximaEntrevista']=df['fechaProximaEntrevista'].astype(np.datetime64)
df['fecha_incorporacion']=df['fecha_incorporacion'].astype(np.datetime64)
# '%d/%m/%Y'

""" print("Fecha Entrevista:",df['fechaProximaEntrevista'])
print("Fecha incorporacion: ",df['fecha_incorporacion']) """

#df.fechaProximaEntrevista = pd.to_datetime(df.fechaProximaEntrevista).strftime(df.fechaProximaEntrevista, '%d/%m/%Y')
#df.fecha_incorporacion =  datetime.strptime(df['fecha_incorporacion'],'%d/%m/%Y')
""" print(df['fechaProximaEntrevista'].dtype)
print(df['fecha_incorporacion'].dtype)
 """

df.to_csv(localCSV,index=False,date_format='%d/%m/%Y')
print("Fichero Creado..")
df
