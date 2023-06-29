# Python initialisieren :
import numpy as np;
# Parameter :
A=np.array([[2,3],[4,5]]);
prec =3;
# Berechnungen :
s=np.trace (A);
d=np.linalg det(A);
# Ausgabe :
print (f"s = {s} und d = {d}");
# print (f"s = {s :#.{ prec }} und d = {d :#.{ prec }}");