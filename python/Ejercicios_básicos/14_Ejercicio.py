#14-Calcular el costo de un terreno rectangular teniendo como dato el ancho y la longitud en metros y el costo del metro cuadrado. 
# Hay que tener en cuenta si el terreno posee menos de 600 m2 no se tiene descuento., si posee entre 600 y 1000 m2 (incluidos) el descuento será
#del 17% y si tiene más de 1000 metros cuadrados el descuento es del 25%. Calcular el precio final.

ancho= float(input("Ingrese ancho del terreno en metros: "))
long= float(input("Ingrese largo del terreno en metros: "))
costo= float(input("Ingrese costo del metro cuadrado: "))

area=(ancho*long)
calculo=(area*costo)

print("El área total del terreno es de", area, "metros cuadrados, por lo tanto: ")
if area<600:
    print("El costo del terreno no tiene descuento, el precio final es de " , calculo, "pesos")
elif area>=600 and area<=1000:
    desc17= (calculo*0.17)
    costfinal1= (calculo-desc17)
    print("El costo del terreno posee 17 porciento de descuento, el precio final es de " , costfinal1 , "pesos")
elif area>1000:
    desc25=(calculo*0.25)
    costfinal2= (calculo-desc25)
    print("El costo del terreno posee 25 porciento de descuento, el precio final es de " , costfinal2 , "pesos")
