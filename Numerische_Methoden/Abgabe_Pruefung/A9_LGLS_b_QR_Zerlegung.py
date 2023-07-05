"""
-------------------------
Numerik Prüfung A9 LGLS b) QR- Zerlegung
Autor: Christian Gilomen
Datum: 30.06.2023
-------------------------
"""
# Python initialisieren :
import numpy as np
import scipy as cp
import scipy.linalg
# Parameter :
A = np.array([[1., 0.2, 0.1, 0., 0., 6.85],
              [0.2, 2., 0.2, 0.1, 0., 16.78],
              [0.1, 0.2, 0.3, 0.2, 0.1, 29.10],
              [0., 0.1, 0.2, 4.0, 0.2, -9.88],
              [0., 0., 0.1, 0.2, 5., 29.73]])
pr = 3
# Berechnungen :
[Q, R] = cp.linalg.qr(A)
# Ausgabe :
with np.printoptions(precision=pr):
    print(f"Q = \n{Q}\n\nR = \n{R}")
