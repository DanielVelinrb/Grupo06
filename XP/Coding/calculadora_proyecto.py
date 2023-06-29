import math

"""Funciòn que muestra un menù cuando se ejecuta el programa, 
se muestran 4 opciones para que el usuario pueda seleccionar que operaciòn desea realizar. """
def mostrar_menu():
    print("==== Calculadora ====")
    print("1. Operaciones matemáticas básicas")
    print("2. Salir")


"""Funciòn para realizar operaciones matemàticas bàsicas, 
el usuario tendrà que ingresar dos nùmeros para realziar una de las operaciones de este apartado.
luego se mostrar un submenù para elegir que opraciòn bàsica realizarà el usuario."""
def realizar_operaciones_basicas():
    print(type(realizar_operaciones_basicas))
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))
    operador = input("Introduce el operador (+, -, *, /): ")
    
    resultado = None
    if operador == '+':
        resultado = suma(num1, num2)
    elif operador == '-':
        resultado = resta(num1, num2)
    elif operador == '*':
        resultado = multiplicacion(num1, num2)
    elif operador == '/':
        resultado = division(num1, num2)
    else:
        print("Operador inválido. Introduce un operador válido.")
    
    if resultado is not None:
        print("El resultado es: {:.2f}".format(resultado))



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


continuar = True
while continuar:
    mostrar_menu()
    opcion = int(input("Elige una opción (1-4): "))
    if opcion == 1:
        realizar_operaciones_basicas()
    elif opcion == 2:
        print("¡Hasta luego!")
        continuar = False
