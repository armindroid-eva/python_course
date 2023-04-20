# Cuando estemos trabajando con kwargs, siempre debemos especificarle el nombre del argumento cuando llamamos a la funcion
def get_product(**datos):
    print(datos["id"], datos["name"])


get_product(id="12", name="iPhone", desc='Esto es un iPhone')
# id = parametro y "12" = argumento
