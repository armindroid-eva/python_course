numeros = [1, 2, 3]
letras = ['a', 'b', 'c']
palabras = ['Luis Alberto', 'Octavio', 'Rodrigo', 'Pepe']
matriz = [[0, 1, 2, 3],
          [0, 1, 2, 3],
          [0, 1, 2, 3]]
print(matriz)
booleans = [True, False, True, False]
# Operaciones con listas
# Creando una lista de 10 ceros
ceros = [0] * 10
print('Lista creada a partir de la multiplicacion:', ceros)

# Uniendo 2 listas
alfanumerico = numeros + letras
print('Lista unida:', alfanumerico)

# Creacion de lista a partir del metodo list()
rango = list(range(1, 11))
print('Lista creada a partir de list(), usando range:', rango)

# Creacion de una lista a partir de un String iterable
chars = list("Hola mundo")
print(chars)
