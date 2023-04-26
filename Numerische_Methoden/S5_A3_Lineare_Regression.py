import numpy as np
import matplotlib.pyplot as plt
# Parameter
dg = 1
pr = 3
lw = 3
fig = 1

x_0 = 1.
x_E = 7.
y_a = -2
y_b = 3

tc_x = np.r_[x_0: x_E+0.5:0.5]
tc_y = np.r_[y_a: y_b+0.5:0.5]

# Daten
a_x = np.r_[x_0: x_E+1]
a_y = [2.5, 2.2, 1.5, 1.0, 0.6, -0.3, -1.4]
# b_x = np.r_[x_0: x_E+2:2]
# b_y = [0.5, 0.4, 1.1, 1.8, 3.5, 3.0, 4.2]

# Berechnungen
poly = np.polyfit(a_x, a_y, dg)
g_data = np.polyval(poly, a_x)

# print("polynom", poly)
m = f"{poly[0]:#.{pr}g}"
q = f"{poly[1]:#.{pr}g}"
print("--------------------------------------------------")
print(__file__)
print("--------------------------------------------------")
print(f"Steigung              m = {poly[0]:#.{pr}g}")
print(f"y-Achsabschnitt       q = {poly[1]:#.{pr}g}")
print("--------------------------------------------------")


fh = plt.figure(fig)
plt.title(f"g(x) = m*x+q = {m} * x + {q}")
plt.scatter(a_x, a_y)
plt.plot(a_x, a_y, linewidth=lw)
plt.plot(a_x, g_data, linewidth=lw)
plt.xlabel("x")
plt.ylabel("y")
plt.xticks(tc_x)
plt.yticks(tc_y)
plt.grid("on")
plt.axis("image")
plt.show()


