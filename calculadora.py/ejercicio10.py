# Determinador de Año Bisiesto

# Ingresar el año
anio = int(input("Ingrese un año: "))

# Verificar si es bisiesto
if anio % 400 == 0:
    print("El año es bisiesto.")
elif anio % 100 == 0:
    print("El año no es bisiesto.")
elif anio % 4 == 0:
    print("El año es bisiesto.")
else:
    print("El año no es bisiesto.")