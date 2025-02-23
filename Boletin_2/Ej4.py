#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Crea un programa que indique si es par o impar el número introducido. 
# Haz un control de excepciones si no se introducen valores numéricos.

__author__ = "Gabriel Gonzalez Kowalska"

try:
    num1 = int(input("Introduce un número: "))
except ValueError:
    print("Error: Debes introducir valores numéricos.")
    exit()

if num1 % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")
