import sympy as sp
import IPython.display as dp
sp.init_printing()


A = sp.Matrix([[2,0],[0,3]])
B = sp.Matrix([[1,1],[2,2]])
C = sp.Matrix([[0,6],[2,0]])
D = sp.Matrix([[0,-6],[2,0]])
E = sp.Matrix([[1,0,0],[2,2,-1],[0,-3,0]])
F = sp.Matrix([[0,1,0],[0,0,1],[1,0,0]])

[E,D] = B.diagonalize()

dp.display(D)
dp.display(E)