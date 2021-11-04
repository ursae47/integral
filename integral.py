#!/usr/bin/python
import math
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

upper_limit= input('upper boundary value?')
lower_limit= input('lower boundary value?')
n=input('number of subintervals?')
 
integration=0

pi=math.pi
cos=math.cos
sin=math.sin
tan=math.tan

# f(x)=((cos((kl/2)*cos(x)) - cos(kl/2))**2)/sin(x)
# for the case of a half wavelength dipole kl/2 = pi/2
# I've left pi/2 in the equations so they can be modified in the future
# to work for more general antennas and not just lambda/2

f_lower_limit=((cos((pi/2)*cos(lower_limit)) - cos(pi/2))**2)/sin(lower_limit)
f_upper_limit=((cos((pi/2)*cos(upper_limit)) - cos(pi/2))**2)/sin(upper_limit)

step_size=(upper_limit-lower_limit)/n
integration_value=f_lower_limit +f_upper_limit

for i in range(1,n,1):
	k=lower_limit + i*step_size
	f_k=((cos((pi/2)*cos(k)) - cos(pi/2))**2)/sin(k)
	integration = integration + 2*f_k
	print(k, f_k, integration,f_upper_limit,f_lower_limit) # used for debugging
	i=i+1
	
integration = (integration + f_lower_limit + f_upper_limit) *step_size/2
print(integration)

		
			
