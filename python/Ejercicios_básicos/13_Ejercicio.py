#13 -Suma o multiplicación de dos números
#1º) Pida por teclado dos números (datos enteros).
#2º) Calcule la suma y multiplicación de ambos números.
#3º) Muestre por pantalla:
#• "La suma es mayor.", en caso de que sea mayor que la multiplicación de ambos números.
#• "La multiplicación es mayor.", en caso de que sea mayor que la suma de ambos números.
#• "La suma y multiplicación son iguales.", en caso de que así sea.

v1= int(input("Ingrese el primer valor: "))
v2= int(input("Ingrese el segundo valor: "))

suma= (v1+v2)
mult= (v1*v2)

if suma>mult:
    print("El valor de la suma de los números es mayor")
elif mult>suma:
    print("El valor del producto de los números es mayor")
else:
    print("Ambos resultados son iguales")