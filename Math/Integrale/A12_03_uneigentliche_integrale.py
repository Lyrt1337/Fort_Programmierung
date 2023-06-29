import sympy as sp
import IPython.display as dp

sp.init_printing()

x = sp.symbols("x")

Fa = sp.exp(1)**-x
Ia = sp.simplify(sp.integrate(Fa,(x, 0, sp.oo)))

dp.display(Ia)

Fb = 2**-x
Ib = sp.simplify(sp.integrate(Fb,(x, 0, sp.oo)))

dp.display(Ib)

Fc = 1/x
Ic = sp.simplify(sp.integrate(Fc,(x, 1, sp.oo)))

dp.display(Ic)

Fd = 1/(x**2)
Id = sp.simplify(sp.integrate(Fd,(x, 1, sp.oo)))

dp.display(Id)

Fe = 1/x
Ie = sp.simplify(sp.integrate(Fe,(x, 0, 1)))

dp.display(Ie)

Ff = 1/(sp.sqrt(x))
If = sp.simplify(sp.integrate(Ff,(x, 0, 1)))

dp.display(If)