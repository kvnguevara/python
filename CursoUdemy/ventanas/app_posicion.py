#Para darle formato a las ventas, posicionar la ventan de la app
#Mostrar información, que le solicitamos al usuario.
from tkinter import *

#constantes para ventana
ANCHO =600
ALTO = 400
POSX = 300
POSY = 100

anchoAlto=str(ANCHO)+"x"+str(ALTO)
eje_x= ""+str(POSX)
eje_y=""+str(POSY)
ventana = Tk() #Crear ventana 
#configurar ventana 
ventana.title("App-python")
ventana.resizable(True, True)

#Ubicacion de la ventana
ventana.geometry(anchoAlto+eje_x+eje_y)

#Configuracion del frame
frame = Frame()
frame.pack(side="top",anchor="s")
frame.config(bg="yellow")
frame.config()

#variables a utlizar
nombre = StringVar()
edad = IntVar()
#Etiquetas
label_nombre= Label(frame,text="Nombre",font=("Arial",12))
label_nombre.grid(column=1,row=2)
label_edad = Label(frame,text="Edad",font=("Arial",12))
label_edad.grid(column=1,row=3)
#texto
txt_nombre=Entry(frame,textvariable=nombre,width=50)
txt_nombre.grid(column=2,row=2)
txt_edad = Entry(frame,textvariable=edad,width=50)
txt_edad.grid(column=2,row=3)
edad.set(15)

#Mostrar ventana 
ventana.mainloop()