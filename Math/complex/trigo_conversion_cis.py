# Python initialisieren:
import numpy as np;

# in die Arithmetische Form

# Parameter
r= 13; phi= 0.874*np.pi ;

# Berechnung
z=r*(np.cos(phi)+1j*np.sin(phi));

# Ausgabe
print("z = ",r, f"* cis( {phi/np.pi:#.3} pi ) = " f"{z:#.3}")

# in die Trigonometrische form
# Parameter:
z=-12+5j;

# Berechnungen:
r=np.abs(z); phi=np.angle(z);

# Ausgabe
print("z =", f"{z:#.3}","=",
      f"{r:#.3}","* cis(",
      f"{phi/np.pi:#.3}","pi )")