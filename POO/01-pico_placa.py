import datetime
class Parqueadero:
    def __init__(self, dueño, placa, color, marca):
        print (f"Bienvenido al parqueadero, señor {dueño}")

        self.dueño = dueño
        self.placa = placa
        self.color = color
        self.marca = marca

       

    def pico_y_placa(self, fecha):
        ultimo_digito = int(self.placa[-1]) 
        dia_semana = fecha.day  

        if dia_semana % 2 == 0:  
            return ultimo_digito in [1, 2, 3, 4, 5]
        else:  
            return ultimo_digito in [6, 7, 8, 9, 0]


dueño = input("Ingresa el nombre del dueño del vehículo: ")
placa = input("Ingresa el número de placa del vehículo: ")
color = input("Ingresa el color del vehículo: ")
marca = input("Ingresa la marca del vehículo: ")


mi_vehiculo = Parqueadero(dueño, placa, color, marca)
fecha_actual = datetime.date.today()

if mi_vehiculo.pico_y_placa(fecha_actual):
    print(f"El vehículo con placa {placa}, con color {color}, y con marca {marca} tiene restricción por pico y placa hoy en Bogotá.")
else:
    print(f"El vehículo con placa {placa}, con color {color}, y con marca {marca} no tiene restricción por pico y placa hoy en Bogotá.")
