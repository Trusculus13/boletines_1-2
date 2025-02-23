#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Realiza un programa que compruebe si para dos números introducidos por pantalla 
# uno es divisor del otro.

__author__ = "Gabriel Gonzalez Kowalska"

num1 = int(input("Introduce un número: "))
num2 = int(input("Introduce otro número: "))

if num1 % num2 == 0:
    print(f"{num1} es divisor de {num2}")
elif num2 % num1 == 0:
    print(f"{num2} es divisor de {num1}")
else:
    print("Ninguno de los números es divisor del otro.")
