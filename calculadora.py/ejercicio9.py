# Cálculo de Descuentos por Compra

# Ingresar el monto de la compra
compra = float(input("Ingrese el monto de la compra: "))

# Verificar si aplica el descuento
if compra > 100:
    descuento = compra * 0.15
    total = compra - descuento
else:
    total = compra

# Mostrar el total a pagar
print("Total a pagar: $", round(total, 2))