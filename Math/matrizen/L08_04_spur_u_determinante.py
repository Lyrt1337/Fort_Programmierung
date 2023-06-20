import numpy as np

pr = 3

a = np.array([[2.,3.],[4.,5.]])
b = np.array([[2.,3.],[4.,6.]])
c = np.array([[-1.,3.,0.],[0.,2.,0.],[1.,2.,-1.]])
d = np.array([[-2.,4.,8.],[1.,-2.,-4.],[6.,-3.,12.]])
e = np.array([[1.,0.,3.,0.],[4.,-2.,12.,6.],[1.,2.,3.,-4.],[3.,3.,15.,-2.]])
f = np.array([[1.,np.sqrt(3),8.,-np.sqrt(2)],[-13.,3.,np.sqrt(2),0.],[np.sqrt(17),-1.,0.,0.],[2.,0.,0.,0.]])
g = np.array([[0.,1.,-1.],[-1.,0.,1.],[1.,-1.,0.]])
h = 1/np.sqrt(2) * np.array([[1.,-1.,0.],[1.,1.,0.],[0.,0.,np.sqrt(2)]])


t = np.trace(a)
det = np.linalg.det(a)

print(f"Trace= {t:#.3}")
print(f"Det= {det:#.3}")

t = np.trace(b)
det = np.linalg.det(b)

print(f"Trace= {t:#.3}")
print(f"Det= {det:#.3}")

t = np.trace(c)
det = np.linalg.det(c)

print(f"Trace= {t:#.3}")
print(f"Det= {det:#.3}")

t = np.trace(d)
det = np.linalg.det(d)

print(f"Trace= {t:#.3}")
print(f"Det= {det:#.3}")

t = np.trace(e)
det = np.linalg.det(e)

print(f"Trace= {t:#.3}")
print(f"Det= {det:#.3}")

t = np.trace(f)
det = np.linalg.det(f)

print(f"Trace= {t:#.3}")
print(f"Det= {det:#.3}")

t = np.trace(g)
det = np.linalg.det(g)

print(f"Trace(g)= {t:#.3}")
print(f"Det(g)= {det:#.3}")

t = np.trace(h)
det = np.linalg.det(h)

print(f"Trace(h)= {t:#.3}")
print(f"Det(h)= {det:#.3}")