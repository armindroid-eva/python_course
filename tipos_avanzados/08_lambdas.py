usuarios = [
    ["Luis Alberto", 2],
    ["Rodrigo", 7],
    [" Pepe", 1]
]

usuarios.sort(key=lambda el: el[1], reverse=True)
print(usuarios)
