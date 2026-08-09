suma = 0
print("Sumando los números del 1 al 100...")
print("-" * 30)

for i in range(1, 101):
    suma += i
    if i % 10 == 0:
        print("Suma parcial hasta", i, "->", suma)

print("-" * 30)
print("La suma total de 1 a 100 es:", suma)

n = 100
suma_formula = n * (n + 1) // 2
print("Verificación con fórmula de Gauss:", suma_formula)