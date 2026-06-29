# Formateador de Direcciones

calle = input("Ingrese el nombre de la calle: ")
numero = input("Ingrese el número de la casa: ")
ciudad = input("Ingrese la ciudad: ")
codigo_postal = input("Ingrese el código postal: ")

print("\nETIQUETA DE ENVÍO")
print(f"{calle} #{numero}")
print(f"{ciudad}")
print(f"Código Postal: {codigo_postal}")