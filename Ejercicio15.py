# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 11:50:50 2019

@author: Yudy Andrea Fierro
"""

#EJERCICIO 15

lista_nums = eval(input('Porfavor ingrese la lista de números entre '
                        'corchetes ([]) y separado por comas (,) ->'))

condicion_int = False
lista_repetidos = []
for j in lista_nums:
    if lista_nums.count(j) == 2:
        if j not in lista_repetidos:
            lista_repetidos.append(j)
            print('El número ',j,'está repetido exactamente 2 veces.')

if len(lista_repetidos) == 0:
    print('No se encontró almenos 1 número que esté repetido exactamente 2 veces')