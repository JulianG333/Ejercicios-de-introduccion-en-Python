print("PROGRAM QUE IDENTIFICA UN PALÍDROMO")
def es_palindromo():
    cadena = input("Introduce una cadena de texto: ")
    cadena = cadena.replace(" ", "").lower()
    if cadena == cadena[::-1]:
        return True
    else:
        return False
if es_palindromo():
    print("La cadena es un palíndromo.")
else:
    print("La cadena no es un palíndromo.")
