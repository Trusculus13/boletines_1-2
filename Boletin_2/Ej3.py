#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Realiza un programa que lea un número y determine si está entre 10 y 100 (ambos inclusive). 
# Haz un control de excepciones si no se introducen valores numéricos.

__author__ = "Gabriel Gonzalez Kowalska"

try:
    num1 = int(input("Introduce un número: "))
except ValueError:
    print("Error: Debes introducir valores numéricos.")
    exit()

if num1 >= 10 and num1 <= 100:
    print("El número está entre 10 y 100")
else:
    print("El número no está entre 10 y 100")
