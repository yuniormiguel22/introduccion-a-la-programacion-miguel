# Simulador de Semáforo

color_semaforo = input("Ingrese el color del semáforo: ").lower()

if color_semaforo == "verde":
    print("Avanzar")
elif color_semaforo == "amarillo":
    print("Frenar con precaución")
elif color_semaforo == "rojo":
    print("Detenerse")
else:
    print("Semáforo averiado")