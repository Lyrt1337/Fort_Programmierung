import numpy as np

A = np.array([[1,3,-1],[4,-2,8]])
B = np.array([[-3,9,3],[-6,6,3]])

C = [A+B, -2*A, B/3, 2*B-A]

for i in range(0,4):
    L = C[i]
    print(L)