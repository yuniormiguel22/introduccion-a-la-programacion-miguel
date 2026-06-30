# Sistema de Calificación Escolar

def clasificar_nota(nota):
    if nota < 60:
        return "Reprobado"
    elif nota <= 89:
        return "Aprobado"
    else:
        return "Excelente"

# Solicitar la nota al usuario
nota = float(input("Ingrese la nota final: "))

# Llamar a la función
resultado = clasificar_nota(nota)

# Mostrar el resultado
print("Resultado:", resultado)