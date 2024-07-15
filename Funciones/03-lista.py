print("PROGRAMA PARA SUMAR UNA LISTA DE NÚMEROS")
def suma_lista():
    lista_numeros = input("Introduce una lista de números separados por comas: ")
    lista_numeros = list(map(int, lista_numeros.split(',')))
    suma = sum(lista_numeros)
    return suma
print(f"La suma de los números en la lista es: {suma_lista()}")
