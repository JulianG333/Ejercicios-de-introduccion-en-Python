class Ave:
    def __init__(self, nombre, color):
        self.nombre = nombre
        self.color = color

    def volar(self):
        print(f"{self.nombre} está volando.")



class Aguila(Ave):
    def __init__(self, nombre, color, envergadura):
        super().__init__(nombre, color)
        self.envergadura = envergadura

    def cazar(self):
        print(f"{self.nombre} está cazando.")

class Canario(Ave):
    def cantar(self):
        print(f"{self.nombre} está cantando.")

nombre_aguila = input("Ingrese el nombre del águila: ")
color_aguila = input("Ingrese el color del águila: ")
envergadura_aguila = input("Ingrese la envergadura del águila en metros: ")

nombre_canario = input("Ingrese el nombre del canario: ")
color_canario = input("Ingrese el color del canario: ")

aguila = Aguila(nombre_aguila, color_aguila, envergadura_aguila)
canario = Canario(nombre_canario, color_canario)
aguila.cazar()
canario.cantar()
aguila.volar()
canario.volar()
print(f"El águila {aguila.nombre} de color {aguila.color} tiene una envergadura de {aguila.envergadura} metros.")
print(f"El canario {canario.nombre} de color {canario.color} es un ave pequeña y canta muy bien.")
