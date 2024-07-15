print("PROGRAMA QUE IMPRIME LOS NÚMEROS PARES")
def numeros_pares():
    lista_numeros = input("Introduce una lista de números separados por comas: ")
    lista_numeros = list(map(int, lista_numeros.split(',')))
    pares = [num for num in lista_numeros if num % 2 == 0]
    return pares
print(f"Los números pares en la lista son: {numeros_pares()}")
