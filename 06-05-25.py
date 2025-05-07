import tkinter as tk

def saludar():
    nombre = entrada_nombre.get()
    edad = entrada_edad.get(
    etiqueta_resultado.config(text=f"Hola {nombre}, tienes {edad}, años.")

ventana = tk.Tk()
ventana.title("Mi primera App grafica")
ventana.geometry("400x200")

etiqueta_nombre = tk.Label(ventana, text="Ingresa tu nombre:")
etiqueta.pack()
entrada_nombre = tk.Entry(ventana)
entrada_nombre.pack()

etiqueta_edad = tk.Label(ventana, text="Ingresa tu edad:")
etiqueta_edad.pack()
entrada_edad = tk.Entry(ventana)
entrada_edad.pack()

boton = tk.Button(ventana, text="Mostrar Saludo", command=saludar)
boton.pack()

etiqueta_resultado = tk.Label(ventana, text="")
etiqueta_resultado.pack()

ventana.mainloop()
