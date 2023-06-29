# Python initialisieren :
import numpy as np;
# Parameter :
A=np.array ([[4 , -3 ,2] ,[6 ,2 ,5] ,[ -1 , -2 ,3]]);
B=np.array ([[3 ,4] ,[1 ,2] ,[5 ,6]]);
u=np.array ([[0] ,[2] ,[ -4]]);
v=np.array ([[1] ,[3] ,[ -3]]);
# Berechnungen :
C =A@B;
# Ausgabe :
print (f"C =\n{C}");


# Hilfe
# ValueError: mismatch in its core dimension = falsche Dimensionen
# die Operation ist "nicht Definiert"

# Berechnen
# A * B = A @ B
# A^T = A.T (Transponierte Matrix)

