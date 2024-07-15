print("PROGRAMA QUE SACA EL MÁXIMO DE 3 NÚEMROS")
def maximo_de_tres_numeros():
    a = float(input("Introduce el primer número: "))
    b = float(input("Introduce el segundo número: "))
    c = float(input("Introduce el tercer número: "))
    return max(a, b, c)
print(f"El número mayor es el {maximo_de_tres_numeros()}")  
