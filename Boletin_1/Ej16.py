#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Programa que solicita al usuario su nombre y apellidos por separado, 
# y muestra el siguiente mensaje por pantalla: 
# "El usuario Apellido1 Apellido2, Nombre se ha registrado correctamente". 
# NOTA: los dos apellidos se pueden pedir juntos; lo que se debe pedir por separado 
# es el nombre por un lado y los apellidos por otro.

__author__ = "Gabriel Gonzalez Kowalska"


nombre = input("Introduce tu nombre: ")

apellido1 = input("Introduce tu primer apellido: ")

apellido2 = input("Introduce tu segundo apellido: ")

print(f"El usuario {apellido1} {apellido2}, {nombre} se ha registrado correctamente")