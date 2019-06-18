# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 19:51:37 2019

@author: Yudy Andrea Fierro
"""
#Ejercicio 1

'''Se realiza el ingreso del número y de ser negativo para tal motivo se multi
plica por -1 para obtener el valor absoluto'''

x = float(input('Ingrese un número: '))
if x<0:
    v_a = x*-1
    
else:
    v_a = x
    
print('El valor absoluto es: ',v_a)