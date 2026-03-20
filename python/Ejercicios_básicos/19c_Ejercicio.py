imp=float(input("Ingrese importe de la venta: "))
if imp<1500:
    dto=(imp*0.05)
    pf=(imp-dto)
else: 
    dto=(imp*0.10)
    pf=(imp-dto)
(print("El costo final de la venta es de: " , pf ,"pesos."))

