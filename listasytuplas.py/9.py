encuesta = [
    ("Juan", 5),
    ("Maria", 3),
    ("Pedro", 4),
    ("Laura", 5),
    ("Carlos", 2),
    ("Ana", 5)
]

suma = 0
nombres_cinco = []

for respuesta in encuesta:
    suma += respuesta[1]
    if respuesta[1] == 5:
        nombres_cinco.append(respuesta[0])

promedio = suma / len(encuesta)

print("Puntuacion promedio de la encuesta:", promedio)
print("Personas que calificaron con 5:", nombres_cinco)