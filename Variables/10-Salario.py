salario_diario = float(input("Por favor, ingresa el salario diario: "))
dias_trabajados = int(input("Por favor, ingresa el número de días trabajados: "))
# Calcular el salario bruto
salario_bruto = salario_diario * dias_trabajados
# Calcular los descuentos por pensión y salud
descuento_pension = salario_bruto * 0.10
descuento_salud = salario_bruto * 0.15
# Calcular el salario neto después de los descuentos
salario_neto = salario_bruto - descuento_pension - descuento_salud
print(f"El salario a pagar después de los descuentos es: {salario_neto}")