#PRIMERA VERSION
import tkinter as tk

def saludar():
    nombre = entrada.get()
    etiqueta_resultado.config(text=f"Hola {nombre}")

ventana = tk.Tk()
ventana.title("Saludar")
ventana.geometry("300x150")

etiqueta = tk.Label(ventana, text="Ingresa tu nombre:")
etiqueta.pack()

entrada = tk.Entry(ventana)
entrada.pack()

boton = tk.Button(ventana, text="Saludar", command=saludar)
boton.pack()

etiqueta_resultado = tk.Label(ventana, text="")
etiqueta_resultado.pack()

ventana.mainloop()
---------------------------------------------------------------------------
#SEGUNDA VERSION
import tkinter as tk

def saludar():
    nombre = entrada_nombre.get()
    edad = entrada_edad.get()
    etiqueta_resultado.config(text=f"Hola {nombre}, tienes {edad} años.")

ventana = tk.Tk()
ventana.title("Mi primera app gráfica")
ventana.geometry("400x200")

etiqueta_nombre = tk.Label(ventana, text="Ingresa tu nombre:")
etiqueta_nombre.pack()
entrada_nombre = tk.Entry(ventana)
entrada_nombre.pack()

etiqueta_edad = tk.Label(ventana, text="Ingresa tu edad:")
etiqueta_edad.pack()
entrada_edad = tk.Entry(ventana)
entrada_edad.pack()

boton = tk.Button(ventana, text="Mostrar saludo", command=saludar)
boton.pack()

etiqueta_resultado = tk.Label(ventana, text="")
etiqueta_resultado.pack()

ventana.mainloop()
----------------------------------------------------------------------------
#TERCERA VERSION
import tkinter as tk

def saludar():
    nombre = entrada_nombre.get()
    edad = entrada_edad.get()
    etiqueta_resultado.config(text=f"Hola {nombre}, tienes {edad} años.")

ventana = tk.Tk()
ventana.title("Mi primer App gráfica")
ventana.geometry("400x200")
ventana.config(bg="#20B2AA")

etiqueta_nombre = tk.Label(ventana, text="Ingresa tu nombre:", bg="#20B2AA")
etiqueta_nombre.pack()
entrada_nombre = tk.Entry(ventana)
entrada_nombre.pack()

etiqueta_edad = tk.Label(ventana, text="Ingresa tu edad:", bg="#20B2AA")
etiqueta_edad.pack()
entrada_edad = tk.Entry(ventana)
entrada_edad.pack()

boton = tk.Button(ventana, text="Mostrar saludo", command=saludar)
boton.pack()

etiqueta_resultado = tk.Label(ventana, text="", bg="#20B2AA")
etiqueta_resultado.pack()

etiqueta_marca = tk.Label(ventana, text="Autor: Mónica González García", bg="#20B2AA")
etiqueta_marca.pack(side="bottom")

ventana.mainloop()
