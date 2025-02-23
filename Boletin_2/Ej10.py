#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Programa que pide al usuario los coeficientes de una ecuación de segundo grado y
# calcula la solución. Comprueba si hay una solución, dos o ninguna. Dependiendo del
# caso, muestra las soluciones que correspondan.

__author__ = "Gabriel Gonzalez Kowalska"


try:
    a = float(input("Introduce el coeficiente a: "))
    b = float(input("Introduce el coeficiente b: "))
    c = float(input("Introduce el coeficiente c: "))
except ValueError:
    print("Error: Debes introducir valores numéricos.")
    exit()

if a == 0:
    print("Error: a no puede ser 0.")
    exit()

#calculamos el discriminante
discriminante = b**2 - 4*a*c

#si el discriminante es mayor que 0, la ecuación tiene dos soluciones
if discriminante > 0:
    x1 = (-b + discriminante**0.5) / (2*a)
    x2 = (-b - discriminante**0.5) / (2*a)
    print(f"Las soluciones {x1} y {x2}")

#si el discriminante es igual a 0, la ecuación tiene una solución
elif discriminante == 0:
    x = -b / (2*a)
    print(f"La solucion es x = {x}")

#si el discriminante es menor que 0, la ecuación no tiene soluciones
else:
    print("La ecuacion no tiene soluciones")
