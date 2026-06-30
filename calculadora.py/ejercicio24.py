# Función para calcular la tarifa del estacionamiento

def calcular_tarifa_estacionamiento(horas):

    # Si se estaciona 2 horas o menos
    if horas <= 2:
        return horas * 2.00

    # Si permanece más de 2 horas
    else:
        costo_primeras_dos = 2 * 2.00
        horas_adicionales = horas - 2
        costo_adicional = horas_adicionales * 1.50

        return costo_primeras_dos + costo_adicional

# Solicitar las horas al usuario
horas = int(input("Ingrese la cantidad de horas: "))

# Llamar a la función
total = calcular_tarifa_estacionamiento(horas)

# Mostrar el resultado
print("Total a pagar: $", total)