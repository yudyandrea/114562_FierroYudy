# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 21:18:40 2019

@author: Yudy Andrea Fierro
"""
#Ejercicio 5

list_a = []
cant_cincos = 0
a = int(input('Ingrese un número entero: '))

'''Se realiza el desglosamiento del número para poder evaluar casa digito'''

while a > 0 :
    list_a.append(a%10)
    a//= 10 
    
''' Se agregan los valores a una lista y se verifican si son o no cincos'''

list_a.append(0)
for i in range(len(list_a)):
    if list_a[i] == 5:
        if list_a[i-1] != 5 and list_a[i+1] != 5:
            continue
        else:
            cant_cincos+=1
            
print('La cantidad de cincos consecutivos en el número es:',cant_cincos)