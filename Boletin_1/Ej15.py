#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Programa que solicita al usuario los coeficientes de una ecuación de segundo grado
# y calcula las dos soluciones. Muestra las dos soluciones por pantalla.

__author__ = "Gabriel Gonzalez Kowalska"


a = float(input("Introduce el coeficiente a: "))

b = float(input("Introduce el coeficiente b: "))

c = float(input("Introduce el coeficiente c: "))

x1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)

x2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)

print(f"Las soluciones de la ecuación {a}x^2 + {b}x + {c} = 0 son: {x1} y {x2}")