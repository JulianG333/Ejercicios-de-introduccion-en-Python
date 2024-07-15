print("PROGRAMA QUE DEVULEVE UNA LISTA CON ELEMNETOS DE OTRA LISTA")
def elementos_unicos():
    lista_elementos = input("Introduce una lista de elementos separados por comas: ")
    lista_elementos = lista_elementos.split(',')
    lista_unicos = list(set(lista_elementos))
    return lista_unicos
print(f"La lista con elementos únicos es: {elementos_unicos()}")
