# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 19:52:57 2019

@author: Yudy Andrea Fierro
"""
#Ejercicio 2

list_a = []

a = int(input('Escribir un número entero: '))

'''Se realiza el desglosamiento del número para poder imprimirlo posteriormente
al revés'''

while a > 0:
    list_a.append(a%10)
    a//=10

for i in list_a:
    print(i,end='')