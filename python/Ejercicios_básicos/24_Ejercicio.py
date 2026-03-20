import statistics

nombres = []
edades = []

for i in range(5):
    nombre = input(f"Ingrese nombre del alumno {i+1}: ")
    edad = int(input(f"Ingrese edad del alumno {i+1}: "))
    nombres.append(nombre)
    edades.append(edad)

indice_mayor = edades.index(max(edades))
indice_menor = edades.index(min(edades))

print("El alumno de mayor edad es:", nombres[indice_mayor])
print("El alumno de menor edad es:", nombres[indice_menor])
print("El promedio de edades es:", statistics.mean(edades), "años.")