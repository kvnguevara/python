import pandas as pd
from datetime import datetime,timedelta
from openpyxl.reader.excel import load_workbook
locExcel= (r"C:\Users\dperezs\Desktop\TrabajoPython\primero\LibroUltimo.xlsx")
localCSV= (r"C:\Users\dperezs\Desktop\TrabajoPython\primero\LibroUltimo.csv")
libro = load_workbook(locExcel)
hoja = libro.active
df = pd.read_excel (locExcel)
c = 0
for x in df['Resumen_candidato']:
    flag = False
    t = 0
    for y in x:
        if str(y) == "-" or str(y)=="\n" or str(y)=="•" or str(y)=="o":
            #print("ENTRANDOOOOOOO")
            flag = True
            t = t +1
    if flag != False:
        print("ID: ",str(c))
        print("///////--AQUI NO HAY GUIONES---//////")
        print("GUIONES: ",str(t))
        print(x)
        '''
        pal = "Q"+ str(c)
        hoja[pal]="valor"
        libro.save()'''
    c = c +1
