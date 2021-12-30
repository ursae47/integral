#!/usr/bin/python
import math
import os

# clear screen
os.system('cls')
print("***************************************************************")
print("*                                                             *")
print("*              Trapezoidal summation program                  *")
print("*              for a half wavelength antenna                  *")
print("*                                                             *")
print("*                                  |   ^                      *")
print("*                                  |   |                      *")
print("*                                  |   |                      *")
print("* sinusoidal driving signal--->    |   |                      *")
print("*                ==================    | lambda/2             *")
print("*                                  |   |                      *")
print("*                                  |   |                      *")
print("*                                  |   |                      *")
print("*                                  |   v                      *")
print("*                                                             *")
print("***************************************************************")
print("\n")
print("Enter your definite integral as follows")
print("1.- Modify the source code to define your function f(x)")
print("\n")
print("2.- Enter the upper limit of integration when prompted")
print("\n")
print("3.- Enter the lower limit of integration when prompted")
print("\n")

#input values
upper_limit=float(input('Upper limit of integration value? (e.g. 3.14159 for pi) '))
lower_limit=float(input('Lower limit of integration value? (e.g. 0.00001 for zero) '))
n=int(input('number of subintervals? (e.g. 10 or 1000 or 1000000) '))

#initializing variable
integration=0

#simplifying constants & operators
pi=math.pi
cos=math.cos
sin=math.sin
tan=math.tan

# f(x)=((cos((kl/2)*cos(x)) - cos(kl/2))**2)/sin(x)
# for the case of a half wavelength dipole kl/2 = pi/2
# I've left pi/2 in the equations so they can be modified in the future
# to work for more general antennas and not just lambda/2

#evaluating the function at the upper & lower limits
f_lower_limit=((cos((pi/2)*cos(lower_limit)) - cos(pi/2))**2)/sin(lower_limit)
f_upper_limit=((cos((pi/2)*cos(upper_limit)) - cos(pi/2))**2)/sin(upper_limit)

#trapezoidal rule for integration
step_size=(upper_limit-lower_limit)/n
integration_value=f_lower_limit +f_upper_limit

for i in range(1,n,1):
	k=lower_limit + i*step_size
	f_k=((cos((pi/2)*cos(k)) - cos(pi/2))**2)/sin(k)
	integration = integration + 2*f_k
	#print(k, f_k, integration,f_upper_limit,f_lower_limit) # used for debugging
	
	
integration = (integration + f_lower_limit + f_upper_limit) *step_size/2
print("The definite integral's value is: ",integration)
