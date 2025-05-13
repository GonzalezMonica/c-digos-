num1 = float(input("Escribe el primer número: "))
num2 = float(input("Escribe el segundo número: "))
resultado = (num1*num2)/2
if resultado>100:
    print("Área:"{resultado},el area es grande)
else:
    print("Área:"{resultado},el area es chica)

import tkinter as tk

def resultado_op():
    try:
        base = float(entrada_b.get())
        altura = float(entrada_h.get())
        resultado = (base * altura) / 2
        if resultado > 100:
            mensaje = f"Resultado: {resultado:.2f}, el área es grande"
        else:
            mensaje = f"Área: {resultado:.2f}, el área es pequeña"
        etiqueta_resultado.config(text=mensaje)
    except ValueError:
        etiqueta_resultado.config(text="Por favor, ingresa números válidos.")

def repetir():
    entrada_b.delete(0, tk.END)
    entrada_h.delete(0, tk.END)
    etiqueta_resultado.config(text="")

def cerrar():
    ventana.destroy()

ventana = tk.Tk()
ventana.title("Área del Triángulo")
ventana.geometry("400x250")
ventana.config(bg="#FAFAD2")

etiqueta_b = tk.Label(ventana, text="Ingresa la base:", bg="#FAFAD2")
etiqueta_b.pack()
entrada_b = tk.Entry(ventana)
entrada_b.pack()

etiqueta_h = tk.Label(ventana, text="Ingresa la altura:", bg="#FAFAD2")
etiqueta_h.pack()
entrada_h = tk.Entry(ventana)
entrada_h.pack()

tk.Button(ventana, text="Calcular área", command=resultado_op).pack()

etiqueta_resultado = tk.Label(ventana, text="", bg="#FAFAD2")
etiqueta_resultado.pack()

etiqueta_r = tk.Label(ventana, text="¿Desea repetir?", bg="#FAFAD2")
etiqueta_r.pack()

frame_botones = tk.Frame(ventana, bg="#FAFAD2")
frame_botones.pack()

tk.Button(frame_botones, text="Sí", command=repetir).pack(side="left", padx=10)
tk.Button(frame_botones, text="No", command=cerrar).pack(side="left", padx=10)

ventana.mainloop()
