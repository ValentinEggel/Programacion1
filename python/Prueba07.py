import datetime
import random
import math

fecha = datetime.date.today()
print("La fecha de hoy es:", fecha)

numero = random.randint(1, 100)
print("Número aleatorio del 1 al 100:", numero)

raiz = math.sqrt(numero)
print("Raíz cuadrada del número aleatorio:", round(raiz, 2))
