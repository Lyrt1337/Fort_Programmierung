# Python initialisieren :
import IPython.display as dp;
import sympy as sp;
# Python konfigurieren :
sp.init_printing();
r,x,y,alpha,tau=sp.symbols("r,x,y,alpha,tau");
# Parameter :
tau_0= 0; tau_E= 2;
# Funktionen :
def w(x,y):
    res=sp.Matrix([[0.5] ,[0.25]]);
    return res ;
def s(tau):
    res=sp.Matrix ([[1-2*tau] ,[3+8*tau]]);
    return res ;
# Berechnungen :
v=sp.simplify(sp.diff(s(tau),tau));
I=sp.simplify(sp.integrate(v.dot(w(s(tau)[0], s(tau)[1]))
,(tau, tau_0, tau_E)));
# Ausgabe :
dp.display(I);