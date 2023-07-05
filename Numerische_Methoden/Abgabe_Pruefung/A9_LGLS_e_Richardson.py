"""
-------------------------
Numerik Prüfung A9 LGLS e) Richardson
Autor: Christian Gilomen
Datum: 30.06.2023
-------------------------
"""

# Python initialisieren
import numpy as np
# Parameter
A = np.array([[1., 0.2, 0.1, 0., 0.],
              [0.2, 2., 0.2, 0.1, 0.],
              [0.1, 0.2, 0.3, 0.2, 0.1],
              [0., 0.1, 0.2, 4.0, 0.2],
              [0., 0., 0.1, 0.2, 5.]])
b = np.array([6.85, 16.78, 29.10, -9.88, 29.73])
s = 0.37
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