while True:
    horas = int(input("Ingrese horas trabajadas: "))
    
    if horas <= 40:
        sueldo = horas * 16
        print("El sueldo es:", sueldo, "pesos.")
        break  # termina porque no hay horas extra
    else:
        extra = horas - 40
        sueldo = (40 * 16) + (extra * 20)
        print("El sueldo es:", sueldo, "pesos.")


    