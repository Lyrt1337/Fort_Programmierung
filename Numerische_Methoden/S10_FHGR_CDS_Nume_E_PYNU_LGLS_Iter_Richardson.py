# Python initialisieren
import numpy as np
# Parameter
A = np.array([[3., 1., 1.], [1., 3., 1.], [1., 1., 3.]])
b = np.array([8., 10., 12.])
s = 0.22
N = 100
pr_x = 3
pr_y = 2
pr_t = 16
n = np.shape(b)[0]
# Vorbereitung
H = s * np.eye(n)
M = np.eye(n) - H@A
y = np.linalg.norm(M)
q = H@b
x = b
w = 0.
k = 0


# Funktionen
def f(x):
    y = M@x+q
    return y


# Iteration
print(f"x_{k} = {x}")
while np.array_equal(x, w) == False and k < N:
    w = x
    k = k + 1
    x = f(x)
    print(f"x_{k} = {x}")
    print(f"x_{k} = {np.array2string(x, precision=pr_t)}")

# Ausgabe :
print("--------------------------------------------------")
print(f" Loesung : x = {np.array2string(x, precision=pr_x)}")
print(f" Norm : y = {y:#.{pr_y}g}")
print("--------------------------------------------------")