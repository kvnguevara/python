from tkinter import *

def click():
    txt_resultado = "Pulsado: "
    if color01.get():
        txt_resultado +='Rojo'
        ventana.configure(bg="red")
    elif color02.get():
        txt_resultado +='Azul'
        ventana.configure(bg="blue")
    elif color03.get():
        txt_resultado += 'Amarillo'
        ventana.configure(bg="yellow")
    elif (not color01.get() and not color02.get() and not color03.get()): #Para validar que no se ha seleciconado nada 
        txt_resultado += 'No se ha selecionado'
        ventana.configure(bg="white")  
    label_resultado.configure(text=txt_resultado)
    
ventana  = Tk()
ventana.title("App con RadioButton")
ventana.geometry("640x400")
frame = Frame()
frame.pack()

color01 = IntVar()
color02 = IntVar()
color03= IntVar()

chk_rojo= Checkbutton(frame,text="Rojo",variable=color01,onvalue=1,offvalue=0,command=click)
chk_rojo.grid(column=1,row=3)

chk_azul= Checkbutton(frame,text="Azul",variable=color02,onvalue=1,offvalue=0,command=click)
chk_azul.grid(column=1,row=4)

chk_amarillo= Checkbutton(frame,text="Amarillo",variable=color03,onvalue=1,offvalue=0,command=click)
chk_amarillo.grid(column=1,row=5)

label_resultado = Label(frame,text='Resultado',font=("Arial",12))
label_resultado.grid(column=1,row=6)

ventana.mainloop()