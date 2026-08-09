atletas = [
    ("Carlos", 12.5),
    ("Ana", 11.8),
    ("Luis", 13.2),
    ("Sofia", 11.5),
    ("Pedro", 12.9)
]

atletas_ordenados = sorted(atletas, key=lambda atleta: atleta[1])

print("Los tres primeros lugares son:")
print("1er lugar:", atletas_ordenados[0][0], "-", atletas_ordenados[0][1], "segundos")
print("2do lugar:", atletas_ordenados[1][0], "-", atletas_ordenados[1][1], "segundos")
print("3er lugar:", atletas_ordenados[2][0], "-", atletas_ordenados[2][1], "segundos")