valor_unitario = float(input("Ingresa el valor unitario del producto: "))
cantidad_productos = int(input("Ingresa la cantidad de productos comprados: "))
# Calcular el valor total sin IVA
valor_total_sin_iva = valor_unitario * cantidad_productos
# Calcular el IVA
iva = valor_total_sin_iva * 0.16
# Calcular el valor final con IVA
valor_final = valor_total_sin_iva + iva
print(f"El valor final a pagar es: {valor_final}")
