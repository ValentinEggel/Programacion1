#27-Obtener e imprimir la suma de todos los números pares entre 1 y 100.

lista= range(1, 101)
pares=0

for numero in lista:
    if numero % 2 == 0:
        pares+=numero

print("La suma de los números pares del 1 al 100 es: " , pares)