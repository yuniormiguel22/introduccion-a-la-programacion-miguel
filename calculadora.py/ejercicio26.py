# Determinador de Números Primos

def es_primo(numero):

    match numero:
        case 2 | 3 | 5 | 7:
            return "Número primo"
        case 1 | 4 | 6 | 8 | 9 | 10:
            return "Número compuesto"
        case _:
            return "Número fuera del rango"

# Solicitar un número
numero = int(input("Ingrese un número del 1 al 10: "))

# Llamar a la función
resultado = es_primo(numero)

# Mostrar el resultado
print(resultado)