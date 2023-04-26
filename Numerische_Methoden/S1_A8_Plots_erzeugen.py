# Python initialisieren :
import numpy as np
import matplotlib . pyplot as pl
# Python konfigurieren :
pl.close ("all")
pl.rcParams["figure.figsize"] = (7.03, 15)
pl.rcParams["font.size"] = 9
pl.rcParams["font.family"] = "serif"
pl.rcParams["text.usetex"] = True
# Parameter :
x_0 = 0
x_E = 4
N = 201
lw = 3
fig = 1
# Funktionen :


def f(x):
    y = 3/(1 + x)
    return y


def g(x):
    y = x/2
    return y


# Daten :
x_data = np.linspace(x_0, x_E, N)
f_data = f(x_data)
g_data = g(x_data)
# Plot :
fh = pl.figure(fig)
pl.plot(x_data, f_data, linewidth=lw, label=r"$f$")
pl.plot(x_data, g_data, "--", linewidth=lw, label=r"$g$")
pl.xlabel(r"$x$")
pl.ylabel(r"$y$")
pl.legend()
pl.grid(visible=True)
pl.axis("image")
pl.show()
