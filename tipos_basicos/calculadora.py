n1 = int(input("Ingrese el primer numero: "))
n2 = int(input("Ingrese el segundo numero: "))

suma = n1 + n2
resta = n1 - n2
multi = n1 * n2
div = n1 / n2

mensaje = f"""
Para los numeros {n1} y {n2},
La suma es {suma}
La resta es {resta}
La multiplicacion es {multi}
La division es {div}
"""

print(mensaje)
