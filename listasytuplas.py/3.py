calificaciones = [
    ("Matematicas", 85),
    ("Historia", 65),
    ("Ciencias", 90),
    ("Arte", 55),
    ("Ingles", 75)
]

print("Asignaturas aprobadas:")
suma = 0
for asignatura in calificaciones:
    suma += asignatura[1]
    if asignatura[1] >= 70:
        print("-", asignatura[0], ":", asignatura[1])

promedio = suma / len(calificaciones)
print("Promedio general:", promedio)