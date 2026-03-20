#7-Calcular el importe de una factura por consumo de energía eléctrica, dados los siguientes datos:
#-Indicación del medidor al término del periodo anterior
#-Indicación del medidor al término del periodo presente
#-Precio del kw por hora


medant= float(input("Ingrese consumo del medidor anterior: "))
medact= float(input("Ingrese consumo del medidor actual: "))
valor= float(input("Ingrese valor por Kw: "))

importe= (medact-medant)*valor

print("El importe de la factura es de: " , importe , " pesos.")