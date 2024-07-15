print("PROGRAMA QUE CALCULA EL FACTORIAL")
def factorial():
    numero = int(input("Introduce un número entero no negativo: "))
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    return resultado
print(f"El factorial del número es: {factorial()}")
