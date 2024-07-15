print("Bienvenidos a la tienda, ¡SUPER PROMOCIONES!")
cantidad = int(input("Ingresa la cantidad de artículos: "))
precio_unitario = float(input("Ingresa el precio unitario original: "))
if cantidad <= 5:
    descuento = 0
elif cantidad < 10:
    descuento = 0.05
else:
    descuento = 0.08
precio_unitario_descuento = precio_unitario * (1 - descuento)
valor_total = cantidad * precio_unitario_descuento
print(f"El valor total a pagar es ${valor_total}")