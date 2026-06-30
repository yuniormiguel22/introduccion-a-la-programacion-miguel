# Validador de Triángulos

def validar_triangulo(lado1, lado2, lado3):

    # Verificar si puede formar un triángulo
    if lado1 + lado2 <= lado3 or lado1 + lado3 <= lado2 or lado2 + lado3 <= lado1:
        return "No es un triángulo válido"

    # Clasificar el triángulo
    if lado1 == lado2 and lado2 == lado3:
        return "Equilátero"
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        return "Isósceles"
    else:
        return "Escaleno"

# Solicitar los lados
lado1 = float(input("Ingrese el primer lado: "))
lado2 = float(input("Ingrese el segundo lado: "))
lado3 = float(input("Ingrese el tercer lado: "))

# Llamar a la función
resultado = validar_triangulo(lado1, lado2, lado3)

# Mostrar el resultado
print("Resultado:", resultado)