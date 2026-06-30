# Juego de Piedra, Papel o Tijera

jugador1 = input("Jugador 1 (Piedra, Papel o Tijera): ").lower()
jugador2 = input("Jugador 2 (Piedra, Papel o Tijera): ").lower()

if jugador1 == jugador2:
    print("Empate")
else:
    if jugador1 == "piedra":
        if jugador2 == "tijera":
            print("Gana el Jugador 1")
        else:
            print("Gana el Jugador 2")

    elif jugador1 == "papel":
        if jugador2 == "piedra":
            print("Gana el Jugador 1")
        else:
            print("Gana el Jugador 2")

    elif jugador1 == "tijera":
        if jugador2 == "papel":
            print("Gana el Jugador 1")
        else:
            print("Gana el Jugador 2")

    else:
        print("Opción no válida")