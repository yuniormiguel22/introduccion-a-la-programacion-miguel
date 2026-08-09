numero_valido = False
while not numero_valido:
    entrada = input("Ingresa un número: ")
    if entrada.isdigit():
        n = int(entrada)
        numero_valido = True
    else:
        print("Error: debes ingresar un número entero no negativo.")

factorial = 1
i = 1

print("\nCalculando el factorial de", n)
print("-" * 30)

while i <= n:
    factorial *= i
    print(i, "! parcial ->", factorial)
    i += 1

print("-" * 30)
if n == 0:
    print("El factorial de 0 es 1 (por definición)")
else:
    print("El factorial de", n, "es", factorial)