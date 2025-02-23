#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Pedir al usuario el radio y la altura de un cilindro y calcular su volumen. 
# Mostrar el resultado por pantalla.

__author__ = "Gabriel Gonzalez Kowalska"

radio = float(input("Introduce el radio del cilindro: "))

altura = float(input("Introduce la altura del cilindro: "))

pi = 3.141595

volumen = pi * radio ** 2 * altura

print(f"El volumen del cilindro es: {volumen}")