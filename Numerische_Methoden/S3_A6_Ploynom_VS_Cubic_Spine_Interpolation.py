# Python initialisieren :
import matplotlib.pyplot as pl
import scipy.interpolate as ip
import numpy as np
# Parameter :
x_data = np.array([1., 2., 3., 4., 5., 6., 7., 8., 9., 10.])
y_data = np.array([1., 1., 1., 1., 1., 3., 3., 3., 3., 3.])
x_0 = 0
x_E = 11
y_a = -1
y_b = 5
N = 501
lw = 3
sp = 0.2
fig = 1
tc_x = np.r_[x_0:x_E + 1]
tc_y = np.r_[y_a:y_b + 0.5:0.5]
# Berechnungen :
po = ip.BarycentricInterpolator(x_data, y_data)
cs = ip.CubicSpline(x_data, y_data)
# Daten :
u_data = np.linspace(x_0, x_E, N)
v_data = po(u_data)
w_data = cs(u_data)
# Plot :
[fh, ax] = pl.subplots(2, 1)
ax[0].plot(u_data, v_data, linewidth=lw)
ax[0].plot(x_data, y_data, "o", linewidth=lw)
ax[0].set_xlabel(r"$x$")
ax[0].set_ylabel(r"$y$")
ax[0].set_xticks(tc_x)
ax[0].set_yticks(tc_y)
ax[0].grid(visible = True )
ax[0].axis([x_0 ,x_E ,y_a ,y_b])
ax[1].plot(u_data ,w_data , linewidth=lw)
ax[1].plot(x_data ,y_data ,"o", linewidth=lw)
ax[1].set_xlabel(r"$x$")
ax[1].set_ylabel(r"$y$")
ax[1].set_xticks(tc_x)
ax[1].set_yticks(tc_y)
ax[1].grid(visible = True)
ax[1].axis([x_0, x_E, y_a, y_b])
pl.subplots_adjust(hspace=sp)
pl.show()
