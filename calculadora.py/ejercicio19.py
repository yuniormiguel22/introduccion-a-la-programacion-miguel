# Función Máximo de Tres Números

def mayor_numero(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

# Solicitar los números al usuario
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))
numero3 = float(input("Ingrese el tercer número: "))

# Llamar a la función
resultado = mayor_numero(numero1, numero2, numero3)

# Mostrar el resultado
print("El número mayor es:", resultado)