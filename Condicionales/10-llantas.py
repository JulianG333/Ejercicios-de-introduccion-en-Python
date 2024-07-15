print("COMPRA DE LLANTAS")
num_llantas = int(input("Ingresa el número de llantas que deseas comprar: "))
# Determinar el precio unitario y calcular el valor total
if num_llantas < 6:
    precio_unitario = 240000
elif num_llantas >= 6 and  num_llantas <= 7 :
    precio_unitario = 221000
else:
    precio_unitario = 180000
valor_total = num_llantas * precio_unitario
print(f"El valor total a pagar es ${valor_total}")
