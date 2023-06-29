# Python initialisieren:
import matplotlib.pyplot as pl;
import scipy.integrate as ig;
import numpy as np;
# Python konfigurieren:
pl.close('all');
pl.rcParams['figure.figsize']=(7.03,10);
pl.rcParams['font.size']=16;
pl.rcParams['font.family']='serif';
pl.rcParams['text.usetex']=True;
# Parameter:
x_0=0; x_E=np.pi; n=6; N=10; lw=3; fig=1;
# Funktionen:
def f(x): y=np.sin(x); return y;
# Daten:
for k in range(0,n):
    x_data=np.linspace(x_0,x_E,N);
    f_data=f(x_data);
    # Berechnungen:
    I=np.trapz(f_data,x_data);
    J=ig.simps(f_data,x_data);
    # Ausgabe:
    print('I =',f"{I:.16}",'J =',f"{J:.16}");
    N=2*N;
# Ausgabe:
print('Integral I =',f"{I:.3}");
print('Integral J =',f"{J:.3}");
# Plot:
fh=pl.figure(fig);
pl.plot(x_data,f_data,linewidth=lw);
pl.xlabel(r'$x$'); pl.ylabel(r'$y$');
pl.grid('on'); pl.axis('image');
#

