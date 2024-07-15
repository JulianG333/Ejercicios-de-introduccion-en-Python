print("VERIFICACIÓN DE UN PALINDROMO")
frase = input("Ingresa una frase para su validación: ")
frase = frase.lower().replace(" ", "")
invertida = frase[::-1]

if frase == invertida:
    print("La frase es un palíndromo.")
elif frase != invertida:
    print("La frase no es un palíndromo.")
else:
    print("No se pudo verificar la frase.")
