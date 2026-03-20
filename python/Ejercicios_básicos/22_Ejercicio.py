import random
numeros = [random.randint(-9999, 9999) for _ in range(25)]

suma_pares = 0
suma_impares = 0
suma_positivos = 0
suma_negativos = 0
cant_positivos = 0
cant_negativos = 0
cant_nulos = 0

for numero in numeros:
    # pares e impares
    if numero % 2 == 0:
        suma_pares += numero
    else:
        suma_impares += numero

    # positivos, negativos y nulos
    if numero > 0:
        suma_positivos += numero
        cant_positivos += 1
    elif numero < 0:
        suma_negativos += numero
        cant_negativos += 1
    else:
        cant_nulos += 1

print(numeros)

print("La cantidad de la suma de los numeros pares es: " , suma_pares)
print("La cantidad de la suma de los numeros impares es: " , suma_impares)
print("La cantidad de la suma de los numeros positivos es: " , suma_positivos)
print("La cantidad de la suma de los numeros negativos es: " , suma_negativos)
print("La cantidad de números positivos es : " , cant_positivos)
print("La cantidad de números negativos es: " , cant_negativos)
print("La cantidad de los numeros nulos es: " , cant_nulos )

    