numeros = [1, 2, 3, 4, 5, 6]

# A esto se le llama desempaquetado o destructuring de una lista
primero, segundo, tercero, *otros = numeros
print(primero, segundo, tercero, otros)

# Obteniendo el primer y ultimo valor
first, *others, last = numeros
print(first, others, last)
