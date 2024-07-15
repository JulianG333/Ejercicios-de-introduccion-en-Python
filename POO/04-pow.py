class Pow:
    def pow(self, x, n):
        return x ** n
    
x = int(input("Ingrese el valor de x(base): "))
n = int(input("Ingrese el valor de n(exponente): "))


pow = Pow()
resultado = pow.pow(x, n)
print(f"Resultado de {x}^{n} es: {resultado}") 