import math
import os
import random
import re
import sys

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

if __name__ == '__main__':
    # Pedimos el número directamente por consola
    n = int(input("Ingresa un número: ").strip())

    result = factorial(n)

    # Imprimimos el resultado en pantalla
    print(f"El factorial es: {result}")