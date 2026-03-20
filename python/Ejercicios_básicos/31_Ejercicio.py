pagos=0
pago=1500
sueldo=0

n= int(input("Ingrese cantidad de empleados: "))

for i in range(n):
    horas = int(input("Ingrese cantidad de horas trabajadas (Ingrese 0 para finalizar): "))
    if horas==0:
        break
    sueldo=(horas*pago)
    pagos+=sueldo

print("La empresa pago en sueldos:", pagos , " por la cantidad: " , n , " de empleados.")
    
