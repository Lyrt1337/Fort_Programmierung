# Python initialisieren
import numpy as np

# Parameter
w=7-5j
z=0-4j

# Berechnungen
x=np.real(z)
y=np.imag(z)
zs=np.conj(z)
r=np.abs(z)
phi=np.angle(z)
u=w/z

# Ausgabe
print("z=", f"{z:#.3}")
print("z*=", f"{zs:#.3}")
print("x=", f"{x:#.3}")
print("y=", f"{y:#.3}")
print("r=", f"{r:#.3}")
print("phi=", f"{phi/np.pi:#.3}", "pi")
print("u=", f"{u:#.3}")