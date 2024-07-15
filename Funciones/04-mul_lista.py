print("PROGRAMA QUE MULTIPLICA UNA LISTA DE NÚMEROS")
def multiplicar_numeros():
    lista_numeros = input("Introduce una lista de números separados por comas: ")
    lista_numeros = lista_numeros.split(',')
    lista_numeros = [int(num) for num in lista_numeros]
    resultado = 1
    for num in lista_numeros:
        resultado *= num
    return resultado
print(f"El producto de los números en la lista es: {multiplicar_numeros()}")
