# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 11:48:18 2019

@author: Yudy Andrea Fierro
"""

#EJERCICIO 11

import keyword
cadena = input('Ingrese la cadena de texto. ')

vocal_MAYUS = ['A','E','I','O','U','Á','É','Í','Ó','Ú','Ü']
vocal_mins_MAYUS_tilds = ['á','é','í','ó','ú','ü','Á','É','Í','Ó','Ú','Ü']

cont_vocal_MAYUS = 0
cont_mins_MAYUS_tilds = 0
cont_dig = 0
cont_esp = 0
cont_reserv = 0

for i in range(len(cadena)):
    if cadena[i] in vocal_MAYUS:
        cont_vocal_MAYUS += 1
    elif cadena[i] in vocal_mins_MAYUS_tilds:
        cont_mins_MAYUS_tilds += 1
    elif cadena[i].isdigit():
        cont_dig += 1
    elif cadena[i] == ' ':
        cont_esp += 1

cadena_copia = cadena.split(' ')

for j in cadena_copia:
    if j in keyword.kwlist:
        cont_reserv += 1

print('Cantidad de vocales MAYÚSCULAS: ', cont_vocal_MAYUS)
print('Cantidad de letras con tilde minúsculas y MAYÚSCULAS: ', cont_mins_MAYUS_tilds)
print('Cantidad de dígitos es: ', cont_dig)
print('Cantidad de espacios es: ', cont_esp)
print('Cantidad de palabras reservadas es: ', cont_reserv)