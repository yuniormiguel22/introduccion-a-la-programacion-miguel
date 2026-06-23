#Crear un programa que permita capturar n cantidad de ventas, y registrar el producto y precio para cada transacción. Mostrar o imprimir cada producto con su precio
""""""

ventas = []
n = int(input("¿Cuántas ventas deseas registrar? "))

for i in range(n):
    producto= input(f"Ingresa el nombre del producto {i+1}: ")
    precio = float(input(f"Ingresa el precio del producto {i+1}: "))
    ventas.append({"producto": producto, "precio": precio})

print("\n--- Lista de Ventas Registradas ---")
for venta in ventas:
    print(f"Producto: {venta['producto']}  -  Precio: ${venta['precio']:.2f}")