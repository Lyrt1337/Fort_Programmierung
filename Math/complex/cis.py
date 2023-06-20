# Python initialisieren:
import numpy as np;

# Parameter

r=np.sqrt(2); phi=105*np.pi/180;

# Berechnungen
z=r*(np.cos(phi)+1j*np.sin(phi));

# Ausgabe
print("z=", f"{z:#.3}")