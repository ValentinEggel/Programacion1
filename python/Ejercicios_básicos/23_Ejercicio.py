#23-Dados 79 sueldos de empleados imprimir el sueldo mayor y el menor.

import random
sueldos = [random.randint(100,1000) for _ in range(10)]

sueldomayor= sueldos[0]
sueldomenor=sueldos[0]

for numero in sueldos:
    if numero>sueldomayor:
        sueldomayor=numero
    if numero< sueldomenor:
            sueldomenor=numero

print(sueldos)
print("El sueldo mayor registrado es de:" , sueldomayor )
print("El sueldo menor registrado es de:" , sueldomenor )
