import numpy as np

A = np.array([[2,0],[0,3]])
B = np.array([[1,1],[2,2]])
C = np.array([[0,6],[2,0]])
D = np.array([[0,-6],[2,0]])
E = np.array([[1,0,0],[2,2,-1],[0,-3,0]])
F = np.array([[0,1,0],[0,0,1],[1,0,0]])

[S,E] = np.linalg.eig(A)

print(f"S = {S}")
print(f"E = \n{E}")