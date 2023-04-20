def es_Palindromo(texto):
    texto_sin_espacios = no_space(texto).lower()
    texto_reverse = reverse(texto_sin_espacios)
    return texto_sin_espacios == texto_reverse


def reverse(texto):
    texto_reversa = ""
    for char in texto[::-1]:
        texto_reversa += char
    return texto_reversa


def no_space(texto):
    nueva_cadena = ""
    for char in texto:
        if char != " ":
            nueva_cadena += char
    return nueva_cadena


print("Abba", es_Palindromo("Abba"))
print("Amo la paloma", es_Palindromo("Amo la paloma"))
print("Hola", es_Palindromo("Hola"))
