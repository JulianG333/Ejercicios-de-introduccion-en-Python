print("Programa para ordenar números")
num_1 = float(input("Ingresa el primer número: "))
num_2 = float(input("Ingresa el segundo número: "))
num_3 = float(input("Ingresa el tercer número: "))
# Determinar los números en orden ascendente
if num_1 <= num_2 <= num_3:
    ascendente1, ascendente2, ascendente3 = num_1, num_2, num_3
elif num_1 <= num_3 <= num_2:
    ascendente1, ascendente2, ascendente3 = num_1, num_3, num_2
elif num_2 <= num_1 <= num_3:
    ascendente1, ascendente2, ascendente3 = num_2, num_1, num_3
elif num_2 <= num_3 <= num_1:
    ascendente1, ascendente2, ascendente3 = num_2, num_3, num_1
elif num_3 <= num_1 <= num_2:
    ascendente1, ascendente2, ascendente3 = num_3, num_1, num_2
else:  # num3 <= num2 <= num1
    ascendente1, ascendente2, ascendente3 = num_3, num_2, num_1
# Determinar los números en orden descendente
descendente1, descendente2, descendente3 = ascendente3, ascendente2, ascendente1
print("Números en orden ascendente: ", ascendente1, ascendente2, ascendente3)
print("Números en orden descendente: ", descendente1, descendente2, descendente3)
