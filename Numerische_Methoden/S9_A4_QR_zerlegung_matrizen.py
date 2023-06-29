# Python initialisieren :
import numpy as np
import scipy as cp
import scipy.linalg
# Parameter :
A = np.array([[3, 1], [6, 9]])
pr = 3
# Berechnungen :
[Q, R] = cp.linalg.qr(A)
# Ausgabe :
with np.printoptions(precision=pr):
    print(f"Q = \n{Q}\n\nR = \n{R}")
