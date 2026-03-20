while True:
    n = int(input("Ingrese número (0 para salir): "))
    if n == 0:
        break
    ant = n - 1
    pos = n + 1
    print(f"El número posterior de {n} es {pos} y el anterior es {ant}")