#!/usr/bin/env python3
##############################################################################
#
#                        Program name: integral_sp.py
#                        Created:      Dec 25, 2025 11:03
#                        Modified:     Dec 25, 2025 19:15
#                        author:       Stephen Flowers Chávez
#
##############################################################################
import math
import os

# clear screen
os.system('cls')
print("***************************************************************")
print("*                                                             *")
print("*              Programa de suma trapezoidal                   *")
print("*              para antena de media onda                      *")
print("*                                                             *")
print("*                                  |   ^                      *")
print("*                                  |   |                      *")
print("*                                  |   |                      *")
print("* senal sinusoidal -->             |   |                      *")
print("*                ==================    | lambda/2             *")
print("*                                  |   |                      *")
print("*                                  |   |                      *")
print("*                                  |   |                      *")
print("*                                  |   v                      *")
print("*                                                             *")
print("***************************************************************")
print("\n")
print("Escriba su integral definitiva de la siguiente manera")
print("1.- Modifique el codigo fuente para definir su funcion f(x)")
print("\n")
print("2.- Escriba el limite de integracion superior cuando se le pida")
print("\n")
print("3.- Escriba el limite de integracion inferior cuando se le pida")
print("\n")

#valores iniciales
upper_limit=float(input('Valor de frontera superior para la integracion? (e.g. 3.14159 for pi) '))
lower_limit=float(input('Valor de frontera inferior para la integracion? (e.g. 0.00001 for zero) '))
n=int(input('numero de subintervalos? (e.g. 10 or 1000 or 1000000) '))

#initializando variable
integration=0

#simplificando constantes y operadores
pi=math.pi
cos=math.cos
sin=math.sin
tan=math.tan

# f(x)=((cos((kl/2)*cos(x)) - cos(kl/2))**2)/sin(x)
# para el caso de dipolo de media onda kl/2 = pi/2
# deje pi/2 en las ecuaciones por posible futura modificacion
# para trabajar con antenas mas generales que de media onda

#evaluando la funcion en fronteras superior e inferior
f_lower_limit=((cos((pi/2)*cos(lower_limit)) - cos(pi/2))**2)/sin(lower_limit)
f_upper_limit=((cos((pi/2)*cos(upper_limit)) - cos(pi/2))**2)/sin(upper_limit)

#regla de integracion trapezoidal
step_size=(upper_limit-lower_limit)/n
integration_value=f_lower_limit +f_upper_limit

for i in range(1,n,1):
	k=lower_limit + i*step_size
	f_k=((cos((pi/2)*cos(k)) - cos(pi/2))**2)/sin(k)
	integration = integration + 2*f_k
	#print(k, f_k, integration,f_upper_limit,f_lower_limit) # used for debugging
	
	
integration = (integration + f_lower_limit + f_upper_limit) *step_size/2
print("El valor de la integral definitiva es: ", integration)
