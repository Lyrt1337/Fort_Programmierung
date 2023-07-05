"""
-------------------------
Numerik Prüfung A8 Heron-Verfahren a) plot
Autor: Christian Gilomen
Datum: 30.06.2023
-------------------------
"""
import numpy as np
import matplotlib.pyplot as plt
# Parameter
q = 4
x_0 = -5
x_E = -x_0
x_1 = -0.2
x_2 = -x_1
N = 100
y_a = -4
y_b = -y_a
N_f = 201
N_g = 3
lw = 3
fig = 1
tc_x = np.r_[x_0:x_E+1.:1.]
tc_y = np.r_[y_a:y_b+1.:1.]

# Funktionen
def f(x):
    y = (2 - q * x) * x
    return y


# Daten
x_a_data = np.linspace(x_0, x_E, N_f)
x_b_data = np.linspace(x_0, x_E, N_f)
f_a_data = f(x_a_data)
f_b_data = f(x_b_data)
x_data = np.linspace(x_0, x_E, N_g)
g_data = x_data
# plot
fh = plt.figure(fig)
plt.plot(x_a_data, f_a_data, linewidth=lw)
plt.plot(x_data, g_data, linewidth=lw)
plt.xlabel("x")
plt.ylabel("y")
plt.xticks(tc_x)
plt.yticks(tc_y)
plt.grid("on")
plt.axis("image")
plt.xlim([x_0, x_E])
plt.ylim([y_a, y_b])
plt.show()
