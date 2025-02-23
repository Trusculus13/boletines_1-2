#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Programa que solicite al usuario dos números enteros y determine si la suma es mayor que 10. 
# Haz un control de excepciones si no se introducen valores numéricos.

__author__ = "Gabriel Gonzalez Kowalska"

try:
    num1 = int(input("Introduce un número entero: "))
    num2 = int(input("Introduce otro número entero: "))
except ValueError:
    print("Error: Debes introducir un número entero.")

suma = num1 + num2

if suma > 10:
    print("La suma de los números es mayor que 10.")
else:
    print("La suma de los números es menor o igual a 10.")
