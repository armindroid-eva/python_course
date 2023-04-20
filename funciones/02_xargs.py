# Los xargs nos sirven para poder manejar de una manera iterable los parametros de una funcion
def suma(*numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total


print(suma(2, 3, 5, 7, 9, 3))
