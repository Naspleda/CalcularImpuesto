# Ejercicio: Calculadora de impuestos
# Crear una función para calcular el total de un pago incluyendo impuesto aplicado.
# Formula: pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto/100)


def calcular_pago(pago_sin_impuesto, impuesto):
    pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto/100)
    return pago_total


pago_sin_impuesto = float(input('Proporcione el pago sin impuesto: '))
impuesto = float(input('Proporcione el monto del impuesto: '))
pago_con_impuesto = calcular_pago(pago_sin_impuesto, impuesto)
print(f'El pago total es de: {pago_con_impuesto}')
