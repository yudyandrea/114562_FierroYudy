# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 11:47:35 2019

@author: Yudy Andrea Fierro
"""

#EJERCICIO 10

cadena = input('Ingrese la cadena de texto. ')


lista_mins = ['a','á','b','c','d','e','é','f','g','h','i','í','j','k','m','n',
              'l','ñ','o','ó','p','q','r','s','t','u','ú','ü','v','w','x',
              'y','z']
lista_MAYS = ['A','Á','B','C','D','E','É','F','G','H','I','Í','J','K','M','N',
              'L','Ñ','O','Ó','P','Q','R','S','T','U','Ú','Ü','V','W','X',
              'Y','Z']

for i in range(len(cadena)):
    if cadena[i] in lista_mins:
        pos_min = lista_mins.index(cadena[i])
        print(lista_MAYS[pos_min], end='')
    else:
        print(cadena[i],end='')
