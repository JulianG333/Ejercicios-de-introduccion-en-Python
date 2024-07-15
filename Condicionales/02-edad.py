print("Programa para verificar su rango de edad")
nombre_usuario = input("Escriba su nombre: ")
edad_usuario = int(input("Escriba su edad: "))
#Se determina su rango de edad
if edad_usuario < 0 or edad_usuario > 100:
    print("Ingrese un edad valida")
elif edad_usuario >= 18:
    print(f"Hola {nombre_usuario}, usted es mayor de edad")
else:
    print(f"Hola {nombre_usuario}, usted es menor de edad")