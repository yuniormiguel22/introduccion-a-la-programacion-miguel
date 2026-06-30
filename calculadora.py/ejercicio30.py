# Evaluador de Desempeño de Empleados

ventas_mes = int(input("Ingrese la cantidad de ventas del mes: "))
asistencia_perfecta = input("¿Tiene asistencia perfecta? (si/no): ").lower()

if asistencia_perfecta == "si":
    asistencia_perfecta = True
else:
    asistencia_perfecta = False

if ventas_mes > 50 and asistencia_perfecta:
    print("Bono Premium")
elif ventas_mes > 50 or asistencia_perfecta:
    print("Bono Estándar")
else:
    print("No recibe bono")