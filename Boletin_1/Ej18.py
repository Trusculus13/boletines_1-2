#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Programa que solicita al usuario 3 números y le muestra por pantalla la media de los 3 números.

__author__ = "Gabriel Gonzalez Kowalska"

num1 = float(input("Introduce el primer número: "))

num2 = float(input("Introduce el segundo número: "))

num3 = float(input("Introduce el tercer número: "))

media = (num1 + num2 + num3) / 3

media = round(media, 2)

print(f"La media de los números {num1}, {num2} y {num3} es: {media}")