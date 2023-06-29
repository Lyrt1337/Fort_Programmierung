import numpy as np

# LGLS mit Hilfe von linalg.solve

a = np.array([[2,-1],[-3,2]])
b = np.array([[1],[0]])

c = np.linalg.solve(a,b)
print(c)

# LGLS mit Hilve der inversen Matrix und linalg.inv

a_inv = np.linalg.inv(a)
L = a_inv @ b
print(L)