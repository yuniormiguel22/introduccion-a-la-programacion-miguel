# Definir listas vacías
producto = []
precio = []

# Leer número de productos
n = int(input("Número de productos: "))

# Bucle para leer productos y precios
for i in range(n):
    prod = input(f"Producto {i+1}: ")
    producto.append(prod)
    
    prec = float(input(f"Precio de {prod}: "))
    precio.append(prec)  # Agrega a la lista, no sobrescribe

# Mostrar lista de ventas
print("\n-- LISTA DE VENTAS REGISTRADAS ---")
for i in range(n):
    print(f"Producto: {producto[i]} - Precio: ${precio[i]:.2f}")
