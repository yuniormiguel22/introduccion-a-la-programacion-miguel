contrasena_correcta = "clave123"
intentos = 0
max_intentos = 5

intento = input("Ingresa la contraseña: ")
intentos += 1

while intento != contrasena_correcta:
    print("Contraseña incorrecta, intenta de nuevo.")
    
    if intentos >= max_intentos:
        print("Has alcanzado el número máximo de intentos (" + str(max_intentos) + ").")
        break
    
    intento = input("Ingresa la contraseña: ")
    intentos += 1

if intento == contrasena_correcta:
    print("Acceso concedido. Bienvenido.")
    print("Intentos utilizados:", intentos)