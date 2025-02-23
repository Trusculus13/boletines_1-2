#!/usr/bin/env python
# -*- coding: utf-8 -*-

# La evaluación de este módulo es la siguiente: 15% tareas, 20% examen teórico y 
# 65% examen práctico. El programa le pedirá al usuario sus tres notas sobre 10 e 
# indicará por pantalla su nota final sobre 10.

__author__ = "Gabriel Gonzalez Kowalska"

nota1 = float(input("Introduce la nota de las tareas: "))
nota2 = float(input("Introduce la nota del examen teorico: "))
nota3 = float(input("Introduce la nota del examen practico: "))

nota_tarea = (nota1 * 15) / 100
nota_teorico = (nota2 * 20) / 100
nota_practico = (nota3 * 65) / 100

nota_final = nota_tarea + nota_teorico + nota_practico

print(f"La nota final de este modulo es: {nota_final}")