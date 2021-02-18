# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 10:07:13 2021

@author: Derly garzon
"""
from tkinter import *    # Carga módulo tk (widgets estándar)
from tkinter import ttk  # Carga ttk (para widgets nuevos 8.5+)

   
   
# Define la ventana principal de la aplicación
raiz = Tk()
raiz.geometry("300x200")

# título de la ventana
raiz.title("Formulario")

#marco que permite agrupar diferentes widgets.
miFrame= Frame()
#muestra el elemento
miFrame.pack()

#muestra el elemento
bienvenido = Label(miFrame, text="BIENVENIDO")
bienvenido.grid(row=0, column=0)
bienvenido.config(font=('Arial', 16))


#label 
nombre_label= Label(miFrame, text="Cual es tu nombre:")
nombre_label.grid(row=1, column=0)
nombre_label.config(padx=10, pady=10)


#input text
cuadro_nombre=Entry(miFrame)
cuadro_nombre.grid(row=1, column=1)

#boton
def clicked():
    res = "Welcome to " + cuadro_nombre.get()
    bienvenido.configure(text= res)
    
    
btn = Button(miFrame, text="Click Me", command=clicked)
btn.grid(column=0, row=2)   

raiz.mainloop()
