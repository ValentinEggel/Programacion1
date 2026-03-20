aprobados = 0
aplazados = 0
promocionados = 0

while True:
    nota = float(input("Ingrese nota: "))
    if nota == 0:
        break
    if nota >= 6:
        promocionados += 1
    if nota >= 4:
        aprobados += 1
    if nota < 4:
        aplazados += 1

print("Aprobados:", aprobados)
print("Aplazados:", aplazados)
print("Promocionados:", promocionados)
