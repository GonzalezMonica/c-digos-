import tkinter as tk

def saludar():
    nombre = entrada_nombre.get()
    edad = entrada_edad.get(
    etiqueta_resultado.config(text=f"Hola {nombre}, tienes {edad}, años.")

ventana = tk.Tk()
ventana.title("Mi primera App grafica")
ventana.geometry("400x200")
ventana.config(bg="#20B2AA")

etiqueta_nombre = tk.Label(ventana, text="Ingresa tu nombre:", bg="#20B2AA")
etiqueta.pack()
entrada_nombre = tk.Entry(ventana)
entrada_nombre.pack()

etiqueta_edad = tk.Label(ventana, text="Ingresa tu edad:", bg="#20B2AA")
etiqueta_edad.pack()
entrada_edad = tk.Entry(ventana)
entrada_edad.pack()

boton = tk.Button(ventana, text="Mostrar Saludo", command=saludar)
boton.pack()

etiqueta_resultado = tk.Label(ventana, text="", bg="#20B2AA")
etiqueta_resultado.pack()

etiqueta_marcagua = tk.Label(ventana, text="Autor: Mónica González García del 2BMPG", bg="#20B2AA")
etiqueta_marcagua.pack(side="bottom")

ventana.mainloop()
