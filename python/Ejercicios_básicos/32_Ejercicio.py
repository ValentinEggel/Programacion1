pago_mensual = 10
total_pagado = 0

for mes in range(1, 21):
    total_pagado += pago_mensual
    print("Mes", mes, "- Pago:", pago_mensual, "pesos.")
    pago_mensual *= 2

print("Total pagado después de 20 meses:", total_pagado, "pesos.")