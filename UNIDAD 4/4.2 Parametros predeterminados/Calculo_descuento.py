# función para calcular el descuneto


def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el descuento y devuelve el monto del descuento.

    :param monto_total: Monto total de la compra.
    :param porcentaje_descuento: Porcentaje de descuento (por defecto 10%).
    :return: Monto del descuento.
    """
    descuento = (monto_total * porcentaje_descuento) / 100
    return descuento


def main():
    # Primer caso: monto total de la compra
    monto1 = 150.00
    descuento1 = calcular_descuento(monto1)
    monto_final1 = monto1 - descuento1

    print(f"Monto total: ${monto1:.2f}")
    print(f"Descuento (10%): ${descuento1:.2f}")
    print(f"Monto final a pagar: ${monto_final1:.2f}\n")

    # Segundo caso: monto total de la compra y porcentaje de descuento
    monto2 = 200.00
    porcentaje2 = 15  # 15% de descuento
    descuento2 = calcular_descuento(monto2, porcentaje2)
    monto_final2 = monto2 - descuento2

    print(f"Monto total: ${monto2:.2f}")
    print(f"Descuento ({porcentaje2}%): ${descuento2:.2f}")
    print(f"Monto final a pagar: ${monto_final2:.2f}")


if __name__ == "__main__":
    main()
