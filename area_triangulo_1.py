num1 = float(input("Escribe el primer número: "))
num2 = float(input("Escribe el segundo número: "))
resultado = (num1*num2)/2
print(resultado)

import tkinter as tk

def resultado_op():
    base = float (entrada_b.get())
    altura = float (entrada_h.get())
    resultado = (base*altura)/2
    if resultado>100:
        etiqueta_resultado = tk.Label(text=f"Resultado: {resultado}, el area es grande", bg="#FAFAD2")
        etiqueta_resultado.pack()
    else:
        etiqueta_resultado = tk.Label(text=f"Area: {resultado}", bg="#FAFAD2")
        etiqueta_resultado.pack()

def salir():
    ventana.destroy()
    

ventana = tk.Tk()
ventana.title("Area del Triangulo")
ventana.geometry("400x200")
ventana.config(bg="#FAFAD2")

etiqueta_b = tk.Label(ventana, text="Ingresa la base:", bg="#FAFAD2")
etiqueta_b.pack()
entrada_b = tk.Entry(ventana)
entrada_b.pack()

etiqueta_h =  tk.Label(ventana, text="Ingresa la altura:", bg="#FAFAD2")
etiqueta_h.pack()
entrada_h = tk.Entry(ventana)
entrada_h.pack()

boton = tk.Button(ventana, text="Sacar area", command=resultado_op)
boton.pack()

boton = tk.Button(ventana, text="Salir", command=salir)
boton.pack()
     
ventana.mainloop()

