nombre = "Luis Alberto Sanchez Juarez"
texto_largo = """Esto es un string largo donde podemos poner cualquier parrafo"""
print(texto_largo)

# Funcion para obtener la longitud de un String
print(len(nombre))

# Accesar a los indices de un String
print(nombre[0])
print(nombre[1])

# Devolviendo una parte de un String, [inicio : final]
print(nombre[0:4])

# Devolviendo una parte del String sin pasarle el indice 'final' [inicio : ]
# Esto tomara un valor por defecto en la parte de 'final', el cual es la longitud restante del String
print(nombre[5:])


# Devolviendo una parte de un String, [: final]
# Esto tomara el valor por defecto del indice 'inicio', el cual es 0
print(nombre[:6])


# Devolviendo el mismo String, donde se toman los valores por defecto de [inicio : final]
print(nombre[:])
