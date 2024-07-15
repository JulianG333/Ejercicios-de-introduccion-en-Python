print("PROGRAMA PARA ÁREAS DE FIGURAS")
print("1. Cuadrado")
print("2. Rectángulo")
print("3. Triángulo")
print("4. Círculo")
print("5. Rombo")
print("6. Trapecio")
print("7. Salir")
opcion = int(input("Elige una opción: "))

if opcion == 1:
    lado = float(input("Ingresa el lado del cuadrado: "))
    area = lado ** 2
    print(f"El área del cuadrado es {area}")
elif opcion == 2:
    base = float(input("Ingresa la base del rectángulo: "))
    altura = float(input("Ingresa la altura del rectángulo: "))
    area = base * altura
    print(f"El área del rectángulo es {area} ")
elif opcion == 3:
    base = float(input("Ingresa la base del triángulo: "))
    altura = float(input("Ingresa la altura del triángulo: "))
    area = (base * altura) / 2
    print(f"El área del triángulo es {area}")
elif opcion == 4:
    radio = float(input("Ingresa el radio del círculo: "))
    area = 3.1416 * (radio ** 2)
    print(f"El área del círculo es {area}")
elif opcion == 5:
    D = float(input("Ingresa la diagonal mayor del rombo: "))
    d = float(input("Ingresa la diagonal menor del rombo: "))
    area = (D * d) / 2
    print(f"El área del rombo es {area}")
elif opcion == 6:
    B = float(input("Ingresa la base mayor del trapecio: "))
    b = float(input("Ingresa la base menor del trapecio: "))
    h = float(input("Ingresa la altura del trapecio: "))
    area = ((B + b) / 2) * h
    print(f"El área del trapecio es {area}")
elif opcion == 7:
    print("¡Hasta luego!")
else:
    print("Opción no válida. Por favor, elige una opción del 1 al 7.")
