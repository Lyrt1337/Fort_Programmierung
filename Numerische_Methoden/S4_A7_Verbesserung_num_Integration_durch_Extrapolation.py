# Python initialisieren :
import numpy as np
# Parameter :
pr = 16
# Daten :
h_data = np.array([3.110487775831478e-2, 1.555243887915739e-2,
                   7.776219439578696e-3, 3.888109719789348e-3])
I_data = np.array([1.999835503887443, 1.999959284652254,
                   1.999989871646689, 1.999997474185016])


# Extrapolation gem. Neville-Aitken-Schema an der Stelle Null
# Funktion
def NeAiNu(x_data, y_data):
    n = np.size(y_data)
    TAB = np.block([[y_data], [np.zeros((n - 1, n))]])
    for i in range(1, n):
        for j in range(i, n):
            TAB[i][j] = ((x_data[j]) * TAB[i - 1][j - 1]
                         - (x_data[j - i]) * TAB[i - 1][j])\
                        / (x_data[j] - x_data[j - i])
    return TAB[n - 1][n - 1]


# Berechnungen :
I = NeAiNu(h_data, I_data)
# Ausgabe :
print("--------------------------------------------------")
print(__file__)
print("--------------------------------------------------")
print (f"I = {I:#.{pr}g}")
print("--------------------------------------------------")