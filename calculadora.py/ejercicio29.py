# Calculadora de Impuestos Progresiva

def calcular_salario_neto(salario):

    if salario < 1500:
        impuesto = 0

    elif salario <= 3000:
        impuesto = (salario - 1500) * 0.10

    else:
        impuesto = (salario - 3000) * 0.20

    salario_neto = salario - impuesto
    return salario_neto

# Solicitar el salario
salario = float(input("Ingrese el salario bruto: "))

# Llamar a la función
resultado = calcular_salario_neto(salario)

# Mostrar el resultado
print("Salario neto:", resultado)