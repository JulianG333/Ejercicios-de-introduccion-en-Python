print("Progama para determinar el tipo de número ingresado")
numero = int(input("Agregue un número: "))
#Determinar si es par, impar o cero
if numero == 0:
    print("El número es cero.")
elif numero % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")