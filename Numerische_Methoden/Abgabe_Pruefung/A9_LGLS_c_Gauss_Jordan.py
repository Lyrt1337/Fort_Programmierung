"""
-------------------------
Numerik Prüfung A9 LGLS c) Gauss-Jordan
Autor: Christian Gilomen
Datum: 30.06.2023
-------------------------
"""
# Python initialisieren
import IPython.display as dp
import sympy as sp
# Parameter

G = sp.Matrix([[1., 0.2, 0.1, 0., 0., 6.85],
               [0.2, 2., 0.2, 0.1, 0., 16.78],
               [0.1, 0.2, 0.3, 0.2, 0.1, 29.10],
               [0., 0.1, 0.2, 4.0, 0.2, -9.88],
               [0., 0., 0.1, 0.2, 5., 29.73]])
# Berechnungen
H = G.rref()
# Ausgabe
# dp.display(G, H[0])
# for i in H[0]:
#     print(H[:i])


dp.display(H[0])
