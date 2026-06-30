# Calculadora de IMC

def calcular_imc(peso, estatura):
    imc = peso / (estatura * estatura)

    if imc < 18.5:
        return "Bajo peso"
    elif imc < 25:
        return "Peso normal"
    else:
        return "Sobrepeso"

# Solicitar datos al usuario
peso = float(input("Ingrese su peso en kg: "))
estatura = float(input("Ingrese su estatura en metros: "))

# Llamar a la función
resultado = calcular_imc(peso, estatura)

# Mostrar el resultado
print("Clasificación:", resultado)