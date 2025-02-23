#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Crea un menú para seleccionar la acción que desea realizar el usuario. En este 
# caso, tenemos tres opciones:
# ● Sumar 2 números introducidos por teclado.
# ● Restar 2 números introducidos por teclado.
# ● Multiplicar 2 números introducidos por teclado. 
# Realiza la operación que seleccione el usuario.

__author__ = "Gabriel Gonzalez Kowalska"

print("Elige una de las opciones:")
print("\t1) Sumar dos números")
print("\t2) Restar dos números")
print("\t3) Multiplicar dos números")
print("\tCualquier otro caracter para salir")
opcion = input("\t> ")

# Opcion 1: sumar
if opcion == "1":
    try:
        num1 = int(input("Introduce un número: "))
        num2 = int(input("Introduce otro número: "))
    except ValueError:
        print("Error: Debes introducir valores numéricos.")
        exit()
    print(f"La suma de los números es: {num1 + num2}")

# Opcion 2: restar
elif opcion == "2":
    try:
        num1 = int(input("Introduce un número: "))
        num2 = int(input("Introduce otro número: "))
    except ValueError:
        print("Error: Debes introducir valores numéricos.")
        exit()
    print(f"La resta de los números es: {num1 - num2}")

# Opcion 3: multiplicar
elif opcion == "3":
    try:
        num1 = int(input("Introduce un número: "))
        num2 = int(input("Introduce otro número: "))
    except ValueError:
        print("Error: Debes introducir valores numéricos.")
        exit()
    print(f"La multiplicación de los números es: {num1 * num2}")

else:
    print("Saliendo del menu.")
