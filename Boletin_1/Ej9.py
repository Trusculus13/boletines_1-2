#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Pedir al usuario el radio de una circunferencia y calcular su perímetro y área. Mostrar el resultado por pantalla.

__author__ = "Gabriel Gonzalez Kowalska"

radio = float(input("Introduce el radio de la circunferencia: "))

pi = 3.141595

perimetro = 2 * pi * radio

area = pi * radio ** 2

print(f"El perimetro de la circunferencia es: {perimetro}")

print(f"El area de la circunferencia es: {area}")