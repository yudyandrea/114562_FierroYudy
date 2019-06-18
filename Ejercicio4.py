# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 19:55:27 2019

@author: Yudy Andrea Fierro
"""
#Ejercicio 4

list_b = []

sum_pos = 0

b = int(input('Ingrese un número entero positivo: '))

'''Desgloso el número digito a digito y lo almaceno en una lista''' 
while b > 0:
    list_b.append(b%10)
    b//=10

'''Se verifica que el digito sea par y se hace la respectiva sumatoria'''
for i in list_b :
    if i%2 == 0:
        sum_pos += i
        
if sum_pos == 0:
    print('No hay números pares')
    
else:
    print('La suma de los números pares es: ',sum_pos)