from tkinter import *

def click():
    txt_resultado = "Pulsado: "
    if opcion.get()==1:
        txt_resultado +='Rojo'
        ventana.configure(bg="red")
    elif opcion.get()==2:
        txt_resultado +='Azul'
        ventana.configure(bg="blue")
    elif opcion.get()==3:
        txt_resultado += 'Amarillo'
        ventana.configure(bg="yellow")
        
    label_resultado.configure(text=txt_resultado)
    
ventana  = Tk()
ventana.title("App con RadioButton")
ventana.geometry("640x400")
frame = Frame()
frame.pack()
opcion= IntVar()
rd_rojo= Radiobutton(frame,text="Rojo",value=1,variable=opcion,command=click)
rd_rojo.grid(column=1,row=3)

rd_azul= Radiobutton(frame,text="Azul",value=2,variable=opcion,command=click)
rd_azul.grid(column=1,row=4)

rd_amarillo= Radiobutton(frame,text="Amarillo",value=3,variable=opcion,command=click)
rd_amarillo.grid(column=1,row=5)

label_resultado = Label(frame,text='Resultado',font=("Arial",12))
label_resultado.grid(column=1,row=6)

ventana.mainloop()