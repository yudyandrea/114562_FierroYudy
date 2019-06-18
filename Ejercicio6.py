# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 11:43:58 2019

@author: Yudy Andrea Fierro
"""

'''
Lee un número y determina si la suma de sus dígitos hace parte de la serie de
Fibonacci.
'''
#Ejercicio 6

a = int(input('Ingrese un número: '))

lista_num = []
lista_serie_fibo = [0,1]
sumatoria = 0

'''Se realiza el desglosamiento del número'''

if a >= 0:
    while a > 0:
        lista_num.append(a%10)
        a//=10

    for i in lista_num:
        sumatoria += i

    while lista_serie_fibo[-1] < sumatoria:
        aux_sig = lista_serie_fibo[-1] + lista_serie_fibo[-2]
        lista_serie_fibo.append(aux_sig)

    if sumatoria in lista_serie_fibo:
        print('La suma de los dígitos si es un número de Fibonacci y es: ', sumatoria)
    else:
        print('La suma de los dígitos no es un número de la serie de Fibonacci.')
else:
    print('Los números negativos no hacen parte de la serie de Fibonacci')