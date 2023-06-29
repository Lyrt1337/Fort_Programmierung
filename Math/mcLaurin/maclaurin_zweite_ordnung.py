import sympy as sp
import IPython.display as dp
sp.init_printing()

x = sp.symbols("x")
# Parameter
n = 2

# Aufgaben
a = sp.sqrt(1+x)

b = sp.log(sp.sqrt(sp.cos(x)))

c = 1/(1+2*sp.sin(x))

# Berechnung
T = sp.series(a,x,0,n+1)
dp.display(T)
T = sp.series(b,x,0,n+1)
dp.display(T)
T = sp.series(c,x,0,n+1)
dp.display(T)