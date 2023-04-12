videogame = "the master chIEf collection"
animal = "  capybara     "

# Pasa el String a mayusculas
print(videogame.upper())

# Pasa el String a minusculas
print(videogame.lower())

# Convierte la primera letra del String a mayusculas, dejando el resto en minusculas
print(videogame.capitalize())

# Convierte el String como si fuera un titulo
print(videogame.title())

# Elimina los espacios del String de la derecha y de la izquierda
print(animal.strip())

# Elimina los espacios a la izquierda
print(animal.lstrip())

# Elimina los espacios a la derecha
print(animal.rstrip())

# Encadenacion de metodos
print(animal.strip().capitalize())

# Encontrando un subString dentro del String, si no lo encuentra regresa -1
print(videogame.find("IE"))

# Remplaza caracteres dentro del String
print(videogame.replace("IE", "uwu"))

# Este metodo lo podemos tomar como una pregunta, La cadena se encuentra en el String dado?
print("IE" in videogame)


# Este metodo lo podemos tomar como una pregunta, La cadena no se encuentra en el String dado?
print("IE" not in videogame)
