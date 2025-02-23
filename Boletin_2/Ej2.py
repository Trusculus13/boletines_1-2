#!/usr/bin/env python
# -*- coding: utf-8 -*-

# A partir de un número introducido por pantalla, crear un algoritmo que indique si es
# un número positivo, negativo o igual a cero. Haz un control de excepciones si no se
# introducen valores numéricos.

__author__ = "Gabriel Gonzalez Kowalska"

try:
    num1 = int(input("Introduce un número: "))
except ValueError:
    print("Error: Debes introducir valores numéricos.")
    exit()

if num1 > 0:
    print("El número es positivo.")
elif num1 < 0:
    print("El número es negativo.")
else:
    print("El número es igual a cero.")
