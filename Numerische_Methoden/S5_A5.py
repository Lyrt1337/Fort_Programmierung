# Python initialisieren :
import matplotlib.pyplot as pl;
import numpy as np;
# Parameter :
p_0 = 0.
p_E = 2.
n_a = 0.
n_b = 20.
E_a = 0.
E_b = 0.2
dg = 1
pr = 4
sc_E = 1e-3
N = 201
lw = 3
sp = 0.3
fig = 1
tc_p = np.r_[p_0:p_E + 2:0.5]
tc_n = np.r_[n_a:n_b + 50:50]
tc_E =np.r_[E_a:E_b]
# Daten :
p_data_gem = np.array([1.3, 1.4, 1.5, 1.6, 1.7])
n_data_gem = np.array([17, 15, 14, 13, 11])
# Berechnungen :
E_data_gem = n_data_gem * p_data_gem
r=np.polyfit(p_data_gem, n_data_gem, dg)
p_data = np.linspace(p_0, p_E, N)
n_data = np.polyval(r, p_data)
E_data = n_data * p_data
# Ausgabe :
print("--------------------------------------------------")
print(__file__)
print("--------------------------------------------------")
print(f" Steigung : m = {r[0]:#.{pr}g} / CHF")
print(f"n- Achsabschnitt : q = {r[1]:#.{pr}g}")
print("--------------------------------------------------")
# Plot :
[fh, ax] = pl.subplots(2, 1)
ax[0].plot(p_data, n_data, linewidth=lw)
ax[0].plot(p_data_gem, n_data_gem, "o", linewidth=lw)
ax[0].set_xlabel(r"$p [\mathrm {CHF }]$")
ax[0].set_ylabel(r"$n$")
ax[0].set_xticks(tc_p)
ax[0].set_yticks(tc_n)
ax[0].grid(visible=True)
ax[1].plot(p_data, E_data * sc_E, linewidth =lw )
ax[1].plot(p_data_gem, E_data_gem * sc_E, "o", linewidth=lw)
ax[1].set_xlabel(r"$p[\mathrm {CHF }]$")
ax[1].set_ylabel(r"$E[\mathrm {kCHF}]$")
ax[1].set_xticks(tc_p)
ax[1].set_yticks(tc_E)
ax[1].grid(visible=True)
pl.subplots_adjust(hspace=sp)
pl.show()
