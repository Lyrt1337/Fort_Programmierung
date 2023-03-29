import numpy as np
import matplotlib.pyplot as plt
# Parameter
dg = 1
pr = 3
lw = 3
fig = 1

# Daten
a_x = [1, 2, 3, 4, 5, 6, 7]
a_y = [2.5, 2.2, 1.5, 1.0, 0.6, -0.3, -1.4]
b_x = [-2, 0, 2, 4, 6, 8, 10]
b_y = [0.5, 0.4, 1.1, 1.8, 3.5, 3.0, 4.2]

# Berechnungen
poly = np.polyfit(a_x, a_y, dg)
g_data = np.polyval(poly, a_x)

# print("polynom", poly)
m = f"{poly[0]:#.{pr}g}"
q = f"{poly[1]:#.{pr}g}"

fh = plt.figure(fig)
plt.title(f"g(x) = m*x+q = {m} * x + {q}")
plt.scatter(a_x, a_y)
plt.plot(a_x, a_y)
plt.plot(a_x, g_data)
plt.xlabel("x")
plt.ylabel("y")
plt.grid("on")
plt.axis("image")
plt.show()


