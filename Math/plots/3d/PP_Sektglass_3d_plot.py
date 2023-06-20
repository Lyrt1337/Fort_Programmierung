# Python initialisieren :
import matplotlib . pyplot as pl
import numpy as np

pl.close("all")

# Parameter :
R = 3.0
H = 10.0
r_0 = 0
r_E = R
phi_0 = 0
phi_E = 2*np.pi
N_r =18
N_phi = 90
fig =1

# Funktionen :
def P(r ,phi):
    x = r*np.cos(phi)
    y = r*np.sin(phi)
    z = -(R-r)**2*H/R**2
    return x,y,z

# Daten :
r_data = np.linspace(r_0, r_E, N_r)
phi_data = np.linspace (phi_0 ,phi_E , N_phi )
[r_grid, phi_grid]= np.meshgrid(r_data, phi_data )
[x_grid, y_grid, z_grid] = P(r_grid, phi_grid )

# Plot :
fh=pl.figure(fig) 
ax=pl.axes(projection ="3d")
ax.plot_surface(x_grid, y_grid, z_grid, cmap ="viridis")
ax.set_xlabel(r"$x$")
ax.set_ylabel(r"$y$")
ax.set_zlabel(r"$z$")
ax.set_box_aspect((np.ptp(x_grid), np.ptp(y_grid), np.ptp(z_grid)))