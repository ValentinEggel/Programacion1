#28-Leer 50 números cualquiera y determinar cuál es el mayor y cuál es el menor de ellos. Imprimirlos

import random
lista=[random.randint(1, 100) for _ in range(50)]

mayor=0
menor=100

for numero in lista:
    if numero>mayor:
        mayor=numero
    if numero<menor:
        menor=numero

print(lista)
print("El número mayor de la lista es: " , mayor )
print("El número menor de la lista es: " , menor )
