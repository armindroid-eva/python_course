mascotas = [
    "Kokorita",
    "Neko",
    "Paki",
    "Copito",
    "Nieve",
    "Pelusa"]

mascotas.insert(1, "Mimi")
# Agregando un elemento al final de la lista
mascotas.append("Piojo")
# Eliminando un elemento por su valor
mascotas.remove("Copito")
# Eliminar el ultimo elemento de la lista
mascotas.pop()
# Eliminando un elemento por su indice
mascotas.pop(0)
# Eliminacion de un elemento usando del
del mascotas[2]

# Limpiar la lista
mascotas.clear()
print(mascotas)
