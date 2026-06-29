# Calculadora de Promedio Simple

# Ingresar las calificaciones
nota1 = float(input("Ingrese la primera calificación: "))
nota2 = float(input("Ingrese la segunda calificación: "))
nota3 = float(input("Ingrese la tercera calificación: "))

# Calcular el promedio
promedio = (nota1 + nota2 + nota3) / 3

# Mostrar el resultado
print("\nEl promedio del estudiante es:", round(promedio, 2))