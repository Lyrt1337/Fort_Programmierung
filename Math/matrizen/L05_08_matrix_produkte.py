import numpy as np

A = np.array([[4,-3,2],[6,2,5],[-1,-2,3]])
B = np.array([[3,4],[1,2],[5,6]])
u = np.array([[0],[2],[-4]])
v = np.array([[1],[3],[-3]])

a = A @ B
b = "Das Matrix-Produkt B * A ist nicht definiert"
c = A @ u
d = A @ A
e = "Das Matrix-Produkt B * B ist nicht definiert"
f = v.T @ u
g = "Das Matrix-Produkt v * u ist nicht definiert"
h = u @ v.T
i = B.T @ v
j = v.T @ B

print("a = \n", a)
print("-----------------")
print("b = \n", b)
print("-----------------")
print("c = \n", c)
print("-----------------")
print("d = \n", d)
print("-----------------")
print("e = \n", e)
print("-----------------")
print("f = \n", f)
print("-----------------")
print("g = \n", g)
print("-----------------")
print("h = \n", h)
print("-----------------")
print("i = \n", i)
print("-----------------")
print("j = \n", j)