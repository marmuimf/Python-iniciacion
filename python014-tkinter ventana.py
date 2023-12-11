#crear un programa en ventana

from tkinter import * #carga todos los elementos

f = Frame(width=300,height=300)
f.pack(padx=30,pady=30) #padding horiz y vert

titulo = Label(f,text = "Hola Mickey")
titulo.pack(side=TOP) #alineado arriba
