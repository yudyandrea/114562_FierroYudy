# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 19:55:55 2019

@author: Yudy Andrea Fierro
"""
#EJERCICIO 8

mul_3 = []
mul_4 = []

'''Se verifica el residuo del número para saber si es multiplo de tres y si lo es
almacenarlo en una lista, igualmente para cuatro'''

for i in range(1,101):
    
    if i%3 == 0 :
        if len (mul_3) < 15:
            mul_3.append(i)
            
    if i%4 == 0 :
        if len(mul_3) == 15:
            mul_4.append(i)
            
print('Primeros 15 multiplos de 3 de los primeros 100 números enteros ' 
      'positivos:',mul_3, end = '\n\n')

print('Multiplos de 4 a partir de los primeros 15 multiplos de 3 en los '
      'primeros 100 números enteros positivos',mul_4)