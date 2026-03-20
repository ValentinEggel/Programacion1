#6-Una empresa paga a sus vendedores una comisión de 5% sobre la venta. Dado el importe de una venta realizada por un vendedor calcula la comisión correspondiente.

venta= float(input("Ingrese valor de la venta realizada: "))
porc= (venta*0.05)
comision= (venta+porc)
print("El valor de la comisión es de ", porc, "pesos.")
print("El valor de la venta más la comisión es de: " , comision, " pesos")