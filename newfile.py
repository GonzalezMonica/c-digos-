num1 = float(input("Escribe el primer número: "))
num2 = float(input("Escribe el segundo número: "))
operacion = input("Selecciona la operación (+, -, *, /): ")

if operacion == '+':
    resultado = num1 + num2
    print(resultado)
elif operacion == '-':
    resultado = num1 - num2
    print(resultado)
elif operacion == '*':
    resultado = num1 * num2
    print(resultado)
elif operacion == '/':
    if num2 != 0:
        resultado = num1 / num2
        print(resultado)
    else:
        print("Error: no se puede dividir entre 0")
else:
    print("Operación no válida")
