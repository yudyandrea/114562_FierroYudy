# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 11:50:19 2019

@author: Yudy Andrea Fierro
"""

#EJERCICIO 14

cadena = input('Ingrese la cadena de texto').replace(' ','')

abecedario = ['a','á','A','Á','b','B','c','C','d','D','e','é','E','É','f','F',
              'g','G','h','H','i','í','I','Í','j','J','k','K','l','L','m','M',
              'n','N','ñ','Ñ','o','ó','O','Ó','p','P','q','Q','r','R','s','S',
              't','T','u','ú','ü','U','Ú','Ü','v','V','w','W','x','X','y','Y',
              'z','Z']

cadena_ordenada = ''

for i in abecedario:
    for j in cadena:
        if i == j:
            cadena_ordenada += j

print('La cadena ordenada alfabéticamente y contando todas las veces que '
      'se pueda repetir una palabra es:\n', cadena_ordenada)