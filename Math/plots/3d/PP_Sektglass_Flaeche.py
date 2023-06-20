# Python initialisieren :
import numpy as np;
# Parameter :
R =3.0; H =10.0;
r_0 =0; r_E=R; N =100; n=5; pr =3;
# Funktionen :
a = 4*H **2/R**4;
def f(r):
    y=r*np.sqrt(1+a*(R-r )**2); return y;
# Daten :
for k in range (0,n):
    r_data = np.linspace(r_0 ,r_E ,N)
    f_data = f(r_data)
# Berechnungen :
I_r =np.trapz(f_data, r_data)
# Ausgabe :
print (f"I_r = {I_r :#.16} ");
N=2*N;
A=2* np.pi*I_r;
# Ausgabe :
print (f"A = {A :#.{ pr }} cm ^2");