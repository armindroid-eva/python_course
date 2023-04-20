# Ordenando numeros con sort
numeros = [23, 443, 345, 234, 231, 35, 63, 435]

# Este metodo afecta la lista original
# Pasandole el parametro de reverse, ordena la lista de manera descendente
numeros.sort(reverse=True)

# Ordenando con sorted
# Esta funcion crea una nueva lista ordenada,
numeros2 = sorted(numeros, reverse=True)

print(numeros2)
print(numeros)

usuarios = [
    ["Luis Alberto", 2],
    ["Rodrigo", 7],
    [" Pepe", 1]
]
# # El metodo sort va a ordenar la lista de listas, tomando en cuenta siempre el primer elemento
# usuarios.sort()
# print(usuarios)

# Que pasaria si el el primer elemento que toma no es ordenable?
# Necesitariamos crear una funcion que retorne el valor ordenable


def ordenada(elemento):
    return elemento[1]


usuarios.sort(key=ordenada, reverse=True)
print(usuarios)
