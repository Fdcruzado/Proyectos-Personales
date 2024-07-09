from tkinter import *
from tkinter import ttk
ventana =Tk()
ventana.title('Ejercicio 3')
ventana.geometry('600x600')
ventana.configure(bg='beige')

lbl=Label(ventana,text="Jugador 1",font=("Arial",13),bg="beige",fg="black")
lbl.grid(column=0,row=0)
lbl=Label(ventana,text="Jugador 2",font=("Arial",13),bg="beige",fg="black")
lbl.grid(column=1,row=0)

funcion1=ttk.Combobox(ventana,font=(("Arial",13)))
funcion1["values"]=["PIEDRA","PAPEL","TIJERA","LAGARTO","SPOCK"]
funcion1.current(0)
funcion1.grid(column=0,row=2)

funcion2=ttk.Combobox(ventana,font=(("Arial",13)))
funcion2["values"]=["PIEDRA","PAPEL","TIJERA","LAGARTO","SPOCK"]
funcion2.current(0)
funcion2.grid(column=1,row=2)

resultado=Label(ventana,font=("Arial",13),fg="blue",bg="beige")
resultado.grid(column=0,row=6)

T1=None
T2=None

def tapar1():
    global T1
    T1=Label(ventana,text="Jugador 1 esperando",bg="blue",fg="white")
    T1.grid(column=0,row=1,padx=2,pady=6,rowspan=2,sticky="nsew")



def tapar2():
    global T2
    T2=Label(ventana,text="Jugador 2 esperando",bg="blue",fg="white")
    T2.grid(column=1,row=1,padx=2,pady=6,rowspan=2,sticky="nsew")

def limpiar():
    global T1, T2
    funcion1.current(0)
    
    funcion2.current(0)
    if T1:
        T1.grid_remove()
        T1 = None
    if T2:
        T2.grid_remove()
        T2 = None
    resultado.configure(text="")


def calcular():
    if funcion1.get()=="PIEDRA" and (funcion2.get()=="LAGARTO"  or funcion2.get()=="TIJERA"):
        resultado.configure(text="Gano Jugador 1")
    elif funcion1.get()=="PIEDRA" and (funcion2.get()=="SPOCK"  or funcion2.get()=="PAPEL"):
        resultado.configure(text="Gano Jugador 2")
    elif funcion1.get()=="PAPEL" and (funcion2.get()=="SPOCK"  or funcion2.get()=="PIEDRA"):
        resultado.configure(text="Gano Jugador 1")
    elif funcion1.get()=="PAPEL" and (funcion2.get()=="TIJERA"  or funcion2.get()=="LAGARTO"):
        resultado.configure(text="Gano Jugador 2")
    elif funcion1.get()=="TIJERA" and (funcion2.get()=="PAPEL"  or funcion2.get()=="LAGARTO"):
        resultado.configure(text="Gano Jugador 1")
    elif funcion1.get()=="TIJERA" and (funcion2.get()=="PIEDRA"  or funcion2.get()=="SPOCK"):
        resultado.configure(text="Gano Jugador 2")
    elif funcion1.get()=="SPOCK" and (funcion2.get()=="TIJERA"  or funcion2.get()=="PIEDRA"):
        resultado.configure(text="Gano Jugador 1")
    elif funcion1.get()=="SPOCK" and (funcion2.get()=="PAPEL"  or funcion2.get()=="LAGARTO"):
        resultado.configure(text="Gano Jugador 2")
    elif funcion1.get()=="LAGARTO" and (funcion2.get()=="PAPEL"  or funcion2.get()=="SPOCK"):
        resultado.configure(text="Gano Jugador 1")
    elif funcion1.get()=="LAGARTO" and (funcion2.get()=="TIJERA"  or funcion2.get()=="PIEDRA"):
        resultado.configure(text="Gano Jugador 2")
    elif funcion1.get()==funcion2.get():
        resultado.configure(text="EMPATE")




btn_jg1=Button(ventana,text="Listo",font=("Arial",13),command=tapar1)
btn_jg1.grid(column=0,row=3)


btn_jg2=Button(ventana,text="Listo",font=("Arial",13),command=tapar2)
btn_jg2.grid(column=1,row=3)



btn_limpiar=Button(ventana,text="Limpiar",font=("Arial",13),command=limpiar)
btn_limpiar.grid(column=1,row=4)

btn_calcular=Button(ventana,text="Jugar",font=("Arial",13),command=calcular)
btn_calcular.grid(column=0,row=4)

ventana.mainloop()
