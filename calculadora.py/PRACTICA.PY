"""
Gestor de Registros en Archivo de Texto
-----------------------------------------
Permite crear, leer y actualizar registros con la estructura:

NOMBRE: XXXXX
MATRICULA: XXXXXX
CORREO: XXXXXX
TELEFONO: XXXXXXX

Cada registro se guarda separado por una línea en blanco.
"""

import os

NOMBRE_ARCHIVO = "registros.txt"


def crear_archivo():
    """Crea el archivo si no existe (o lo vacía si el usuario lo confirma)."""
    if os.path.exists(NOMBRE_ARCHIVO):
        respuesta = input(
            f"El archivo '{NOMBRE_ARCHIVO}' ya existe. "
            "¿Deseas vaciarlo y crearlo de nuevo? (s/n): "
        ).strip().lower()
        if respuesta != "s":
            print("Operación cancelada. El archivo existente se conserva.\n")
            return

    with open(NOMBRE_ARCHIVO, "w", encoding="utf-8") as archivo:
        archivo.write("")  # Crea el archivo vacío

    print(f"Archivo '{NOMBRE_ARCHIVO}' creado correctamente.\n")


def guardar_registro():
    """Solicita los datos de un registro y lo agrega al archivo."""
    if not os.path.exists(NOMBRE_ARCHIVO):
        print("Primero debes crear el archivo (opción 1).\n")
        return

    print("--- Nuevo registro ---")
    nombre = input("NOMBRE: ").strip()
    matricula = input("MATRICULA: ").strip()
    correo = input("CORREO: ").strip()
    telefono = input("TELEFONO: ").strip()

    with open(NOMBRE_ARCHIVO, "a", encoding="utf-8") as archivo:
        archivo.write(f"NOMBRE: {nombre}\n")
        archivo.write(f"MATRICULA: {matricula}\n")
        archivo.write(f"CORREO: {correo}\n")
        archivo.write(f"TELEFONO: {telefono}\n")
        archivo.write("\n")  # Línea en blanco para separar registros

    print("Registro guardado correctamente.\n")


def leer_archivo():
    """Muestra el contenido completo del archivo."""
    if not os.path.exists(NOMBRE_ARCHIVO):
        print("El archivo no existe todavía. Créalo primero (opción 1).\n")
        return

    with open(NOMBRE_ARCHIVO, "r", encoding="utf-8") as archivo:
        contenido = archivo.read()

    if contenido.strip() == "":
        print("El archivo está vacío. Aún no hay registros.\n")
    else:
        print("--- Contenido del archivo ---")
        print(contenido)


def actualizar_nombre():
    """Busca un nombre existente en el archivo y lo reemplaza por otro."""
    if not os.path.exists(NOMBRE_ARCHIVO):
        print("El archivo no existe todavía. Créalo primero (opción 1).\n")
        return

    nombre_buscar = input("Escribe el nombre que deseas buscar: ").strip()

    with open(NOMBRE_ARCHIVO, "r", encoding="utf-8") as archivo:
        lineas = archivo.readlines()

    linea_objetivo = f"NOMBRE: {nombre_buscar}\n"
    encontrado = False

    for i, linea in enumerate(lineas):
        if linea.strip() == f"NOMBRE: {nombre_buscar}":
            nuevo_nombre = input("Escribe el nuevo nombre: ").strip()
            lineas[i] = f"NOMBRE: {nuevo_nombre}\n"
            encontrado = True
            break  # Actualiza solo la primera coincidencia

    if encontrado:
        with open(NOMBRE_ARCHIVO, "w", encoding="utf-8") as archivo:
            archivo.writelines(lineas)
        print("Nombre actualizado correctamente.\n")
    else:
        print(f"No se encontró ningún registro con el nombre '{nombre_buscar}'.\n")


def mostrar_menu():
    print("========== MENÚ ==========")
    print("1. Crear archivo")
    print("2. Guardar registros")
    print("3. Leer archivo")
    print("4. Actualizar nombre")
    print("5. Cerrar")
    print("===========================")


def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            crear_archivo()
        elif opcion == "2":
            guardar_registro()
        elif opcion == "3":
            leer_archivo()
        elif opcion == "4":
            actualizar_nombre()
        elif opcion == "5":
            print("Cerrando el programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.\n")


if __name__ == "__main__":
    main()