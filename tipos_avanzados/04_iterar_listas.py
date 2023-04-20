mascotas = ["Kokorita", "Neko", "Paki", "Copito"]


# Lo que estamos usando aqui es el desempaquetado, pero en este caso lo aplicamos hacia una tupla que genera "enumerate" para asi poder manipular el contenido de la lista con su indice
for indice, mascota in enumerate(mascotas):
    print(indice, mascota)
