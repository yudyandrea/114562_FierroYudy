# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 11:45:05 2019

@author: Yudy Andrea Fierro
"""

#EJERCICIO 7

a = int(input('Ingrese un número: '))

if a > 0:
    copia_a = a
    lista_num = []
    lista_repetidos = []
    while a > 0:
        lista_num.append(a%10)
        a//=10


    for i in lista_num:
        if i not in lista_repetidos:
            lista_repetidos.append(i)
            contador = 0
            for j in lista_num:
                if j == i:
                    if contador == 2:
                        print('El número', i, 'está repetido.')
                        break
else:
    print('No se puede con los números negativos, se pide ENTEROS POSITIVOS.')