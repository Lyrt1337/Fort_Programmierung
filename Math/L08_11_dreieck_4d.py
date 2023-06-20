import numpy as np

pr = 3
A = np.array([[1],[-2],[0],[-2]])
B = np.array([[3],[1],[6],[-2]])
C = np.array([[2],[-5],[3],[10]])

a = C-B
b = A-C
c = B-A

def mu(X):
    V=np.sqrt(np.linalg.det(X.T@X))
    return V

l_c = mu(c)
A_d = 0.5*mu(np.block([a,b]))
S_d = (A+B+C)/3

print(f"Länge c= {l_c:#.{pr}g}")
print(f"Fläche= {A_d:#.{pr}g}")
print(f"Schwerpunkt S= {S_d.T}")