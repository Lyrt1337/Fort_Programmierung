import numpy as np

# Parameter
x_0 = 0.5
Tol = 1.e-8
N = 100
pr = 7


# Funktionen
def f(x):
    # y = 1 - 1/5 * x
    # y = np.cos(x)
    y = np.exp(-x)
    return y


# Berechnungen
w = x_0 + 2. * Tol
x = x_0
k = 0
print(w)
print("--------------------------------------")
print(__file__)
print("--------------------------------------")
print("Fixpunkt-Iteration")
print(f"x_{k} = {x:#.16g}")

while (np.abs(x-w) > Tol) & (k < N):
    w = x
    k += 1
    x = f(x)
    # print("w: ", w)
    # print("x: ", x)
    print(f"x_{k} = {x:#.16g}")
    # print("(x-w): ", np.abs(x - w))

# Ausgabe
print("--------------------------------------")
print(f" Fixpunkt:       x = {x:#.{pr}g}")
print(f" Test:        f(x) = {f(x):#.{pr}g}")
print("--------------------------------------")
