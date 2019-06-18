# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 11:49:38 2019

@author: Yudy Andrea Fierro
"""

#EJERCICIO 13

cadena_1 = input('Ingrese la cadena de texto. ').replace(' ','')

long_linea = 1
lims = [0,1]
cant_impre = 1
ancho = 0
lista_impresiones = []
while lims[1] < len(cadena_1):
    lista_impresiones.append(cadena_1[lims[0]:lims[1]])
    long_linea += 2
    lims = [lims[1],lims[1]+long_linea]
    cant_impre += 1
    if ancho < lims[1]- lims[0]:
        ancho = lims[1]-lims[0]

lista_impresiones.append(cadena_1[lims[0]:])

for i in range(len(lista_impresiones)):
    print('{0: ^45}'.format(lista_impresiones[i]))