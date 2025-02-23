#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Crea una aplicación que solicite al usuario un año e indique si es bisiesto o no.
# Condiciones para ser bisiesto:
# ● Debe ser obligatoriamente divisible por 4.
# ● Si es divisible por 100, también debe ser divisible por 400.

__author__ = "Gabriel Gonzalez Kowalska"

try:
    año = int(input("Introduce un año: "))
except ValueError:
    print("Error: Debes introducir un año.")
    exit()

if año % 4 == 0 and año % 100 == 0 and año % 400 == 0:
    print(f"{año} es un año bisiesto.")
elif año % 4 == 0 and año % 100 != 0:
    print(f"{año} es un año bisiesto.")
else:
    print(f"{año} no es un año bisiesto.")
