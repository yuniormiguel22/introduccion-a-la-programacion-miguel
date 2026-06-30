# Calculadora de Tarifas de Envío

def calcular_envio(peso, zona):

    match zona:
        case "norte":
            return peso * 5
        case "sur":
            return peso * 4
        case "centro":
            return peso * 3
        case _:
            return "Zona no válida"

# Solicitar datos
peso = float(input("Ingrese el peso del paquete: "))
zona = input("Ingrese la zona (Norte, Sur o Centro): ").lower()

# Llamar a la función
resultado = calcular_envio(peso, zona)

# Mostrar el resultado
print("Costo del envío:", resultado)