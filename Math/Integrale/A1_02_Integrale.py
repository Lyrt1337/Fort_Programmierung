import IPython.display as dp
import matplotlib.pyplot as pl;
import sympy as sp
import numpy as np

pl.close("all")
sp.init_printing()

x_0 = 0
x_E = np.pi
n = 6
N = 5
lw = 3
fig = 1
pr = 3

# Funktion
def f(x): 
    y= np.sin(x)
    return y


for i in range(0,n):
    x_data = np.linspace(x_0, x_E, N)
    y_data = f(x_data)
    I = np.trapz(y_data, x_data)
    print(f"I = ", I, "| N =", N)
    N = 3*N

# Ausgabe
print(f"Ergebnis: I= {I:#.{pr}}")

# Plot
fh =pl.figure(fig)
pl.plot(x_data, y_data, linewidth = lw)
pl.xlabel(r"$x$")
pl.ylabel(r"$y$")
pl.axis("image")
pl.grid("on")
pl.show()
    



