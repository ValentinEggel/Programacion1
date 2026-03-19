import calendar
import statistics

notas= [8, 6, 9, 7, 5, 10]
promedio= statistics.mean(notas) 
print("El promedio de las notas es de: " , promedio)

bisiesto= calendar.isleap(2026)
print("¿El año 2026 es bisiesto?" , bisiesto)

dias = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
dia = calendar.weekday(2001, 3, 21)
print("Nací un:", dias[dia])
