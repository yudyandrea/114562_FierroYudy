# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 11:46:06 2019

@author: Yudy Andrea Fierro
"""

#EJERCICIO 9

x_1 = int(input('Ingrese el valor de X del primer círculo. '))
y_1 = int(input('Ingrese el valor de Y del primer círculo. '))
r_1 = int(input('Ingrese el valor del radio del primer círculo. '))
x_2 = int(input('Ingrese el valor de X del segundo círculo. '))
y_2 = int(input('Ingrese el valor de Y del segundo círculo. '))
r_2 = int(input('Ingrese el valor del radio del segundo círculo. '))
a_1 = int(input('Ingrese la coordenada X del punto a saber. '))
b_1 = int(input('Ingrese la coordenada Y del punto a saber. '))

def contenido_circulo(a,b,c):
    d = ((a_1-a)**2+(b_1-b)**2)**(1/2)
    if d <= c:
        return True
    else:
        return False

contenido_1 = contenido_circulo(x_1,y_1,r_1)
contenido_2 = contenido_circulo(x_2,y_2,r_2)

if contenido_1:
    print('El punto SI se encuentra contenido en el primer círculo.')
else:
    print('El punto NO se encuentra contenido en el primer círculo.')
if contenido_2:
    print('El punto SI se encuentra contenido en el segundo círculo.')
else:
    print('El punto NO se encuentra contenido en el segundo círculo.')
if contenido_1 and contenido_2:
    print('El punto se encuentra CONTENIDO en ambos círculos (intersección).')
else:
    print('El punto NO se encuentra CONTENIDO en la intersección de los 2 círculos.')
if not contenido_1 and not contenido_2:
    print('El punto NO se encuentra CONTENIDO en ninguno de los 2 círculos.')
else:
    print('El punto se encuentra CONTENIDO en alguno de los 2 círculos.')