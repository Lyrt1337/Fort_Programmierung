import matplotlib.pyplot as pl;
import numpy as np;

# Python konfigurieren: 
pl.close('all');
pl.rcParams['figure.figsize']=(7.03,10);
pl.rcParams['font.size']=10;
pl.rcParams['font.family']='serif';
pl.rcParams['text.usetex']=True;

# Parameter
x_0=-6; x_E=6; y_0=-3; y_E=3;
N_x=13; N_y=9; sc=16; lw=0.005; fig=1;

# Funktion
# def v(x,y):
#     v_x=2/((1+x**2+y**2)**(1/2))*x;
#     v_y=2/((1+x**2+y**2)**(1/2))*y;
#     return v_x,v_y;

def v(x,y):
    v_x=1/(np.sqrt(x**2+y**2))*x;
    v_y=1/(np.sqrt(x**2+y**2))*y;
    return v_x,v_y;

# Daten
x_data=np.linspace(x_0,x_E,N_x);
y_data=np.linspace(y_0,y_E,N_y);
[x_grid, y_grid]=np.meshgrid(x_data, y_data);
[v_x_grid,v_y_grid]=v(x_grid,y_grid);

# Plot
fh=pl.figure(fig);
pl.quiver(x_grid,y_grid,v_x_grid,v_y_grid,scale=sc,width=lw);
pl.xlabel('$x$'); pl.ylabel('$y$');
pl.grid('on'); pl.axis('image');


