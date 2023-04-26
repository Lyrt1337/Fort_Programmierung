# Python initialisieren :
import numpy as np
# Parameter :
a = 12.3
b = 8.14
pr = 3
ME="cm";
# Berechnungen:
c = np.sqrt(a**2 + b**2)
# Ausgabe :
print("--------------------------------------------------")
print(__file__)
print("--------------------------------------------------")
print(f"Seite a = {a:#.{pr}g} {ME}")
print(f"Seite b = {b:#.{pr}g} {ME}")
print(f"Seite c = {c:#.{pr}g} {ME}")
print("--------------------------------------------------")