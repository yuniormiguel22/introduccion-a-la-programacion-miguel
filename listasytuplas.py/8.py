libros = [
    ("Cien años de soledad", "Gabriel Garcia Marquez", 1967),
    ("El principito", "Antoine de Saint-Exupery", 1943),
    ("Sapiens", "Yuval Noah Harari", 2011),
    ("Educated", "Tara Westover", 2018),
    ("Atomic Habits", "James Clear", 2018),
    ("Becoming", "Michelle Obama", 2018)
]

print("Libros publicados despues de 2015:")
contador = 0
for libro in libros:
    if libro[2] > 2015:
        print("-", libro[0], "por", libro[1], "(", libro[2], ")")
        contador += 1

print("\nTotal de libros publicados despues de 2015:", contador)