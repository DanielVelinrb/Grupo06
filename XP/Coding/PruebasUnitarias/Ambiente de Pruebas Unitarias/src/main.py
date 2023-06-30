import math
"""Funciòn que recibe dos numeros de tipo flotante y retorna la suma de los dos nùmeros"""
def suma(num1, num2):
    return num1 + num2

"""Funciòn que recibe dos numeros de tipo flotante y retorna la resta de los dos nùmeros"""
def resta(num1, num2):
    return num1 - num2

"""Funciòn que recibe dos numeros de tipo flotante y retorna el producto de los dos nùmeros"""
def multiplicacion(num1, num2):
    return num1 * num2

"""Funciòn que recibe dos numeros de tipo flotante y retorna la suma de los dos nùmeros"""
def division(num1, num2):
    if num2 == 0:
        print("Error: No es posible dividir entre cero.")
        return None
    return num1 / num2

"""Funciòn que recibe un nùmero de tipo flotante y retorna el seno del nùmero ingresado."""
def seno(angulo):
    return math.sin(math.radians(angulo))

"""Funciòn que recibe un nùmero de tipo flotante y retorna el coseno del nùmero ingresado."""
def coseno(angulo):
    return math.cos(math.radians(angulo))

"""Funciòn que recibe un nùmero de tipo flotante y retorna el tangente del nùmero ingresado."""
def tangente(angulo):
    return math.tan(math.radians(angulo))

"""Funciòn que recibe 6 coeficientes de tipo flotante y retorna el valor de la soluciòn x, y."""
def resolver_ecuaciones(a1, b1, c1, a2, b2, c2):
    determinante = a1 * b2 - a2 * b1

    if determinante == 0:
        return None, None

    x = (c1 * b2 - c2 * b1) / determinante
    y = (a1 * c2 - a2 * c1) / determinante

    return x, y

continuar = True


