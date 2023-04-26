# Python initialisieren :
import numpy as np

# Parameter :
x_0 = 0
x_E = 2
n = 5
N = 201
pr = 6


# Funktionen :
def f(x):
    y = np.sqrt(x + np.sin(x))
    return y


def NeAiNu(x_data, y_data):
    n = np.size(y_data)
    TAB = np.block([[y_data], [np.zeros((n - 1, n))]])
    for i in range(1, n):
        for j in range(i, n):
            TAB[i][j] = (x_data[j] * TAB[i - 1][j - 1]
                         - x_data[j - i] * TAB[i - 1][j]) \
                        / (x_data[j] - x_data[j - i])
    return TAB[n - 1][n - 1]


# Ausgabe :
print("--------------------------------------------------")
print(__file__)
print("--------------------------------------------------")
# Berechnungen :
h_data = np.zeros(n)
I_data = np.zeros(n)
for k in range(0, n):
    h = (x_E - x_0) / N
    x_data = np.linspace(x_0, x_E, N)
    f_data = f(x_data)
    # Integration :
    I = np.trapz(f_data, x_data)
    h_data[k] = h
    I_data[k] = I
    print(f"I = {I :#.16g} | N = {N:g}")
    N = 2 * N
I_raw = I_data[-1]
I_ext = NeAiNu(h_data, I_data)
# Ausgabe :
print("--------------------------------------------------")
print(f" I_raw = {I_raw :#.{pr}g}")
print(f" I_ext = {I_ext :#.{pr}g}")
print("--------------------------------------------------")
