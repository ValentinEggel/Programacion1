color = input("Ingrese color (rojo/verde): ")
tamano = input("Ingrese tamaño (pequeño/mediano/grande): ")
cantidad = int(input("Ingrese cantidad: "))

if color == "rojo":
    if tamano == "pequeño":
        precio = 2.1
    elif tamano == "mediano":
        precio = 3
    else:
        precio = 5.4
elif color == "verde":
    if tamano == "pequeño":
        precio = 1.6
    elif tamano == "mediano":
        precio = 2.3
    else:
        precio = 4.1
else:
    print("Color inválido, ingrese rojo o verde")
    precio = 0
importe = precio * cantidad
print("El importe total es:", importe, "pesos.")