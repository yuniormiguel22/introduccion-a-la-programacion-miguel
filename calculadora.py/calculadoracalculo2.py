# ============================================
# CALCULADORA DE CALCULO 2
# Hace 3 cosas: derivadas, integrales y limites
# Usa la libreria sympy para calcular simbolicamente
# (si no la tienes: pip install sympy)
# ============================================

import sympy as sp

# Creamos la variable "x" que vamos a usar en todas las funciones
x = sp.symbols('x')

# Mostramos el menu una y otra vez hasta que el usuario elija salir
while True:

    print("\n---------------------------------")
    print(" CALCULADORA DE CALCULO 2")
    print("---------------------------------")
    print("1. Derivada")
    print("2. Integral indefinida")
    print("3. Integral definida")
    print("4. Limite")
    print("5. Salir")

    opcion = input("Elige una opcion: ")

    # ---------- OPCION 1: DERIVADA ----------
    if opcion == "1":
        texto = input("Escribe la funcion f(x), ejemplo x**2 + sin(x): ")
        f = sp.sympify(texto)          # convierte el texto en una funcion matematica
        derivada = sp.diff(f, x)       # sympy calcula la derivada
        print("La derivada de", f, "es:", sp.simplify(derivada))

    # ---------- OPCION 2: INTEGRAL INDEFINIDA ----------
    elif opcion == "2":
        texto = input("Escribe la funcion f(x): ")
        f = sp.sympify(texto)
        integral = sp.integrate(f, x)  # sympy calcula la antiderivada
        print("La integral de", f, "es:", sp.simplify(integral), "+ C")

    # ---------- OPCION 3: INTEGRAL DEFINIDA ----------
    elif opcion == "3":
        texto = input("Escribe la funcion f(x): ")
        f = sp.sympify(texto)
        a = sp.sympify(input("Limite inferior (a): "))
        b = sp.sympify(input("Limite superior (b): "))
        resultado = sp.integrate(f, (x, a, b))   # integral entre a y b
        print("El area bajo la curva entre", a, "y", b, "es:", resultado)

    # ---------- OPCION 4: LIMITE ----------
    elif opcion == "4":
        texto = input("Escribe la funcion f(x): ")
        f = sp.sympify(texto)
        punto = sp.sympify(input("A que valor tiende x (usa oo para infinito): "))
        resultado = sp.limit(f, x, punto)
        print("El limite de", f, "cuando x tiende a", punto, "es:", resultado)

    # ---------- OPCION 5: SALIR ----------
    elif opcion == "5":
        print("Programa finalizado.")
        break

    # ---------- OPCION INVALIDA ----------
    else:
        print("Esa opcion no existe, intenta de nuevo.")