agenda = [
    ("Juan Perez", "809-555-1234"),
    ("Maria Lopez", "809-555-5678"),
    ("Pedro Gomez", "809-555-9012"),
    ("Laura Diaz", "809-555-3456")
]

nombre_buscar = input("Ingresa el nombre a buscar: ")

encontrado = False
for contacto in agenda:
    if contacto[0] == nombre_buscar:
        print("Telefono encontrado:", contacto[1])
        encontrado = True
        break

if not encontrado:
    print("El nombre no fue encontrado en la agenda.")