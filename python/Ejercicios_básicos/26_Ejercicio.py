import random

mayores20 = 0
mayores60 = 0
comprendidos = 0

numeros = [random.randint(1, 100) for _ in range(15)]

for numero in numeros:
    if numero > 20:
        mayores20 += 1
    if numero > 60:
        mayores60 += 1
    if 55 <= numero <= 85:
        comprendidos += 1

print(numeros)
print("Números mayores a 20:", mayores20)
print("Números mayores a 60:", mayores60)
print("Números entre 55 y 85:", comprendidos)
