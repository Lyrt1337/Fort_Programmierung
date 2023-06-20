import numpy as np

n = 17
fac = 1
e = 1.0
pr = 16
ps = 13

for k in range(1,n+1):
    fac = fac * k
    e = e+1/fac
    print(f"Euler-Zahl: e{k} = {e:#.{pr}}")

print(f"Euler-Zahl: e = {e:#.{ps}}")