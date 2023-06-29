import numpy as np
import matplotlib.pyplot as pl


pl.close("all")
R= 5
t_0 = 0
t_E = 2*np.pi
N = 601
fig = 1


def s(t):
    x= R*np.sin(t)
    y = R*np.cos(t)
    return x, y

tau = np.linspace(t_0, t_E, N)

x_data = 0
y_data = 0
[x_data, y_data] = s(tau)

fh = pl.figure(fig)
pl.plot(x_data, y_data)
pl.grid("on")
pl.xlabel("x")
pl.ylabel("y")
pl.axis("image")