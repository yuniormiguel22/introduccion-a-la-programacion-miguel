# Función de Saludo Personalizado

def saludar_usuario(nombre, hora_dia):

    if hora_dia == "mañana":
        return f"¡Buenos días, {nombre}!"
    elif hora_dia == "tarde":
        return f"¡Buenas tardes, {nombre}!"
    elif hora_dia == "noche":
        return f"¡Buenas noches, {nombre}!"
    else:
        return f"¡Hola, {nombre}!"

# Pruebas de la función
print(saludar_usuario("Carlos", "mañana"))
print(saludar_usuario("Ana", "tarde"))
print(saludar_usuario("Luis", "noche"))