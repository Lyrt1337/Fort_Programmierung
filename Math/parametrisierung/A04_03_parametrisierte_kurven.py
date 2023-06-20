import numpy as np
import matplotlib.pyplot as pl


pl.close("all")

t_0 = -2
t_E = 2
N = 601
fig = 1


def s(t):
    x= 2*t-3
    y = 2-t
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