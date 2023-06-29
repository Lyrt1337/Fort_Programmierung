# Python initialisieren

import matplotlib.pyplot as pl;
from mpl_toolkits import mplot3d;
import numpy as np;

# Python konfigurieren: 
pl.close('all');
pl.rcParams['figure.figsize']=(7.03,10);
pl.rcParams['font.size']=16;
pl.rcParams['font.family']='serif';
pl.rcParams['text.usetex']=True;

# Parameter
x_0=-4; x_E=4; y_0=-4; y_E=4;
N_x=601; N_y=201; N_g=10; az=26-90; el=20; N_l=21; fig=1;

# Funktion
def f(x,y):
    z=x/2;
    return z;

# Daten
x_data=np.linspace(x_0, x_E, N_x);
y_data=np.linspace(y_0, y_E, N_y);
[x_grid, y_grid]=np.meshgrid(x_data, y_data);
z_grid=f(x_grid, y_grid);

# Graph-Plot
fh=pl.figure(fig); ax=pl.axes(projection='3d');
ax.plot_surface(x_grid, y_grid, z_grid, rstride=N_g, cstride=N_g, cmap='viridis');
ax.view_init(el,az);
ax.set_xlabel(r'$x$');
ax.set_ylabel(r'$y$');
ax.set_zlabel(r'$z$');
#ax.set_box_aspect((np.ptp(x_grid),np.ptp(y_grid),np.ptp(z_grid)));

# Farb-Plot
fig=fig+1; fh=pl.figure(fig);
pl.pcolor(x_grid, y_grid, z_grid, cmap='viridis', shading='auto');
pl.xlabel('$x$'); pl.ylabel('$y$')
pl.grid(b=False); pl.axis('image');

# Level-Linien-Plot
fig=fig+1; fh=pl.figure(fig);
pl.contour(x_grid, y_grid, z_grid, N_l, cmap='viridis');
pl.xlabel('$x$'); pl.ylabel('$y$')
pl.grid(b=False); pl.axis('image');


# Berechnung

# Ausgabe
# print(x_grid)
# print("----------")
# print(y_grid)
# print("----------")
# print(z_grid)