sucursales = [
    ("Sucursal Norte", [15000, 18000, 20000, 17000]),
    ("Sucursal Sur", [12000, 13000, 11000, 14000]),
    ("Sucursal Este", [22000, 25000, 23000, 24000]),
    ("Sucursal Oeste", [16000, 15000, 17000, 18000])
]

totales = []
promedios = []

print("Total de ventas por sucursal:")
for sucursal in sucursales:
    nombre = sucursal[0]
    ventas_mensuales = sucursal[1]
    total = sum(ventas_mensuales)
    promedio = total / len(ventas_mensuales)
    totales.append((nombre, total))
    promedios.append((nombre, promedio))
    print("-", nombre, ": $", total)

sucursal_mayor = totales[0]
for t in totales:
    if t[1] > sucursal_mayor[1]:
        sucursal_mayor = t

print("\nLa sucursal con mayor total de ventas es:", sucursal_mayor[0], "con $", sucursal_mayor[1])

print("\nPromedio mensual por sucursal:")
for p in promedios:
    print("-", p[0], ": $", p[1])

suma_promedios = 0
for p in promedios:
    suma_promedios += p[1]

promedio_general = suma_promedios / len(promedios)
print("\nPromedio general de todas las sucursales: $", promedio_general)

print("\nSucursales con promedio mensual superior al promedio general:")
for p in promedios:
    if p[1] > promedio_general:
        print("-", p[0], ": $", p[1])