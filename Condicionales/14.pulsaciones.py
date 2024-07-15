edad = int(input("Ingresa tu edad en años: "))
genero = int(input("Ingresa tu género (1 para femenino, 2 para masculino): "))
if genero == 1:  # Género femenino
    pulsaciones = (220 - edad) / 10
elif genero == 2:  # Género masculino
    pulsaciones = (210 - edad) / 10
else:
    print("Género no válido. Por favor, ingresa 1 para femenino o 2 para masculino.")
    exit()
print(f"El número de pulsaciones que debes tener por cada 10 segundos de ejercicio aeróbico es {pulsaciones}")
