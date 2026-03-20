suma_ninos = 0
suma_jovenes = 0
suma_adultos = 0
suma_am = 0
cant_ninos = 0
cant_jovenes = 0
cant_adultos = 0
cant_am = 0

for i in range(5):
    edad = int(input(f"Persona {i+1} - Edad: "))
    peso = int(input(f"Persona {i+1} - Peso: "))

    if edad <= 12:
        suma_ninos += peso
        cant_ninos += 1
    elif edad <= 29:
        suma_jovenes += peso
        cant_jovenes += 1
    elif edad <= 59:
        suma_adultos += peso
        cant_adultos += 1
    else:
        suma_am += peso
        cant_am += 1

print("Promedio peso niños:", suma_ninos / cant_ninos)
print("Promedio peso jóvenes:", suma_jovenes / cant_jovenes)
print("Promedio peso adultos:", suma_adultos / cant_adultos)
print("Promedio peso adultos mayores:", suma_am / cant_am)