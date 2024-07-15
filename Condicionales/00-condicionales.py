nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
if edad < 0:
    print("Ingrese un edad valida")
elif edad >= 18:
    print("Usted es mayor de edad")
else:
    print("Usted es menor de edad")
