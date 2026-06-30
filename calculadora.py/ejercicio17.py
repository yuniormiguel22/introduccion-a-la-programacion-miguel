# Función de Conversión de Moneda

def convertir_usd_a_eur(cantidad_usd, tasa_cambio):
    euros = cantidad_usd * tasa_cambio
    return euros

# Solicitar datos al usuario
dolares = float(input("Ingrese la cantidad en dólares: "))
tasa = float(input("Ingrese la tasa de cambio: "))

# Llamar a la función
resultado = convertir_usd_a_eur(dolares, tasa)

# Mostrar el resultado
print("Equivale a", round(resultado, 2), "euros.")