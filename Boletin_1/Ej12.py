#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Calcula el valor del siguiente polinomio 2x^2 + 5x - 3 para el valor de x que especifique el usuario. 
# Muestra el resultado por pantalla.

__author__ = "Gabriel Gonzalez Kowalska"

x = float(input("Introduce el valor de x: "))

polinomio = 2 * x ** 2 + 5 * x - 3

print(f"El valor del polinomio 2x^2 + 5x - 3 para x = {x} es: {polinomio}")