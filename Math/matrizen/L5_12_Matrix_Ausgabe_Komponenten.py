import numpy as np;

M=np. array ([[1 ,2 ,3 ,4 ,5 ,6] ,
              [7 ,8 ,9 ,10 ,11 ,12] ,
              [13 ,14 ,15 ,16 ,17 ,18] ,
              [19 ,20 ,21 ,22 ,23 ,24]]);

A=M[2,3] # Komponente M_34
print(A)

B=M[1,:] # 2. Zeile
print(B)

C=M[:,2] # 3. Spalte
print(C)

D=M[:,-1] # Letzte Spalte
print(D)

E=M[[0,-1],:] # 1. und letzte Spalte
print(E)

F=M[:,1::2] # Gerade Komponenten
print(F)