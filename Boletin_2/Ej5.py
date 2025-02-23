#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Implementar una aplicación que calcule el menor de tres números introducidos por el
# usuario mediante el teclado. Asegúrate primero de que ningún par de números sea igual. 
# Si esto ocurre, indícalo al usuario y no calcules cuál es el menor de los 3. 
# Haz un control de excepciones si no se introducen valores numéricos.

__author__ = "Gabriel Gonzalez Kowalska"

try:
    num1 = int(input("Introduce un numero: "))
    num2 = int(input("Introduce otro numero: "))
    num3 = int(input("Introduce otro numero: "))
except ValueError:
    print("Error: Debes introducir valores numéricos.")
    exit()

if num1 == num2 or num1 == num3 or num2 == num3:
    print("Al menos dos números son iguales.")
else:
    if num1 < num2 and num1 < num3:
        print("El numero menor es: ", num1)
    elif num2 < num1 and num2 < num3:
        print("El numero menor es: ", num2)
    else:
        print("El numero menor es: ", num3)
