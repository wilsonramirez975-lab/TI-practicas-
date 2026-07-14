#!/bin/python3

import math
import os
import random
import re
import sys

# Función para calcular la factura
def solve():

    productos = [
        "Ensalada",
        "Arroz",
        "Guandules",
        "Pollo",
        "Agua"
    ]

    subtotal = 0

    print("====================================")
    print("   DE WILSON RESTAURANTE ")
    print("====================================")

    # Solicitar el precio de cada producto
    for producto in productos:
        precio = float(input(f"Ingrese el precio de {producto}: RD$ "))
        subtotal += precio

    # Porcentajes
    propina_percent = 10
    impuesto_percent = 18

    # Cálculos
    propina = subtotal * (propina_percent / 100)
    impuesto = subtotal * (impuesto_percent / 100)
    total = subtotal + propina + impuesto

    # Mostrar factura
    print("\n=========== FACTURA ===========")
    print(f"Subtotal : RD$ {subtotal:.2f}")
    print(f"Propina ({propina_percent}%): RD$ {propina:.2f}")
    print(f"ITBIS ({impuesto_percent}%): RD$ {impuesto:.2f}")
    print("-------------------------------")
    print(f"TOTAL A PAGAR: RD$ {total:.2f}")
    print("===============================")

if __name__ == '__main__':
    solve()