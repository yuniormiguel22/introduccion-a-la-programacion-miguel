numero_valido = False
while not numero_valido:
    entrada = input("Ingresa un número: ")
    try:
        n = int(entrada)
        numero_valido = True
    except ValueError:
        print("Error: debes ingresar un número entero válido.")

print("\nTabla de multiplicar del", n)
print("=" * 25)

for i in range(1, 11):
    resultado = n * i
    print(n, "x", i, "=", resultado)

print("=" * 25)
print("Tabla completada del 1 al 10")