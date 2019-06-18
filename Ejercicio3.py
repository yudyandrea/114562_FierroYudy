# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 19:54:32 2019

@author: Yudy Andrea Fierro
"""
#Ejercicio 3

num = int(input('Ingrese un número entero de 3 digitos: '))

'''Se verifica que el número sea positivo para proceder a la operación'''

if num<0:
    num = num*-1

ud1 = 8

ud2 = (num-((num//10)*10))

ud3 = (num//10)

ud4 = (ud3-((ud3//10)*10))

ud5 = (ud3//10)

'''Se realiza la comparación digito al digito del termino para determinar si 
contiene el número 8'''

if ud2 == ud1:
    print('El número contiene el digito 8')
    
elif ud4 == ud1:
    print ('El número contiene el digito 8')
    
elif ud5 == ud1:
    print('El número contiene el digito 8')
    
else:
    print('El número no contiene el digito 8')