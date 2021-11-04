from tkinter import *

#Funcion para controlar el evento click del boton
def click():
    texto = "Hola, "+txtbox.get()
    etiqueta.configure(text=texto)

#Config basica de las ventana
ventana = Tk() #Para cargar la venta 
ventana.title("App Widgets Basicos") #titulo
ventana.resizable(True,True) #Renderizar
ventana.config() #Configura la ventana
frame = Frame() #crear el frame
frame.pack() #
frame.config()
frame.config(width="640",height="320") #darle ancho y largo al frame

#etiquetas
etiqueta = Label(frame,text="App-Python",font=("Ariak",25)) #Para darle valor al label
#etiqueta.grid(column=1,row=2)
#Para indicar en un lugar 
etiqueta.grid(column=1,row=2)

#textbox, caja 
txtbox= Entry(frame,width=22)
txtbox.grid(column=2,row=2)

#Botenes
btn_aceptar = Button(frame,text="Aceptar",bg="blue",fg="yellow",command=click)
btn_aceptar.grid(column=1,row=4)


ventana.mainloop()