# Python initialisieren:
import matplotlib.pyplot as pl;
from mpl_toolkits import mplot3d;
import numpy as np;
# Parameter:
x_0=-2; x_E=2; y_0=-1; y_E=1;
N_x=401; N_y=201; N_g=10; N_l=21;
az=-25; el=20; cm='viridis'; fig=1;
# Funktionen:
def f(x,y): z=x*y; return z;
# Daten:
x_data=np.linspace(x_0,x_E,N_x);
y_data=np.linspace(y_0,y_E,N_y);
[x_grid,y_grid]=np.meshgrid(x_data,y_data);
z_grid=f(x_grid,y_grid);
# Graph-Plot:
fh=pl.figure(fig); ax=pl.axes(projection='3d');
ax.plot_surface(x_grid,y_grid,z_grid,rstride=N_g,cstride=N_g,cmap=cm);
ax.view_init(el,az);
ax.set_xlabel(r'$x$'); ax.set_ylabel(r'$y$'); ax.set_zlabel(r'$z$');
ax.set_box_aspect((np.ptp(x_grid),np.ptp(y_grid),np.ptp(z_grid)));
# Farb-Plot:
fig=fig+1; fh=pl.figure(fig);
pl.pcolor(x_grid,y_grid,z_grid,cmap=cm,shading='auto');
pl.xlabel(r'$x$'); pl.ylabel(r'$y$');
pl.grid(visible=False); pl.axis('image');
# Level-Linien-Plot:
fig=fig+1; fh=pl.figure(fig);
pl.contour(x_grid,y_grid,z_grid,N_l,cmap=cm);
pl.xlabel(r'$x$'); pl.ylabel(r'$y$');
pl.grid(visible=True); pl.axis('image');
#