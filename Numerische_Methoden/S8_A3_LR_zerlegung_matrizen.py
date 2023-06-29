# Python initialisieren :
import numpy as np
import scipy as cp
import scipy . linalg
# Parameter :
A = np.array([[3, 1], [6, 9]])
pr = 3
# Berechnungen :
[P, L, R] = cp.linalg.lu(A)
# Ausgabe :
with np.printoptions(precision=pr):
    print(f"P = \n{P}\n\nL = \n{L}\n\nR = \n{R}")