from tkinter import *
from tkinter import ttk
ventana =Tk()
ventana.title('Ejercicio 3')
ventana.geometry('300x300')
ventana.configure(bg='beige')

lbl_voltaje=Label(ventana,text="Voltaje: ",font=("Arial",13),bg="beige",fg="black")
lbl_voltaje.grid(column=0,row=0,sticky="w")

voltaje=Entry(ventana,text="Voltaje: ",font=("Arial",13),fg="blue",width=10)
voltaje.grid(column=1,row=0)

lbl_corriente=Label(ventana,text="Corriente: ",font=("Arial",13),bg="beige",fg="black")
lbl_corriente.grid(column=0,row=1)

corriente=Entry(ventana,text="Corriente: ",font=("Arial",13),fg="blue",width=10)
corriente.grid(column=1,row=1)

lbl_potencia=Label(ventana,text="Potencia: ",font=("Arial",13),fg="blue",bg="beige")
lbl_potencia.grid(column=0,row=2,sticky="w")

potencia=Label(ventana,font=("Arial",13),fg="blue",bg="beige")
potencia.grid(column=1,row=2)

lbl_resistencia=Label(ventana,text="Resistencia: ",font=("Arial",13),fg="blue",bg="beige")
lbl_resistencia.grid(column=0,row=3,sticky="w")

resistencia=Label(ventana,font=("Arial",13),fg="blue",bg="beige")
resistencia.grid(column=1,row=3)




def calcular():
    potencia.configure(text=str(eval(voltaje.get())*eval(corriente.get()))+" Watts")
    resistencia.configure(text=str(eval(voltaje.get())/eval(corriente.get()))+" Ohms")
    
def limpiar():
    voltaje.delete(0,END)
    corriente.delete(0,END)
    potencia.configure(text="")
    resistencia.configure(text="")

btn_calcular=Button(ventana,text="Calcular",font=("Arial",13),command=calcular)
btn_calcular.grid(column=0,row=4)

btn_limpiar=Button(ventana,text="Limpiar",font=("Arial",13),command=limpiar)
btn_limpiar.grid(column=1,row=4)


ventana.mainloop()
