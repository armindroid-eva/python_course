# El alcance de las variables de "saludo" solo va a existir dentro de la funcion, en ninguna otra parte del codigo se van a poder ocupar esa variables, mas que dentro de la funcion
def saludar():
    saludo = "Hola mundo"
    print(saludo)


def saludaChanchito():
    saludo = "Hola Chanchito"
    print(saludo)


saludar()
saludaChanchito()
