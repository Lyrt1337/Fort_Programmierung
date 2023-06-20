import sympy as sp
import numpy as np

r,x,y,alpha,tau, pi = sp.symbols("r,x,y,alpha,tau,pi")

tau_0 = 0
tau_E = 1


def w(x,y):
    res = sp.Matrix([[y],[-x]])
    return res

def s(tau):
    res = sp.Matrix([[3*sp.cos(2*pi*tau)],[3*sp.sin(2*pi*tau)]])
    return res

v = sp.simplify(sp.diff(s(tau), tau))
I = sp.simplify(sp.integrate(v.dot(w(s(tau)[0], s(tau)[1])), (tau, tau_0, tau_E)))


print("w(x,y) = ", w(x,y))
print("s(tau) = ", s(tau))
print("v = s' =", v)
print(f"I = {I}")

print(sp.simplify(v.dot(w(s(tau)[0], s(tau)[1]))))


