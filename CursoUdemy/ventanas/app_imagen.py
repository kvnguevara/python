from tkinter import *

ventana = Tk()
ventana.title("Imagenes")
ventana.geometry("100x100")
frame = Frame()
frame.pack()

#scroll en python 
scroll=Scrollbar(frame)
scroll.pack(side=RIGHT,fill=Y)

#Texto
txt =Text(frame)
txt.configure(width=50,height=50,bg="#f9e64f")
txt.pack(expand=YES,fill=BOTH)
txt.insert(0.0,"Escriba Aquí:")
txt.configure(yscrollcommand=scroll.set)
scroll.configure(command=txt.yview())
#abrimos ventana
ventana.mainloop()
