class Rectangle:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho

    def area(self):
        return self.largo * self.ancho

largo = int(input("Escriba el largo que tiene el rectángulo: "))
ancho = int(input("Escriba el ancho que tiene el rectángulo: "))

rectangulo = Rectangle(largo, ancho)
print(f"Área del rectángulo: {rectangulo.area()}")
