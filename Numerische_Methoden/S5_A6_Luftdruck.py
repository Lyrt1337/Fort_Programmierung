# Python initialisieren :
import matplotlib.pyplot as pl
import numpy as np
# Parameter :
h_PB = 4049.
h_0 = 0.
h_E = 5000.
y_a = 6.
y_b = 7.
p_a = 500.
p_b = 1100.
dg = 1
pr = 4
N = 201
lw = 3
sp = 0.3
fig = 1
tc_h = np.r_[h_0:h_E + 500:500]
tc_y = np.r_[y_a:y_b + 0.1:0.1]
tc_p = np.r_[p_a:p_b + 100:100]
# Daten :
h_data_gem = np.array([273., 412., 556., 990., 1638., 1709., 3550.])
p_data_gem = np.array([976.9, 973.6, 955.5, 902.3, 834.2, 824.7, 649.])
# Berechnungen :
y_data_gem = np.log(p_data_gem)
r = np.polyfit(h_data_gem, y_data_gem, dg)
h_data = np.linspace(h_0, h_E, N)
y_data = np.polyval(r, h_data)
m = r[0]
q = r[1]
Sigma = -1 / m
p_0 = np.exp(q)


# Funktionen :
def p(h):
    res = p_0 * np.exp(-h / Sigma)
    return res


# Berechnungen :
p_data = p(h_data)
p_PB = p(h_PB)
# Ausgabe :
print("--------------------------------------------------")
print(__file__)
print("--------------------------------------------------")
print(f" Steigung : m = {m :#.{pr}g} / m")
print(f"y- Achsabschnitt : q = {q:#.{pr}g}")
print(f" Referenzdruck : p_0 = {p_0:#.{pr}g} hPa")
print(f" Schrittweite : Sigma = { Sigma:#.{pr}g} m")
print(f" Luftdruck Piz Bernina : p_PB = { p_PB:#.{pr}g} hPa")
print("--------------------------------------------------")
# Plot :
[fh, ax] = pl.subplots(2, 1)
ax[0].plot(h_data, y_data, linewidth=lw)
ax[0].plot(h_data_gem, y_data_gem, "o", linewidth=lw)
ax[0].set_xlabel(r"$h [\mathrm {m}]$")
ax[0].set_ylabel(r"$y$")
ax[0].set_xticks(tc_h)
ax[0].set_yticks(tc_y)
ax[0].grid(visible=True)
ax[1].plot(h_data, p_data, linewidth=lw)
ax[1].plot(h_data_gem, p_data_gem, "o", linewidth=lw)
ax[1].set_xlabel(r"$h [\mathrm {m}]$")
ax[1].set_ylabel(r"$p [\mathrm {hPa }]$")
ax[1].set_xticks(tc_h)
ax[1].set_yticks(tc_p)
ax[1].grid(visible=True)
pl.subplots_adjust(hspace=sp)
pl.show()
