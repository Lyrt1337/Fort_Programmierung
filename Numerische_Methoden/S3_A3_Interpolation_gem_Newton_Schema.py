# Python initialisieren :
import matplotlib . pyplot as pl
import numpy as np
# Parameter :
x_data = np.array([4., 8.])
y_data = np.array([1., -1.])
x_0 = x_data[0]
x_E = x_data[-1]
N = 3
lw = 3
fig = 1
# Berechnungen :
n = np.size( y_data )
TAB = np. block([[y_data], [np.zeros((n - 1, n))]])
c_data = np. zeros(n)
c_data[0] = y_data[0]
for i in range(1, n):
    for j in range(i, n):
        TAB[i][j] = (TAB[i - 1][j]-TAB[i - 1][j - 1])/(x_data[j] - x_data[j-i])
    c_data[i] = TAB[i][i]
# Ausgabe :
print("--------------------------------------------------")
print(__file__)
print("--------------------------------------------------")
print(f"Daten Argumente : x = {x_data}")
print(f"Daten Funktionswerte : y = {y_data}")
print(f"Newton - Koeffizienten : c = {c_data}")
print("--------------------------------------------------")
# Funktionen :


def p(x):
    d = 1.
    y = c_data[0]
    for k in range(1, n):
        d = d * (x - x_data[k - 1])
        y = y + c_data[k] * d
        return y


# Daten :
u_data = np.linspace(x_0, x_E, N)
v_data = p(u_data)
# Plot :
fh = pl.figure(fig)
pl.plot(u_data, v_data, linewidth=lw)
pl.plot(x_data, y_data, "o", linewidth=lw)
pl.xlabel(r"$x$")
pl.ylabel(r"$y$")
pl.grid(visible=True)
pl.axis("image")
pl.show()
