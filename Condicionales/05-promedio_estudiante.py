print("Progrma para solicitar notas y calcular el promedio y su aprobación")
# Solicitar cinco notas al estudiante
nota1 = float(input("Ingresa la nota 1 (de 0.0 a 5.0): "))
nota2 = float(input("Ingresa la nota 2 (de 0.0 a 5.0): "))
nota3 = float(input("Ingresa la nota 3 (de 0.0 a 5.0): "))
# Calcular el promedio
promedio = (nota1 + nota2 + nota3) / 3
# Determinar si el estudiante aprobó o no
if promedio >= 3.0:
    print(f"Aprobó con un promedio de {promedio}.")
else:
    print(f"No aprobó. Su promedio fue {promedio}.")
