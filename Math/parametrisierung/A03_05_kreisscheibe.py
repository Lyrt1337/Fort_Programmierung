import numpy as np
import matplotlib.pyplot as pl

pl.close("all")

# Parameter
fig = 1
sc = 180
aw = 0.005

x_0 = -20
x_E = 20

y_0 = -20
y_E = 20

N_x = 18
N_y = 18

# Funktionen
def v(x,y):
    v_x = 12.6/(np.sqrt(x**2 + y**2))*-y
    v_y = 12.6/(np.sqrt(x**2 + y**2))*x
    return v_x, v_y

# Daten

x_data = np.linspace(x_0, x_E, N_x)
y_data = np.linspace(y_0, y_E, N_y)
[x_grid, y_grid] = np.meshgrid(x_data, y_data)
[v_x_grid, v_y_grid] = v(x_grid, y_grid)

# Ausgabe
# print(x_data)
# print(y_data)
# print(x_grid)
# print(y_grid)
# print(v_x_grid)
# print(v_y_grid)
fh = pl.figure(fig)
pl.quiver(x_grid, y_grid, v_x_grid, v_y_grid, scale = sc, width = aw)
pl.xlabel("$x$")
pl.ylabel("$y$")
pl.grid("on")
pl.axis("tight")