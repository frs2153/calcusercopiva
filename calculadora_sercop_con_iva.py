
from decimal import Decimal, getcontext, ROUND_HALF_UP

# Configuramos precisión alta
getcontext().prec = 30

def redondeo_sercop(valor_str):
    valor = Decimal(valor_str)
    return valor.quantize(Decimal('0.0001'), rounding=ROUND_HALF_UP)

def calcular_total(valor_unitario, cantidad, iva_porcentaje=15):
    subtotal = valor_unitario * cantidad
    subtotal_redondeado = subtotal.quantize(Decimal('0.0001'), rounding=ROUND_HALF_UP)
    iva = (subtotal_redondeado * Decimal(iva_porcentaje) / Decimal(100)).quantize(Decimal('0.0001'), rounding=ROUND_HALF_UP)
    total = (subtotal_redondeado + iva).quantize(Decimal('0.0001'), rounding=ROUND_HALF_UP)
    return subtotal_redondeado, iva, total

if __name__ == "__main__":
    print("Calculadora de redondeo SERCOP Ecuador con IVA\n")
    while True:
        entrada = input("Ingresa un valor unitario con muchos decimales (o escribe 'salir'): ").strip()
        if entrada.lower() == 'salir':
            break
        cantidad_input = input("Ingresa la cantidad (entero): ").strip()
        try:
            valor_unitario = redondeo_sercop(entrada)
            cantidad = int(cantidad_input)
            subtotal, iva, total = calcular_total(valor_unitario, cantidad)

            print(f"Valor ingresado: {entrada}")
            print(f"Redondeado a 4 decimales: {valor_unitario}")
            print(f"Cantidad: {cantidad}")
            print(f"Subtotal: {subtotal}")
            print(f"IVA 15%: {iva}")
            print(f"Total con IVA: {total}\n")
        except Exception as e:
            print(f"Error: {e}\n")
