import numpy as np
import matplotlib.pyplot as plt
# Parameter
q = 4
x_0 = -5
x_E = -x_0
N = 100
y_a = -6
y_b = -y_a


# Funktionen
def f(x):
    y = 1/2 * (x + q/x)
    return y


# Daten
x_data = np.linspace(x_0, x_E, N+1)
y_data = f(x_data)
y_data2 = x_data
# plot
plt.plot(x_data, y_data)
plt.plot(x_data, y_data2)
plt.xlabel("x")
plt.ylabel("y")
plt.grid("on")
plt.xlim([x_0, x_E])
plt.ylim([y_a, y_b])
plt.show()
