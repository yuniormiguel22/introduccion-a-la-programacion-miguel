# Calculadora de IVA

# Entrada de datos
precio = float(input("Ingrese el precio del producto: RD$ "))
porcentaje_iva = float(input("Ingrese el porcentaje de IVA: "))

# Cálculos
monto_iva = precio * porcentaje_iva / 100
precio_final = precio + monto_iva

# Salida de resultados
print("\n===== DESGLOSE DE LA COMPRA =====")
print(f"Precio del producto: RD$ {precio:.2f}")
print(f"Porcentaje de IVA: {porcentaje_iva:.0f}%")
print(f"Monto del IVA: RD$ {monto_iva:.2f}")
print(f"Precio final: RD$ {precio_final:.2f}")