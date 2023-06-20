import numpy as np;
import sympy as sp;
from fractions import Fraction
# Parameter
#v = a*x**2 + b*x + c

a = 4
b = 4
c = 1


# Berechnungen

# Diskriminante
D = b**2-4*a*c
Nenner = 2*a

print("Diskriminante D = ",D)

# x_a= -b/(2*a) + (np.sqrt(D))/(2*a)
# x_b= -b/(2*a) - np.sqrt(D)/(2*a)

if D > 0:
    x = "mehr als 1 Lösung";
    x_a=(-b - np.sqrt(D))/(2*a)
    x_b=(-b + np.sqrt(D))/(2*a)
    
if D == 0:
    x = -b/(2*a);
    x_a = "nur 1 Lösung";
    x_b = "nur 1 Lösung";
    
if D < 0:
    x = "mehr als 1 Lösung"
    x_a = -b/(2*a) - 1j*np.sqrt(abs(D))/(2*a)
    x_b = -b/(2*a) + 1j*np.sqrt(abs(D))/(2*a)
    
   
print("x = ",x)
print("x_1 = ", x_a)
print("x_2 = ", x_b)

print("L = ", Fraction(-b,(2*a))," +- ", u"\u221A",Fraction(D,2*a),"i")
