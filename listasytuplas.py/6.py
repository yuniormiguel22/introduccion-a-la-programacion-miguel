ventas = [
    ("Lunes", 1500),
    ("Martes", 2000),
    ("Miercoles", 1800),
    ("Jueves", 2200),
    ("Viernes", 2500),
    ("Sabado", 3000),
    ("Domingo", 1200)
]

total = 0
dia_mayor_venta = ventas[0]

for venta in ventas:
    total += venta[1]
    if venta[1] > dia_mayor_venta[1]:
        dia_mayor_venta = venta

print("Total vendido en la semana:", total)
print("El dia con mayores ventas fue:", dia_mayor_venta[0], "con", dia_mayor_venta[1])