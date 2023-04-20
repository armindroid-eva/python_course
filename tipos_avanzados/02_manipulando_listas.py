mascotas = ["Kokorita", "Paki", "Neko", "Nieve"]
print(mascotas[1])

# Cambiando valores dentro de la lista por su indice
mascotas[1] = "Copito"
print(mascotas)

# Manipulando la lista de mascotas
print(mascotas[1:3])
print(mascotas[2:])
print(mascotas[-1])

# Inviertiendo la lista
print(mascotas[::-1])

print(mascotas[0:3:2])

# Imprimiendo los numeros pares de una lista
numeros = list(range(21))
print(numeros[::2])

# Imprimiendo los numeros impares de la lista
print(numeros[1::2])
