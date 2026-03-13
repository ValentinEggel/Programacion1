edad = int(input("Ingresá tu edad: "))

if edad>=18:
    print("Sos mayor de edad")
else:
    falta = 18 - edad
    print("Te faltan", falta, "años para ser mayor de edad")

