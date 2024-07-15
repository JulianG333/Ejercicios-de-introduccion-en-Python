print("PROGRAMA QUE IDENTIFICA UN NÚEMERO PRIMO")
def es_primo():
    numero = int(input("Introduce un número: "))
    if numero > 1:
        for i in range(2, numero):
            if (numero % i) == 0:
                return False
        else:
            return True
    else:
        return False

if es_primo():
    print("El número es primo.")
else:
    print("El número no es primo.")
