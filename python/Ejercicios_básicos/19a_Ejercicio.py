import statistics
import random

numeros = [random.randint(1, 100) for _ in range(5)]
(print(numeros))
(print("El promedio de los números ingresados es: " , statistics.mean(numeros)))