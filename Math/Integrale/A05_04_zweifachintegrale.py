import sympy as sp
import IPython.display as dp

sp.init_printing()


x,y = sp.symbols("x,y")

f = x**2*y
x_0 = 1
x_E = 2
y_0 = 1-x
y_E = sp.sqrt(x)


I = sp.integrate(f, (y, y_0, y_E), (x, x_0, x_E))

print(f"I= {I}")
dp.display(I)