# Python initialisieren :
import numpy as np
# Parameter :
x_0 = -4
x_E = 4
n = 10
N = 201
pr = 6


# Funktionen :
def f(x):
    y = (np.cosh(2 * x) / (1 + x ** 4)) * np.exp(-x**2/2)
    return y


# Ausgabe :
print("--------------------------------------------------")
print(__file__)
print("--------------------------------------------------")
# Berechnungen :
for k in range (0, n):
    x_data = np.linspace(x_0, x_E, N)
    f_data = f(x_data)
    # Integration :
    I = np.trapz(f_data, x_data)
    print(f"I = {I:#.16g} | N = {N:g}")
    N = 2 * N
# Ausgabe :
print("--------------------------------------------------")
print (f"I = {I:#.{pr}g}")
print("--------------------------------------------------")