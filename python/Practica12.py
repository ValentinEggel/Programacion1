from collections import Counter
notas = [7, 8, 6, 9, 8, 7, 10, 8, 6, 7, 8]
conteo = Counter(notas)
print(conteo)          
print(conteo.most_common(1))