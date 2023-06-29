# Python initialisieren:
import matplotlib.pyplot as pl;
import numpy as np;
# Parameter:
x_0=-2.; x_E=2.; y_0=-1.; y_E=1.;
N_x=13; N_y=13; sc=10.; aw=0.005; fig=1;
# Funktionen:
def v(x,y):
    v_x=x/2;
    v_y=y/2;
    return v_x,v_y;
# Daten:
x_data=np.linspace(x_0,x_E,N_x);
y_data=np.linspace(y_0,y_E,N_y);
[x_grid,y_grid]=np.meshgrid(x_data,y_data);
[v_x_grid,v_y_grid]=v(x_grid,y_grid);
# Plot:
fh=pl.figure(fig);
pl.quiver(x_grid,y_grid,v_x_grid,v_y_grid,scale=sc,width=aw);
pl.xlabel('x'); pl.ylabel('y');
pl.grid(visible=True); pl.axis('image');