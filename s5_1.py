from tkinter import *

ventana =Tk()
ventana.title('Fundamentos 15-04')
ventana.geometry('300x300')
ventana.configure(bg='beige')

lbl=Label(ventana,text="Nombre",font=("Arial",13),bg="beige",fg="black")
lbl.grid(column=0,row=0)

def cambio():
        lbl.configure(text='Daniel',fg='red')

btn=Button(ventana,text="Click",font=("Arial",13),bg="gray",fg="black",command=cambio)
btn.grid(column=0,row=1)


ventana.mainloop()

