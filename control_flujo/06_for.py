buscar = 10
# Iterable
# Principalmente la estructura for se utiliza para iterar o para buscar un elemento dentro de una estructura, como una lista, tupla o String
for numero in range(5):
    print(numero)
    if buscar == numero:
        print("Encontre el numero:", buscar)
        break
else:
    print("No encontre el numero solicitado :(")

for letra in "Ultimate Python":
    print(letra)
