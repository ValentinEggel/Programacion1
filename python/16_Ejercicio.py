#6- Conocido el apellido de un socio de un club y su edad. Indica a que categoría pertenece según lo siguiente:
#Categoría Infantil , menor a 13 años Categoría Mayor , mayor o igual a 18 años
#Categoría Menor , mayor e igual a 13 años y menor e igual a 17 años
#Se solicita imprimir apellido y categoría

nombre= (input("Ingrese nombre y apellido del jugador: "))
edad= int(input("Ingrese edad del jugador: "))
if edad<13:
    print("Bienvenido ", nombre , " usted pertenece a la categoría: INFANTIL")
elif edad>=13 and edad<=17:
    print("Bienvenido ", nombre , " usted pertenece a la categoría: MENOR")
else:
    print("Bienvenido ", nombre , " usted pertenece a la categoría: MAYOR")