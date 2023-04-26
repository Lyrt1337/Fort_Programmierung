# Parameter :
q = 2.
a_0 = 1.
pr = 16
# Funktionen ;
def f(x):
    y = 0.5 * (x+q/x)
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
print(f"Wurzel : sqrt ({q:#.{pr}g}) = {a:#.{pr}g}")
print("--------------------------------------------------")