# Autofahrt mit externen Daten
import IPython.display as dp
import matplotlib.pyplot as pl;
import sympy as sp
import numpy as np

pl.close('all');
pl.rcParams['figure.figsize']=(7.03,8);
pl.rcParams['font.size']=16;
pl.rcParams['font.family']='serif';
pl.rcParams['text.usetex']=True;
sp.init_printing()

# Parameter
t_0 = 0
Dt = 10
fac_v = 3.6
sc_t = 1/60
sc_s = 1.0e-3
lw = 3
fig = 1
pr = 3

# Daten
v_data = np.loadtxt("Daten.txt")
N = len(v_data)
t_E = t_0 +(N-1)*Dt
t_data = np.linspace(t_0, t_E, N)

# Berechnungen
Ds = np.trapz(v_data/fac_v, t_data)


# Ausgabe
print(f"Ergebnis: Ds = {Ds*sc_s:#.{pr}} km")

# Plot
# note: pl.axis("tight") works just as fine as pl.ylim and pl.xlim
fh =pl.figure(fig)
pl.plot(t_data*sc_t, v_data, linewidth = lw)
pl.xlabel(r"t[min]")
pl.ylabel(r"v[km/h]")
pl.axis("tight")
# pl.xlim(0, 20)
# pl.ylim(0, 125)
pl.grid("on")
pl.show()
    