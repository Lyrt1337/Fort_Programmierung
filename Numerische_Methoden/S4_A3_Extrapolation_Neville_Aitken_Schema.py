# Python initialisieren :
import numpy as np
# Parameter :
x = 3.
pr = 3
# Daten :
x_data = np.array([4., 8.])
y_data = np.array([1., -1.])
# Funktionen :


def NeAi(x, x_data, y_data):
    n = np.size(y_data)
    TAB = np.block([[y_data], [np.zeros((n - 1, n))]])
    for i in range(1, n):
        for j in range(i, n):
            TAB[i][j] = ((x - x_data[j-i]) * TAB[i - 1][j]
                         - (x - x_data[j]) * TAB[i - 1][j - 1])\
                        / (x_data[j] - x_data[j - i])
    return TAB[n - 1][n - 1]


# Berechnungen :
y = NeAi(x, x_data, y_data)

# Ausgabe :
print("--------------------------------------------------")
print(__file__)
print("--------------------------------------------------")
print(f"p({x:#.{pr}g}) = {y:#.{pr}g}")
print("--------------------------------------------------")



