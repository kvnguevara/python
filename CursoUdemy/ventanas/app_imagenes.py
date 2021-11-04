from tkinter import *
from PIL import ImageTk,Image
#Importamos o instalamos las librerias que nos hacen falta, como es Pillow, dentro de esta esta ImageTk,Image

ventana = Tk()
ventana.title("Imagenes en Python")
#Creamos una variable, done le asignamos la imagen, esa imagen tiene que ser añadida a una label
imagen = ImageTk.PhotoImage(Image.open("logoPython.jpg"))
img_lable = Label(ventana,image=imagen).grid(column=1,row=1)
ventana.mainloop()