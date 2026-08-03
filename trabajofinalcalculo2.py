"""
Calculadora de Cálculo 2
=========================
Permite calcular:
  1) Derivadas (de cualquier orden)
  2) Integrales indefinidas
  3) Integrales definidas
  4) Límites

Requiere la librería sympy (incluida por defecto en muchas distros de Python,
si no la tienes, instálala con: pip install sympy)
"""

import sympy as sp

# Variable simbólica principal
x = sp.symbols('x')


def leer_funcion():
    """Pide al usuario una función en términos de x y la convierte a sympy."""
    print("\nEscribe la función en términos de 'x'.")
    print("Ejemplos válidos: x**2 + 3*x, sin(x), exp(x)*cos(x), sqrt(x), 1/x")
    texto = input("f(x) = ")
    try:
        funcion = sp.sympify(texto)
        return funcion
    except (sp.SympifyError, SyntaxError):
        print("⚠️  No se pudo interpretar la función. Intenta de nuevo.")
        return None


def calcular_derivada():
    f = leer_funcion()
    if f is None:
        return
    try:
        orden = int(input("¿Orden de la derivada? (1 = primera, 2 = segunda, ...): ") or "1")
    except ValueError:
        orden = 1

    derivada = sp.diff(f, x, orden)
    derivada_simplificada = sp.simplify(derivada)

    print("\n--- RESULTADO ---")
    print(f"f(x)        = {f}")
    print(f"f^({orden})(x) = {derivada_simplificada}")


def calcular_integral_indefinida():
    f = leer_funcion()
    if f is None:
        return

    integral = sp.integrate(f, x)
    integral_simplificada = sp.simplify(integral)

    print("\n--- RESULTADO ---")
    print(f"f(x)   = {f}")
    print(f"∫f(x)dx = {integral_simplificada} + C")


def calcular_integral_definida():
    f = leer_funcion()
    if f is None:
        return
    try:
        a = sp.sympify(input("Límite inferior (a): "))
        b = sp.sympify(input("Límite superior (b): "))
    except (sp.SympifyError, SyntaxError):
        print("⚠️  Límites inválidos.")
        return

    integral = sp.integrate(f, (x, a, b))

    print("\n--- RESULTADO ---")
    print(f"f(x) = {f}")
    print(f"∫ desde {a} hasta {b} de f(x) dx = {sp.simplify(integral)}")
    try:
        print(f"Valor numérico ≈ {float(integral):.6f}")
    except (TypeError, ValueError):
        pass


def calcular_limite():
    f = leer_funcion()
    if f is None:
        return
    punto = input("¿A qué valor tiende x? (usa 'oo' para infinito): ")
    try:
        punto = sp.sympify(punto)
    except (sp.SympifyError, SyntaxError):
        print("⚠️  Valor inválido.")
        return

    direccion = input("¿Lado? (dejar vacío = ambos, 'izq' o 'der'): ").strip().lower()
    if direccion == "izq":
        resultado = sp.limit(f, x, punto, dir='-')
    elif direccion == "der":
        resultado = sp.limit(f, x, punto, dir='+')
    else:
        resultado = sp.limit(f, x, punto)

    print("\n--- RESULTADO ---")
    print(f"lim_(x->{punto}) {f} = {resultado}")


def menu():
    while True:
        print("\n============================")
        print("  CALCULADORA DE CÁLCULO 2")
        print("============================")
        print("1) Derivada")
        print("2) Integral indefinida")
        print("3) Integral definida")
        print("4) Límite")
        print("5) Salir")
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            calcular_derivada()
        elif opcion == "2":
            calcular_integral_indefinida()
        elif opcion == "3":
            calcular_integral_definida()
        elif opcion == "4":
            calcular_limite()
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("⚠️  Opción no válida, intenta de nuevo.")


if __name__ == "__main__":
    menu()