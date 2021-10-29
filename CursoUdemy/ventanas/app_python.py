from tkinter import *
#con la libreria tkinter, se hace las ventanas en Python

ventana = Tk()
ventana.title("App Python") #Añadir el titulo
#tenemos que darle los layout
ventana.resizable(True, True) #Para indicar horizaontal, vertical
#Cambio de icono 
#  ventana.iconbitmap("icon.ico")
# #establecer alto y ancho
# ventana.geometry("640x360")
ventana.config(bg="#832561")  #Establecer los colores
frame = Frame()
frame.pack(side="bottom",anchor="n") #para poder el frame en la izquierda...left,right,bottom
frame.config(bg="white")
frame.config(width="640",height="360")



ventana.mainloop() #Para que la ventana este escuchando

