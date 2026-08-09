numero_valido = False
while not numero_valido:
    entrada = input("Ingresa un número entero positivo: ")
    if entrada.isdigit() and int(entrada) > 0:
        n = int(entrada)
        numero_valido = True
    else:
        print("Error: debes ingresar un número entero positivo. Intenta de nuevo.")

print("\nNúmeros impares del 1 al", n, ":")
print("-" * 30)

i = 1
contador_impares = 0

while i <= n:
    if i % 2 != 0:
        print("Impar:", i)
        contador_impares += 1
    i += 1

print("-" * 30)
print("Se encontraron", contador_impares, "números impares")