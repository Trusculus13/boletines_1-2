#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Pedir al usuario su salario bruto e indicarle su salario neto. 
# Utiliza la siguiente fórmula para el cálculo: salario_neto = salario_bruto - (salario_bruto * IRPF).
# Solicítalo también al usuario el porcentaje de retención del IRPF que desea utilizar.
# Muestra el resultado por pantalla.

__author__ = "Gabriel Gonzalez Kowalska"

salario_bruto = float(input("Introduce tu salario mensual bruto: "))

IRPF = float(input("Introduce el porcentaje de retencion del IRPF: "))

salario_neto = salario_bruto - (salario_bruto * IRPF / 100)

print(f"Tu salario neto es: {salario_neto}")