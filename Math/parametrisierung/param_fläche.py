# Python initialisieren :
import matplotlib.pyplot as pl;
from mpl_toolkits import mplot3d;
import numpy as np;
# Parameter :

R= 10; r=4
u_0=0 ; u_E=2*np.pi ; v_0=0 ; v_E=2*np.pi; N_u=51 ; N_v=101 ; fig= 1;
# Funktionen:
def P(u,v):
    x = (R+r*np.sin(u))*np.cos(v);
    y = (R+r*np.sin(u))*np.sin(v);
    z = r*np.cos(u);
    return x,y,z;
# Daten :
u_data=np.linspace(u_0 ,u_E ,N_u);
v_data=np.linspace(v_0, v_E, N_v);
[u_grid, v_grid]=np.meshgrid(u_data, v_data);
[x_grid, y_grid, z_grid]=P(u_grid, v_grid);
# Plot :
fh=pl.figure(fig);
ax=pl.axes(projection="3d");
ax.plot_surface(x_grid, y_grid, z_grid, cmap="viridis");
ax.set_xlabel(r"$x$");
ax.set_ylabel(r"$y$");
ax.set_zlabel(r"$z$");
