# Python initialisieren :
import numpy as np


# Funktionen :
def TRAPZ(y_data, x_data):
    N = np.size(y_data)
    I = 0.
    for k in range (0, N - 1):
        I = I + (x_data[k+1] - x_data[k]) * (y_data[k + 1] + y_data[k])
    I = 0.5 * I
    return I


def TRAPZ(y_data, x_data):
    I = 0.5 * np.dot(np.diff(x_data), (y_data[1:] + y_data[0: -1]))
    return I
