print("Bienvenidos a la calculadora creada por amindroid.exe ")
print("Para salir escribe salir")
print("Las operaciones son suma, multi, division y resta")
n1 = ''
while True:
    if not n1:
        n1 = input("Ingrese un numero: ")
        if n1.lower() == "salir":
            break
        n1 = int(n1)
    operacion = input("Ingrese la operacion: ")
    if operacion.lower() == "salir":
        break
    n2 = input("Ingrese el segundo numero: ")
    if n2.lower() == "salir":
        break
    n2 = int(n2)
    if operacion.lower() == "suma":
        n1 += n2
    elif operacion.lower() == "resta":
        n1 -= n2
    elif operacion.lower() == "multiplicacion":
        n1 *= n2
    elif operacion.lower() == "division":
        n1 /= n2
    else:
        print("Ninguna de las operaciones es valida ")
        break
    print(f'El resultado es {n1}')
