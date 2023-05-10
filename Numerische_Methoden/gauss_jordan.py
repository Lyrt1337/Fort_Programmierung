# Python initialisieren
import IPython.display as dp
import sympy as sp
# Parameter
G = sp.Matrix([[2, 1, 0, 2, 6], [4, 2, 3, 3, 16], [-2, -1, 6, -4 , 2]
,[-8, -4, 9, -11, -12], [2, 1, -3, 3, 2]])
# Berechnungen
H = G.rref()
# Ausgabe
dp.display(G, H[0])
