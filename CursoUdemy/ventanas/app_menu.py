from tkinter import *
from tkinter import messagebox
def salir():
    opcion = messagebox.askquestion("Salir","¿Desea salir?")
    #print(opcion)
    if opcion == "yes":
        ventana.destroy()
ventana= Tk()
ventana.geometry("640x520")
#Hemos creado la barra de menu, luego hemos creado, los archivos, es decir, los item, de cada menu..
#Se añade cada menu a la barra 
barra_menu= Menu(ventana)
ventana.configure(menu=barra_menu)
menu_archive= Menu(barra_menu,tearoff=0)
menu_archive.add_command(label="Abrir")
menu_archive.add_separator()
menu_archive.add_command(label="Salir",command=salir)

menu_ayuda = Menu(barra_menu,tearoff=0)
menu_ayuda.add_command(label="Ayuda")
menu_ayuda.add_separator()
menu_ayuda.add_command(label="Salir")

#Se añade los menus a la barra
barra_menu.add_cascade(label="Archivo",menu=menu_archive)
barra_menu.add_cascade(label="Ayuda",menu=menu_ayuda)
ventana.mainloop()