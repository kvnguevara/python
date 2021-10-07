import pandas as pd
pd.set_option('display.date_dayfirst',True)
pd.set_option('display.date_yearfirst',False)
locExcel= (r"C:\Users\kguevara\Downloads\Libro3.xlsx")
localCSV = (r"C:\Users\kguevara\Desktop\PruebaCSV\csv\libroPruebas3.csv")
read_file = pd.read_excel (locExcel)
read_file.to_csv (localCSV,index = None, header=True, date_format='dd/MM/yyyy')
df=pd.DataFrame(pd.read_csv(localCSV))
df