import openpyxl 
import csv 
import pandas as pd 

locExcel= (r"C:\Users\kguevara\Downloads\Libro3.xlsx")
localCSV = (r"C:\Users\kguevara\Desktop\PruebaCSV\csv\libroPruebas.csv")
  
excel = openpyxl.load_workbook(locExcel, data_only=True) 
  
sheet = excel.active
  
col = csv.writer(open(localCSV, 
                      'w', 
                      newline="") )
  
for r in sheet.rows:      
     col.writerow([cell.value for cell in r])
  
df = pd.DataFrame(pd.read_csv(localCSV)) 
  
df