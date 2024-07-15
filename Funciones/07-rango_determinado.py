print("PROGRAMA QUE COMPRUEBA EL SI UN NÚMERO ESTÁ EN UN RANGO")
def esta_en_rango():
    numero = float(input("Introduce un número: "))
    limite_inferior = float(input("Introduce el límite inferior del rango: "))
    limite_superior = float(input("Introduce el límite superior del rango: "))
    if limite_inferior <= numero <= limite_superior:
        return True
    else:
        return False

if esta_en_rango():
    print("El número está dentro del rango.")
else:
    print("El número está fuera del rango.")
