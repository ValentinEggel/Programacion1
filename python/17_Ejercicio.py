# 17 - Descuentos en ventas

valorcompra = float(input("Ingrese el valor de la compra: "))

if valorcompra < 1000:
    descuento = valorcompra * 0.05
elif 1000 <= valorcompra < 2000:
    descuento = valorcompra * 0.10
else:
    descuento = valorcompra * 0.15

final = valorcompra - descuento
print("El valor final de la compra con descuento es de:", final, "pesos.")


