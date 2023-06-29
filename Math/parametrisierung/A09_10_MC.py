import numpy as np
import matplotlib.pyplot as pl
from mpl_toolkits import mplot3d


pl.close("all")

# Variabeln
R = 6
H = 10

u_0 = 0
u_E = 2*np.pi
N_u = 101

v_0 = 0
v_E = 2*np.pi
N_v = 101

fig = "a)"

#Berechnungen
# Funktion
def P(u, v):
    x = u
    y = v
    z = np.sin(u) + np.cos(v)
    return x,y,z

u_data = np.linspace(u_0, u_E, N_u)
v_data = np.linspace(v_0, v_E, N_v)
z_data = np.linspace(2,2,N_v)

[u_grid, v_grid] = np.meshgrid(u_data, v_data)
[x_grid, y_grid, z_grid] = P(u_grid, v_grid)

#plot
fh = pl.figure(fig)
ax = pl.axes(projection="3d")
ax.plot_surface(x_grid, y_grid, z_grid, cmap="viridis")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.set_box_aspect((np.ptp(x_grid), np.ptp(y_grid), np.ptp(z_grid)))
pl.grid("on")
