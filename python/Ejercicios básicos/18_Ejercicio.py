# 18 - Sueldo con antigüedad

nombre = input("Ingrese nombre y apellido: ")
sueldo = float(input("Ingrese sueldo básico: "))
ant = float(input("Ingrese antigüedad en años: "))

if ant < 5:
    bonus = sueldo * 0.20
elif ant >= 5 and ant < 10:
    bonus = sueldo * 0.40
elif ant >= 10 and ant < 15:
    bonus = sueldo * 0.50
elif ant >= 15 and ant < 20:
    bonus = sueldo * 0.70
else:
    bonus = sueldo * 1.00

if sueldo < 8000:
    bonus += 100   # agrega $100 fijo al bonus

sueldoneto = sueldo + bonus

print("Empleado:", nombre)
print("Sueldo básico:", sueldo)
print("Importe antigüedad:", bonus)
print("Sueldo neto:", sueldoneto)