def saludo(nombre, apellido):  # Los valores dentro del contexto de la funcion se llaman parametros
    print(f"Bienvenido {nombre} {apellido}")


# Los valores que le damos cuando llamamos a la funcion, se llaman argumentos
saludo("Luis Alberto", "Sanchez Juarez")


# Cuando no le pasamos un argumento a la llamada de la funcion, este tendra un valor por defecto que nosotros especificaremos en los parametros de la funcion, en este caso el string "No se escribio el apellido"
def saludo2(nombre, apellido="No se escribio el apellido"):
    print(f"Bienvenido {nombre} {apellido}")


saludo2("Luis Alberto")

# Argumentos nombrados
saludo(apellido="Suarez", nombre="Rodrigo")
