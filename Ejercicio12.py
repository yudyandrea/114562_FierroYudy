# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 11:48:53 2019

@author: Yudy Andrea Fierro
"""

#EJERCICIO 12

cadena_1 = input('Ingrese la primera cadena de texto. ')
cadena_2 = input('Ingrese la segunda cadena de texto. ')


abecedario = ['a','á','A','Á','b','B','c','C','d','D','e','é','E','É','f','F',
              'g','G','h','H','i','í','I','Í','j','J','k','K','l','L','m','M',
              'n','N','ñ','Ñ','o','ó','O','Ó','p','P','q','Q','r','R','s','S',
              't','T','u','ú','ü','U','Ú','Ü','v','V','w','W','x','X','y','Y',
              'z','Z']

if len(cadena_1)<=len(cadena_2):
    for i in range(len(cadena_1)):
        pos_1 = abecedario.index(cadena_1[i])
        pos_2 = abecedario.index(cadena_2[i])
        if pos_1 < pos_2:
            print('La palabra', cadena_1,'está antes que',cadena_2)
            break
        elif pos_1 > pos_2:
            print('La palabra', cadena_2, 'está antes que', cadena_1)
            break
        elif pos_1 == pos_2:
            continue
    else:
        print('La palabra', cadena_1,'está antes que',cadena_2)
else:
    for i in range(len(cadena_2)):
        pos_1 = abecedario.index(cadena_1[i])
        pos_2 = abecedario.index(cadena_2[i])
        if pos_1 > pos_2:
            print('La palabra', cadena_1,'está antes que',cadena_2)
            break
        elif pos_1 < pos_2:
            print('La palabra', cadena_2, 'está antes que', cadena_1)
            break
        elif pos_1 == pos_2:
            continue
    else:
        print('La palabra', cadena_2,'está antes que',cadena_1)