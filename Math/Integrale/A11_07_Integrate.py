import sympy as sp
import IPython.display as dp

sp.init_printing()

a, r, t, x, omega = sp.symbols("a, r, t, x, omega")


I = sp.simplify(sp.integrate(1/(1+x**4), x))
F = sp.simplify(sp.integrate(sp.exp(a*t)*sp.sin(omega*t), t))
G = sp.simplify(sp.integrate(r**3 * sp.cos(r**2), r))

print(I)
dp.display(I)

print(F)
dp.display(F)

print(G)
dp.display(G)