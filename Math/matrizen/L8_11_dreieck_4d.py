# Python initialisieren :
import numpy as np;
# Parameter :
A=np. array ([[1] ,[ -2] ,[0] ,[ -2]]);
B=np. array ([[3] ,[1] ,[6] ,[ -2]]);
C=np. array ([[2] ,[ -5] ,[3] ,[10]]);
prec =3;
# Funktionen :
def mu(X): V=np. sqrt (np. linalg .det(X.T@X )); return V;
# Berechnungen :
a=C-B; b=A-C; c=B-A; # Seitenvektoren
l_c=mu(c); # Seitenlaenge c
F =0.5* mu(np. block ([a,b ])); # Flaeche
S=(A+B+C )/3; # Schwerpunkt
# Ausgabe :
print (" --------------------------------------------------");
print ( __file__ );
print (" --------------------------------------------------");
print (f"a) Seitenlaenge : c = {l_c :#.{ prec }}");
print (f"b) Flaeche : F = {F :#.{ prec }}");
print (f"c) Schwerpunkt : S = {S.T}");
print (" --------------------------------------------------");