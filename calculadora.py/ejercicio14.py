# Identificador de Tipo de Archivo

# Ingresar la extensión del archivo
extension = input("Ingrese la extensión del archivo: ").lower()

# Identificar el tipo de archivo
match extension:
    case "jpg":
        print("Imagen")
    case "mp3":
        print("Audio")
    case "pdf":
        print("Documento de texto")
    case "docx":
        print("Documento de texto")
    case _:
        print("Desconocido")