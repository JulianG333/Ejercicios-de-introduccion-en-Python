class Circle:
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return 3.14159 * self.radio ** 2

    def perimetro(self):
        return 2 * 3.14159 * self.radio

radio = int(input("Ingrese el radio del círculo: "))

circulo = Circle(radio)
print(f"Área del círculo: {circulo.area()}")
print(f"Perímetro del círculo: {circulo.perimetro()}")