n = int(input("Ingresa un número entero positivo: "))
temp = n
contador = 0
while temp > 0:
    temp //= 10
    contador += 1
print(f"El número {n} tiene {contador} dígitos")