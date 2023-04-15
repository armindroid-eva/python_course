# El orden para poder utilizar el if, elif importan, y va a depender de que es lo que queramos evaluar primero
edad = 65
if edad > 60:
    print("Puede ver la pelicula con un super descuento")
elif edad > 45:
    print("Puede ver la pelicula con descuento")
elif edad > 17:
    print("Puedes ver la pelicula")
else:
    print("No puedes ingresar, ve a otro lado")

print("Listo")
