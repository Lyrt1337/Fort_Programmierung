# Python initialisieren :
import numpy as np;
# Parameter :
A=np.array ([[2,0],[0,3]]);
# Berechnungen :
[S,E]= np.linalg.eig(A);
# Ausgabe :
print (f"S = {S}");
print (f"E = \n{E}");

# Python initialisieren :
import IPython . display as dp;
import sympy as sp;
# Python konfigurieren :
sp. init_printing ();
# Parameter :
A=sp. Matrix ([[2 ,0] ,[0 ,3]]);
# Berechnungen :
[E,D]=A. diagonalize ();
# Ausgabe :
dp. display (D);
dp. display (E);