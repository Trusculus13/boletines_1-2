#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Realiza un programa que calcule el salario de un trabajador. El programa recibirá las
# horas trabajadas al día y los €/hora de ese trabajo. A continuación, pregunta al
# usuario si la tarifa es en bruto o en neto. Los días laborables al mes son 22. Si el
# usuario indica que el costo de la hora es en bruto, indícale al usuario que introduzca
# el IRPF para poder calcular el salario neto.

__author__ = "Gabriel Gonzalez Kowalska"

try:
    horas_dia = float(input("Introduce las horas trabajadas al día: "))
    tarifa = float(input("Introduce el coste por hora: "))
except ValueError:
    print("Error: Debes introducir valores numéricos.")
    exit()

while True:
    bruto_neto = input("La tarifa es en bruto o en neto? (b/n): ")
    if bruto_neto == "b":
        irpf = float(input("Introduce el IRPF: "))
        break
    elif bruto_neto == "n":
        break
    else:
        print("Error: Debes introducir 'b' o 'n'.")

salario_bruto = horas_dia * tarifa * 22
if bruto_neto == "b":
    salario_neto = salario_bruto - salario_bruto * irpf / 100
    print("El salario neto es de:", salario_neto)
else:
    print("El salario bruto es de:", salario_bruto)
