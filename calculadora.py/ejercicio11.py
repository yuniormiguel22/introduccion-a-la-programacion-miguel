# Calculadora Aritmética

# Ingresar los datos
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))
operador = input("Ingrese el operador (+, -, *, /): ")

# Realizar la operación
match operador:
    case "+":
        print("Resultado:", numero1 + numero2)
    case "-":
        print("Resultado:", numero1 - numero2)
    case "*":
        print("Resultado:", numero1 * numero2)
    case "/":
        if numero2 != 0:
            print("Resultado:", numero1 / numero2)
        else:
            print("No se puede dividir entre cero.")
    case _:
        print("Operador no válido.")