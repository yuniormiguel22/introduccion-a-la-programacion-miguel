import os

def crear_archivo():
    nombre_archivo = input("Ingresa el nombre del archivo a crear (ejemplo: registros.txt): ")
    if os.path.exists(nombre_archivo):
        print("El archivo ya existe. No se sobrescribirá.")
    else:
        archivo = open(nombre_archivo, "w")
        archivo.close()
        print("Archivo '" + nombre_archivo + "' creado exitosamente.")
    return nombre_archivo


def guardar_registro(nombre_archivo):
    if not os.path.exists(nombre_archivo):
        print("Error: el archivo no existe. Primero crea el archivo.")
        return

    nombre = input("Ingresa el NOMBRE: ")
    matricula = input("Ingresa la MATRICULA: ")
    correo = input("Ingresa el CORREO: ")
    telefono = input("Ingresa el TELEFONO: ")

    archivo = open(nombre_archivo, "a")
    archivo.write("NOMBRE: " + nombre + "\n")
    archivo.write("MATRICULA: " + matricula + "\n")
    archivo.write("CORREO: " + correo + "\n")
    archivo.write("TELEFONO: " + telefono + "\n")
    archivo.write("-" * 30 + "\n")
    archivo.close()

    print("Registro guardado exitosamente.")


def leer_archivo(nombre_archivo):
    if not os.path.exists(nombre_archivo):
        print("Error: el archivo no existe.")
        return

    archivo = open(nombre_archivo, "r")
    contenido = archivo.read()
    archivo.close()

    if contenido == "":
        print("El archivo está vacío.")
    else:
        print("\n" + "=" * 30)
        print("CONTENIDO DEL ARCHIVO")
        print("=" * 30)
        print(contenido)
        print("=" * 30)


def actualizar_nombre(nombre_archivo):
    if not os.path.exists(nombre_archivo):
        print("Error: el archivo no existe.")
        return

    archivo = open(nombre_archivo, "r")
    lineas = archivo.readlines()
    archivo.close()

    nombre_buscar = input("Ingresa el nombre que deseas buscar: ")
    nombre_nuevo = input("Ingresa el nuevo nombre: ")

    encontrado = False
    nuevas_lineas = []

    for linea in lineas:
        if linea.startswith("NOMBRE:"):
            valor_actual = linea.replace("NOMBRE:", "").strip()
            if valor_actual == nombre_buscar:
                nuevas_lineas.append("NOMBRE: " + nombre_nuevo + "\n")
                encontrado = True
            else:
                nuevas_lineas.append(linea)
        else:
            nuevas_lineas.append(linea)

    if encontrado:
        archivo = open(nombre_archivo, "w")
        archivo.writelines(nuevas_lineas)
        archivo.close()
        print("Nombre actualizado exitosamente.")
    else:
        print("No se encontró el nombre '" + nombre_buscar + "' en el archivo.")


def menu():
    nombre_archivo = ""

    while True:
        print("\n" + "=" * 35)
        print("MENU DE GESTION DE ARCHIVOS")
        print("=" * 35)
        print("1. Crear archivo")
        print("2. Guardar registros")
        print("3. Leer archivo")
        print("4. Actualizar nombre")
        print("5. Cerrar")
        print("=" * 35)

        opcion = input("Selecciona una opción (1-5): ")

        if opcion == "1":
            nombre_archivo = crear_archivo()
        elif opcion == "2":
            if nombre_archivo == "":
                nombre_archivo = input("Ingresa el nombre del archivo a usar: ")
            guardar_registro(nombre_archivo)
        elif opcion == "3":
            if nombre_archivo == "":
                nombre_archivo = input("Ingresa el nombre del archivo a usar: ")
            leer_archivo(nombre_archivo)
        elif opcion == "4":
            if nombre_archivo == "":
                nombre_archivo = input("Ingresa el nombre del archivo a usar: ")
            actualizar_nombre(nombre_archivo)
        elif opcion == "5":
            print("Cerrando el programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")


menu()