# Clasificador de Números

# Solicitar un número al usuario
numero = int(input("Ingrese un número entero: "))

# Clasificar el número
if numero > 0:
    if numero % 2 == 0:
        print("Positivo y Par")
    else:
        print("Positivo e Impar")
elif numero < 0:
    print("Negativo")
else:
    print("Cero")