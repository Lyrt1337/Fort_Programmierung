# Python initialisieren :
import matplotlib.pyplot as pl;
import numpy as np;
# Parameter :
tau_0= 0; tau_E= 10*np.pi; N= 401; lw= 3; fig= 1;
# Funktionen:
def s(tau):
    x =2**(-tau/(2*np.pi))*np.cos(tau);
    y =2**(-tau/(2*np.pi))*np.sin(tau);
    return x,y;
# Daten :
tau_data=np.linspace(tau_0 ,tau_E ,N);
[x_data, y_data]=s(tau_data);
# Plot :
fh=pl.figure(fig);
pl.plot(x_data, y_data, linewidth=lw);
pl.xlabel(r"$x$"); pl.ylabel (r"$y$");
pl.grid("on"); pl.axis ("image");