# Función Área de un Triángulo

def calcular_area_triangulo(base, altura):
    area = (base * altura) / 2
    return area

# Solicitar datos al usuario
base = float(input("Ingrese la base del triángulo: "))
altura = float(input("Ingrese la altura del triángulo: "))

# Llamar a la función
resultado = calcular_area_triangulo(base, altura)

# Mostrar el resultado
print("El área del triángulo es:", resultado)