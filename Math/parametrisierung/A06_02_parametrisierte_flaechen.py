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
v_E = H
N_v = 21

fig = "a)"

#Berechnungen
# Funktion
def P(u, v):
    x = R*np.cos(u)
    y = R*np.sin(u)
    z = v
    return x,y,z

u_data = np.linspace(u_0, u_E, N_u)
v_data = np.linspace(v_0, v_E, N_v)

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


# --------------------------

# Variabeln
R = 6
H = 10

u_0 = 0
u_E = 2*np.pi
N_u = 101

v_0 = 0
v_E = R
N_v = 21

fig = "b)"

#Berechnungen
# Funktion
def P(u, v):
    x = v*np.cos(u)
    y = v*np.sin(u)
    z = H/R * v
    return x,y,z

u_data = np.linspace(u_0, u_E, N_u)
v_data = np.linspace(v_0, v_E, N_v)

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



# --------------------------

# Variabeln
R = 6
H = 10

u_0 = 0
u_E = 2*np.pi
N_u = 101

v_0 = 0
v_E = R
N_v = 21

fig = "c)"

#Berechnungen
# Funktion
def P(u, v):
    x = R*np.sin(u) * np.cos(v)
    y = R*np.sin(u) * np.sin(v)
    z = R * np.cos(u)
    return x,y,z

u_data = np.linspace(u_0, u_E, N_u)
v_data = np.linspace(v_0, v_E, N_v)

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
