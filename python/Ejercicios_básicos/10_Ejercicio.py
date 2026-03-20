#10-Construir un algoritmo que permita leer un entero y determinar si es positivo y de 4 dígitos.

valor= int(input("Ingrese valor a evaluar: "))
if valor>=0:
    print("El valor es positivo")
else:
    print ("El valor es negativo")

if valor>999 and valor<=9999:
    print("El valor posee 4 dígitos")
else:
    print("El valor no posee 4 dígitos")