# Simulador de Cajero Automático

# Variable global
saldo_cuenta = 1000

def retirar_dinero(monto):
    global saldo_cuenta

    if monto > saldo_cuenta:
        print("Error: Saldo insuficiente.")
    elif monto % 10 != 0:
        print("Error: El monto debe ser múltiplo de 10.")
    else:
        saldo_cuenta = saldo_cuenta - monto
        print("Retiro realizado con éxito.")
        print("Nuevo saldo:", saldo_cuenta)

# Solicitar el monto a retirar
monto = int(input("Ingrese el monto a retirar: "))

# Llamar a la función
retirar_dinero(monto)