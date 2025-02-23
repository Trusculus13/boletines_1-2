#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Pedir al usuario el radio de una esfera y calcular su volumen. 
# Mostrar el resultado por pantalla.

__author__ = "Gabriel Gonzalez Kowalska"

radio = float(input("Introduce el radio de la esfera: "))

pi = 3.141595

volumen = 4 / 3 * pi * radio ** 3

print(f"El volumen de la esfera es: {volumen}")