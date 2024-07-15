print("PROGRAM QUE CALCULA EL TOTAL DE LETRAS MAYÚSCULAS Y MINÚSCULAS")
def contar_mayusculas_minusculas():
    cadena = input("Introduce una cadena de texto: ")
    mayusculas = 0
    minusculas = 0
    for caracter in cadena:
        if caracter.isupper():
            mayusculas += 1
        elif caracter.islower():
            minusculas += 1
    return mayusculas, minusculas
mayusculas, minusculas = contar_mayusculas_minusculas()
print(f"La cadena tiene {mayusculas} letras mayúsculas y {minusculas} letras minúsculas.")
