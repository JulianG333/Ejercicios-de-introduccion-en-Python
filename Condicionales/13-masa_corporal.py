print("Cálculo de IMC")
peso = float(input("Ingresa tu peso en Kg: "))
estatura = float(input("Ingresa tu estatura en metros: "))
IMC = peso / (estatura ** 2)
if IMC < 18.5:
    estado = "Desnutrido"
elif 18.5 <= IMC < 25:
    estado = "Normal"
elif 25 <= IMC < 30:
    estado = "Sobrepeso"
elif 30 <= IMC < 35:
    estado = "Obesidad Grado 1"
elif 35 <= IMC < 40:
    estado = "Obesidad Grado 2"
elif 40 <= IMC < 50:
    estado = "Obesidad Grado 3"
else: 
    estado = "Obesidad Grado 4"
print(f"Tu IMC es {IMC}")
print(f"Tu estado es {estado}")
