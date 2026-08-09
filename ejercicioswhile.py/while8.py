numero_valido = False
while not numero_valido:
    entrada = input("Ingresa el número de términos: ")
    if entrada.isdigit() and int(entrada) > 0:
        n = int(entrada)
        numero_valido = True
    else:
        print("Error: debes ingresar un número entero positivo. Intenta de nuevo.")

print("\nSerie de Fibonacci con", n, "términos:")
print("-" * 30)

a = 0
b = 1
serie = []

for i in range(n):
    print("Término", i + 1, ":", a)
    serie.append(a)
    siguiente = a + b
    a = b
    b = siguiente

print("-" * 30)
print("Serie completa:", serie)