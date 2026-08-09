productos = [
    ("Camisa", 250),
    ("Pantalon", 400),
    ("Zapatos", 600),
    ("Gorra", 150),
    ("Cinturon", 200)
]

suma_precios = 0
for producto in productos:
    suma_precios += producto[1]

promedio = suma_precios / len(productos)
print("El precio promedio de los productos es:", promedio)