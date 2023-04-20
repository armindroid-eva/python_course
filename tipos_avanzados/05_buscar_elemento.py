# Para buscar un elemento dentro de una lista, debemos asegurarnos primero que ese elemento si exista.
mascotas = ["Kokorita", "Neko", "Paki", "Copito", "Nieve"]

if "Nieve" in mascotas:
    # Lo que hace el metodo index es devolver el indice donde se encuentra dicho valor
    print(mascotas.index("Nieve"))

# Contar las concurrencias de dicho elemento
print(mascotas.count("Kokorita"))
