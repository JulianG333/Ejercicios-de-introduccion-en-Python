print("PROGRAMA QUE CALCULA EL ÁREA DE FIGURAS")
import math

def area_circulo():
    radio = float(input("Introduce el radio del círculo: "))
    return math.pi * radio ** 2

def area_cuadrado():
    lado = float(input("Introduce el lado del cuadrado: "))
    return lado ** 2

def area_rectangulo():
    largo = float(input("Introduce el largo del rectángulo: "))
    ancho = float(input("Introduce el ancho del rectángulo: "))
    return largo * ancho

def area_triangulo():
    base = float(input("Introduce la base del triángulo: "))
    altura = float(input("Introduce la altura del triángulo: "))
    return 0.5 * base * altura

print(f"Área del círculo: {area_circulo()}")
print(f"Área del cuadrado: {area_cuadrado()}")
print(f"Área del rectángulo: {area_rectangulo()}")
print(f"Área del triángulo: {area_triangulo()}")
