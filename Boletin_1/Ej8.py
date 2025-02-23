#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Pedir al usuario base y altura de un triángulo y calcular su área. Mostrar el resultado por pantalla.

__author__ = "Gabriel Gonzalez Kowalska"

base = float(input("Introduce la base del triangulo: "))

altura = float(input("Introduce la altura del triangulo: "))

area = (base * altura) / 2

print(f"El area del triangulo es: {area}")