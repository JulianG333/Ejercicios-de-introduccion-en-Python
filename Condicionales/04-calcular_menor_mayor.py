print("Programa para calcular cuál número es mayor y menor")
# Solicitar dos números al usuario
numero_1 = int(input("Por favor, ingresa el primer número: "))
numero_2 = int(input("Por favor, ingresa el segundo número: "))
# Determinar cuál número es mayor y cuál es menor
if numero_1 > numero_2:
    print(f"El número mayor es {numero_1} y el número menor es {numero_2} .")
elif numero_1 < numero_2:
    print(f"El número mayor es {numero_2} y el número menor es {numero_1}.")
else:
    print("Ambos números son iguales.")
