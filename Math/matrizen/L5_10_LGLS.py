# Python initialisieren :
# LGLS lösen mit linalg.solve
import numpy as np;
# Parameter :
A=np.array ([[2 , -1] ,[ -3 ,2]]); b=np.array ([1 ,0]);
# Berechnungen :
L=np.linalg.solve (A,b);
C=np.linalg.cond (A);
# Ausgabe :
print (f"L = {L}");
print (f"C = {C :#.{3}} ");

# LGLS lösen mit linalg.inv
# Python initialisieren :
import numpy as np;
# Parameter :
A=np.array ([[2 , -1] ,[ -3 ,2]]); b=np.array ([[1] ,[0]]);
# Berechnungen :
Ai=np.linalg.inv(A);
u= Ai@b ;
# Ausgabe :
print (f"u =\n{u}");

