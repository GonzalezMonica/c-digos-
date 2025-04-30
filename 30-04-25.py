def preparar_datos(info):
  acumulador=" "
  for letra in info:
    acumulador +=letra + "-"
  return acumulador[:-1]

# el primer error por el cual no funciono fue porque no habia espacios entre las funciones (las funcines tienen su nombre y parametros)

def mezcla_datos(a,b):
  if a>b: # si a tienes mas letras que b se pone primero la palabra a y luego la b
    return a+b
  elif a==b:# si son iguales se duplica la a
    return a*2
  else: #si no es ninguna de las ateriores y b tiene mas letras que a se pone primero b
    return b+a

def iniciar(): # en esta funcion se le llama a la funcion 1 y 2 para que corra
    entrada1=input("Ingresa un valor de referencia textual: ")
    entrada2=input("Ingresa otra unidad: ")
    a=preparar_datos(entrada1)
    b=preparar_datos(entrada2)
    resultado=mezcla_datos(a,b)
    print("resultado no final: ", resultado)
    if entrada1 in entrada2:
      print ("Coincidencia detectada")
iniciar()
# finalmente cambie x,y por a,b para que el codigo se comprenda mejor
