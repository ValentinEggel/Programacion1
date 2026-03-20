numero= int((input("Ingrese número:")))
if 10 <= numero <= 99:
    decena = numero // 10   # 4
    unidad = numero % 10    # 7
    suma = decena + unidad  # 4 + 7 = 11
    print("La suma del primer dígito con el segundo da como resultado: " , suma)
else:
    print("El número no posee dos dígitos")

