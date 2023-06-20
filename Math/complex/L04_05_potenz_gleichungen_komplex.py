import sympy as sp

z,a,b,c,d,e,f = sp.symbols("z,a,b,c,d,e,f")
l= [z**2, z**2, z**3, z**3, z**3, z**4] 
r = [-49, sp.I, -8, -27*sp.I, 1-sp.sqrt(3)*sp.I, -8+8*sp.sqrt(3)*sp.I]
aufgaben=[a,b,c,d,e,f]


for i in range(0,6):
    
    L = sp.solve(l[i]-r[i],z)
    print(aufgaben[i],") L =",L)