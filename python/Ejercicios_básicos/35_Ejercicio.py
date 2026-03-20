#35-Elaborar un algoritmo que lea 3 números enteros diferentes entre si y determinar el mayor de los tres.
may=0

n1= int(input("INGRESE EL PRIMER VALOR: "))
n2= int(input("INGRESE EL SEGUNDO VALOR: "))
n3= int(input("INGRESE EL TERCER VALOR: "))

may = max(n1, n2, n3)

print(f"El valor mayor es {may}")