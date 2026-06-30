# Función Verificadora de Contraseñas

def validar_longitud_password(password):
    if len(password) >= 8:
        return True
    else:
        return False

password = input("Ingrese una contraseña: ")

resultado = validar_longitud_password(password)

# Mostrar el resultado
print(resultado)