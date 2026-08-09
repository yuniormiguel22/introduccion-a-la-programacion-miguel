estudiantes = [
    ("Ana", 20),
    ("Luis", 22),
    ("Marta", 19),
    ("Carlos", 23),
    ("Sofia", 21)
]

mayor = estudiantes[0]
for estudiante in estudiantes:
    if estudiante[1] > mayor[1]:
        mayor = estudiante

print("El estudiante de mayor edad es:", mayor[0], "con", mayor[1], "años")