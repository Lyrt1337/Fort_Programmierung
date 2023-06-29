# Python initialisieren :
import numpy as np
# Parameter :
G = np.array([[2, 1, 0, 2, 6], [4, 2, 3, 3, 16], [-2, -1, 6, -4, 2],
              [-8, -4, 9, -11, -12], [2, 1, -3, 3, 2]])
pr = 3
# Funktionen :


def LGLS_rref (G, tol=-1):
    # Berechnungen :
    n_Z = G.shape[0]
    n_S = G.shape[1]
    if tol < 0:
        tol = np.max(G.shape) * np.linalg.norm(G, ord=np.inf)\
            * np.finfo(np. float64).eps
    # Stufenform berechnen :
    pz = np.int_([])
    ps = np.int_([])
    ez = 0
    n_R = 0
    m_Z = n_Z - 1
    H = np.copy(1.0 * G)
    for es in range(0, n_S):
        # Spalten -Pivot - Suche :
        if ez < m_Z:
            mm = ez + np.argmax(np.abs(H[range(ez, n_Z), es]))
        else:
            mm = m_Z
        if np.abs(H[mm][es]) > tol:
            if mm != ez:
                tmp = np.copy(H[ez])
                H[ez] = H[mm]
                H[mm] = tmp
            # Division durch Pivot - Wert :
            p = H[ez][es]
            H[ez][es] = 1.0
            for jj in range(es + 1, n_S):
                H[ez][jj] = H[ez][jj] / p
            # Elimination vorwaerts :
            for ii in range(ez + 1, n_Z):
                q = H[ii][es]
                H[ii][es] = 0.0
                for jj in range(es + 1, n_S):
                    H[ii][jj] = H[ii][jj] - q * H[ez][jj]
            n_R = n_R + 1
            pz = np.append(pz, ez)
            ps = np.append(ps, es)
            if ez == m_Z:
                break
            ez = ez + 1
        else:
            for ii in range(ez, n_Z):
                H[ii][es] = 0.0
    # Stufenform reduzieren :
    for kk in range(n_R - 1, -1, -1):
        ez = pz[kk]
        es = ps[kk]
        # Elimination rueckwaerts :
        for ii in range(ez - 1, -1, -1):
            q = H[ii][es]
            H[ii][es] = 0.0
            for jj in range(es + 1, n_S):
                H[ii][jj] = H[ii][jj]-q*H[ez][jj]
    return H


# Berechnungen :
H = LGLS_rref(G)
# Ausgabe :
print(f"H = \n{np.array2string(H, precision =pr)}")
