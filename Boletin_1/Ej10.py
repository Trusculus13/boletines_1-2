#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Realiza una calculadora que reciba una cantidad de Libras y realice el cambio de divisas a euros. 
# Vamos a suponer que el cambio de libra a euros está en 1 libra = 1.10 euros. 
# Muestra el resultado por pantalla.

__author__ = "Gabriel Gonzalez Kowalska"

libras = float(input("Introduce la cantidad de libras: "))

cambio = 1.10

euros = libras * cambio

print(f"{libras} libras son {euros} euros")