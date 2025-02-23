#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Programa que solicita al usuario el número de kilómetros recorridos en su último 
# viaje en coche, el consumo del coche en litros cada 100 kilómetros y el precio en 
# euros de un litro de combustible. Calcula el costo del viaje y lo muestra al usuario por pantalla.

__author__ = "Gabriel Gonzalez Kowalska"

num_kilometros = float(input("Introduce el número de kilómetros recorridos en tu último viaje: "))

consumo = float(input("Introduce el consumo del coche en litros cada 100 kilómetros: "))

consumo = consumo / 100

precio_litro = float(input("Introduce el precio en euros de un litro de combustible: "))

costo_viaje = num_kilometros * consumo * precio_litro

print(f"El costo del viaje es: {costo_viaje}")