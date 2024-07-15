print("PROGRAMA QUE INVIERTE UNA CADENA DE TEXTO")
def invertir_cadena():
    cadena = input("Introduce una cadena de texto: ")
    cadena_invertida = cadena[::-1]
    return cadena_invertida
print(f"La cadena invertida es: {invertir_cadena()}")
