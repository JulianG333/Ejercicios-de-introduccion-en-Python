print("CUENTA DE COBRO")
cuenta = float(input("Ingresa el monto de la cuenta: "))
# Determinar el tipo de pago a usar
if cuenta < 150000:
    print("Pago en efectivo.")
elif 150000 <= cuenta < 300000:
    print("Pago con el celular (dinero electrónico).")
elif 300000 <= cuenta < 600000:
    print("Pago con la tarjeta de débito.")
else:  # cuenta >= 600000
    print("Pago con la tarjeta de crédito.")
