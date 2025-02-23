#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Crea un programa que realice el cambio de divisas tanto de euros a libras como de
# libras a euros. Crea un menú para que el usuario elija el cambio que desea realizar.

__author__ = "Gabriel Gonzalez Kowalska"

try:
    cantidad = float(input("Introduce la cantidad de dinero: "))
except ValueError:
    print("Error: Debes introducir valores numéricos.")
    exit()

print("\t1. Cambiar de euros a libras.")
print("\t2. Cambiar de libras a euros.")
opcion = input("\t> ")

#De euros a libras
if opcion == "1":
    print(f"{cantidad} euros son {cantidad * 0.85} libras.")

#De libras a euros
elif opcion == "2":
    print(f"{cantidad} libras son {cantidad / 0.85} euros.")

else:
    print("Saliendo del menú.")
