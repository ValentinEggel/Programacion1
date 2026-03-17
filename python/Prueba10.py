import statistics

notas = [6, 8, 4, 9, 7, 3, 10, 5]

print("Las tres primeras notas son:", notas[0:3])
print("La nota más alta es:", max(notas))
print("La nota más baja es:", min(notas))
print("El promedio de las notas es:", statistics.mean(notas))
print("Ordenadas de mayor a menor:", sorted(notas, reverse=True))