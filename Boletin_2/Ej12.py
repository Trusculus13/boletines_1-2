#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Escribe un programa que solicite al usuario el nombre de usuario y la contraseña.
# Indica si el inicio de sesión es correcto. El nombre de usuario sería "python" y la
# contraseña "pip".

__author__ = "Gabriel Gonzalez Kowalska"

usuario = input("Introduce tu nombre de usuario: ")
contraseña = input("Introduce tu contraseña: ")

if usuario == "python" and contraseña == "pip":
    print("Inicio de sesión correcto.")
else:
    print("Inicio de sesión incorrecto.")
