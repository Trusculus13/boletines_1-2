#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Calcula el importe a pagar por un vehículo al circular por una autopista. Selecciona
# el vehículo mediante un menú. Si es necesario, pídele al usuario los kilómetros
# recorridos por la autopista y su peso.
# ● Moto: importe fijo de 1€.
# ● Turismo: 0,25€ por kilómetro.
# ● Camión: 0,25€ por kilómetro más 0,15€ por tonelada de peso.

__author__ = "Gabriel Gonzalez Kowalska"

print("\t1. Moto")
print("\t2. Turismo")
print("\t3. Camión")
print("\tCualquier otro caracter para salir")
opcion = input("\t> ")

# Opcion 1: Moto
if opcion == "1":
    print("El importe a pagar es de 1€.")

# Opcion 2: Turismo
elif opcion == "2":
    try:
        km = float(input("Introduce los kilómetros recorridos: "))
    except ValueError:
        print("Error: Debes introducir valores numéricos.")
        exit()
    print(f"El importe a pagar es de {0.25 * km}€.")

# Opcion 3: Camión
elif opcion == "3":
    try:
        km = float(input("Introduce los kilómetros recorridos: "))
        peso = float(input("Introduce el peso del camión: "))
    except ValueError:
        print("Error: Debes introducir valores numéricos.")
        exit()
    print(f"El importe a pagar es de {0.25 * km + 0.15 * peso}€.")

else:
    print("Saliendo del menu.")
