from tkinter import *
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
etiqueta = Label(frame,text="Etiqueta")
etiqueta.pack()
#Para indicar en un lugar 
etiqueta.grid(column=1,row=2)

#Segunda etiqueta 
etiqueta = Label(frame,text="Volvemos en seguida")
etiqueta.grid(column=1,row=2)


ventana.mainloop()