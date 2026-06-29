# Control de Acceso por Edad

# Solicitar la edad al usuario
edad = int(input("Ingrese su edad: "))

# Evaluar la edad
if edad < 18:
    print("Acceso denegado")
elif edad <= 65:
    print("Acceso permitido")
else:
    print("Acceso preferencial para adultos mayores")