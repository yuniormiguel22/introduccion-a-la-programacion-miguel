ciudades = [
    ("Santo Domingo", 32),
    ("Santiago", 30),
    ("Puerto Plata", 28),
    ("La Vega", 26),
    ("Barahona", 34)
]

mas_calida = ciudades[0]
mas_fria = ciudades[0]

for ciudad in ciudades:
    if ciudad[1] > mas_calida[1]:
        mas_calida = ciudad
    if ciudad[1] < mas_fria[1]:
        mas_fria = ciudad

print("La ciudad con mayor temperatura es:", mas_calida[0], "con", mas_calida[1], "grados")
print("La ciudad con menor temperatura es:", mas_fria[0], "con", mas_fria[1], "grados")