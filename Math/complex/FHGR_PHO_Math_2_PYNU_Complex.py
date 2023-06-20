# Python initialisieren:
import numpy as np;
# Parameter:
z=3+4j;
c=5-3j;
# Berechnungen:
x=np.real(z);
y=np.imag(z);
w=np.conj(z);
r=np.abs(z);
q=z/c;
# Ausgabe;
print(f"z = {z:#.4}");
print(f"q = {q:#.4}");