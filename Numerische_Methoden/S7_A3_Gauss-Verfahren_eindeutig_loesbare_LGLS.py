# Python initialisieren :
import numpy as np
# Parameter :
A = np.array([[2, 3, 1], [1, -2, -1], [4, 1, -3]])
b = np.array([8, -3, 6])
pr = 3
# Funktionen :
def LGLS_Gauss(A, b):
    # Vorbereitungen :
    G = 1.0 * np.block([A, np.expand_dims(b, axis=1)])
    n = A.shape[0]
    # Stufenform :
    for ps in range(0, n - 1):
        mm = ps + np.argmax(np.abs(G[range(ps, n), ps]))
        if mm != ps:
            tmp = np.copy(G[ps])
            G[ps] = G[mm]
            G[mm] = tmp
        p = G[ps][ps]
        for zz in range(ps + 1, n):
            f = G[zz][ps] / p
            G[zz][ps] = 0.
            for ss in range(ps + 1, n + 1):
                G[zz][ss] = G[zz][ss] - f * G[ps][ss]
    # Rueckwaertseinsetzen :
    x = np. zeros(n)
    w = 0.
    for rr in range(n - 1, -1, -1):
        for ss in range(n - 1, rr, -1):
            w = x[ss]*G[rr][ss]
        x[rr] = (G[rr][-1] - w) / G[rr][rr]
    return x
# Berechnungen :
x= LGLS_Gauss (A,b)
# Ausgabe :
print(f"x = {np.array2string(x, precision=pr)}")
