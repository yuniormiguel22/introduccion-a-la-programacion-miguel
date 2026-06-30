# Solicitamos la nota al usuario y la convertimos a un número entero
try:
    nota = int(input("Introduce una calificación numérica (1 al 5): "))

    
    match nota:
        case 1 | 2:
            resultado = "Insuficiente"
        case 3:
            resultado = "Suficiente"
        case 4:
            resultado = "Notable"
        case 5:
            resultado = "Sobresaliente"
        case _:  # El guion bajo sirve como comodín para cualquier otro valor
            resultado = "Nota no válida"

    print(f"Resultado: {resultado}")

except ValueError:
    print("Por favor, introduce un número entero válido.")