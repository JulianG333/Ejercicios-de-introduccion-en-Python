print("BIENVENIDO A LA PIZZERIA")
tamaño = int(input("Ingresa el tamaño de la pizza (1, 2 o 3): "))
ingredientes_adicionales = int(input("Ingresa el número de ingredientes adicionales: "))
if tamaño == 1:
    precio_base = 15000
elif tamaño == 2:
    precio_base = 24000
elif tamaño == 3:
    precio_base = 36000
else:
    print("Tamaño no válido. Por favor, ingresa un tamaño del 1 al 3.")
    exit()
costo_ingredientes = ingredientes_adicionales * 4000
precio_total = precio_base + costo_ingredientes
print(f"El precio total a pagar es ${precio_total}")
