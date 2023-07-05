# Parameter :
q = 7.
a_0 = 1.
pr = 16
# Funktionen ;
def f(x):
    y = (2 - q * x) * x
    return y


# Iteration :
w = 0.
a = a_0
k = 0
print("--------------------------------------------------")
print(__file__)
print("--------------------------------------------------")
print("Iteration :")
print(f"a_{k} = {a:#.16g}")
while a != w:
    w = a
    k += 1
    a = f(a)
print(f"a_{k} = {a :#.16g}")
# Ausgabe :
print("--------------------------------------------------")
print(f"f({q:#.{pr}g}) = {a:#.{pr}g}")
print("--------------------------------------------------")
