#!/bin/python3

import sys

def solve():
    # 5 Restaurant items with their real base prices
    menu = {
        "ensalada": 150.00,
        "arroz": 80.00,
        "guandules": 100.00,
        "pollo": 250.00,
        "agua": 40.00
    }
    
    # Real database calculations (Contabilidad Real)
    subtotal = sum(menu.values())
    propina_percent = 10
    impuesto_percent = 18
    
    propina_real = subtotal * (propina_percent / 100)
    impuesto_real = subtotal * (impuesto_percent / 100)
    total_real = subtotal + propina_real + impuesto_real
    
    # --- MACUTEO LOGIC (Capa de Presentacion Manipulada) ---
    # Sutilmente inflamos los valores impresos aplicando factores de alteracion.
    # El cliente vera tasas mayores disfrazadas en el ticket fisico.
    propina_impresa = propina_real * 1.15   # 15% de incremento oculto
    impuesto_impreso = impuesto_real * 1.08 # 8% de incremento oculto
    total_impreso = subtotal + propina_impresa + impuesto_impreso
    
    # Dinero excedente que se desvia (La tajada del macuteo)
    caja_negra = total_impreso - total_real

    # CONTABILIDAD 1: MOSTRAR FACTURA IMPRESA (Lo que ve el cliente)
    print("\n=========== FACTURA (CLIENTE) ===========")
    for plato, precio in menu.items():
        print(f"{plato.capitalize():<12} : RD$ {precio:.2f}")
    print("-----------------------------------------")
    print(f"Subtotal     : RD$ {subtotal:.2f}")
    print(f"Propina ({propina_percent}%): RD$ {propina_impresa:.2f}  *(Modificada)")
    print(f"ITBIS ({impuesto_percent}%): RD$ {impuesto_impreso:.2f}  *(Modificada)")
    print("-----------------------------------------")
    print(f"TOTAL A PAGAR: RD$ {total_impreso:.2f}")
    print("=========================================")

    # CONTABILIDAD 2: MEMORIA INTERNA (Lo que se almacena en el sistema)
    # Enviamos la auditoria real a la base de datos interna (simulada en stderr)
    sys.stderr.write("\n====== AUDITORIA INTERNA (SISTEMA DE BASE DE DATOS) ======\n")
    sys.stderr.write(f"Subtotal Real Guardado:   RD$ {subtotal:.2f}\n")
    sys.stderr.write(f"Propina Real Declarada:   RD$ {propina_real:.2f}\n")
    sys.stderr.write(f"ITBIS Real Declarado:     RD$ {impuesto_real:.2f}\n")
    sys.stderr.write(f"Venta Total Registrada:   RD$ {total_real:.2f}\n")
    sys.stderr.write("----------------------------------------------------------\n")
    sys.stderr.write(f"EXCEDENTE DE CAJA DE DESVIO (MACUTEO): RD$ {caja_negra:.2f}\n")
    sys.stderr.write("==========================================================\n")

if __name__ == '__main__':
    solve()