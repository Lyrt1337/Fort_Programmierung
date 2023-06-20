import numpy as np
import matplotlib.pyplot as pl
pl.close("all")

Q = np.array([2,3,6])
h = 14
N = 5
p = 49/3
A = np.array([0,0,p])
col_0 =(0,0.447,0.741)
col_V =(0.85,0.325,0.098)
aw = 2
lw = 2
el = 20
az = 20
fig = 1

# Funktionen für Generator und Drehmatrix
def J(w):
    M = np.array([[0,-w[2],w[1]],[w[2],0,-w[0]],[-w[1],w[0],0]])
    return M

def R(phi, n):
    nn = n/np.linalg.norm(n)
    M = np.eye(3) + (1-np.cos(phi))*J(nn) @ J(nn) + np.sin(phi) * J(nn)
    return M

# Funktionen zum Plot von Orts- und Verbindungsvektoren
def OVP(v):
    pl.quiver(0,0,0,v[0],v[1],v[2], color= col_0, linewidth = aw, arrow_length_ratio = 0)
    return

def VVP(P,v):
    pl.quiver(P[0], P[1], P[2],v[0],v[1],v[2], color = col_V, linewidth = aw, arrow_length_ratio = 0)
    return

# Berechnungen
n = Q/np.linalg.norm(Q)
phi = 2*np.pi/N
F = h*n
B = R(phi, n) @ A
C = R(2*phi, n) @ A
D = R(3*phi, n) @ A
E = R(4*phi, n) @ A
print (f"A = {A}\ nB = {B}\ nC = {C}\ nD = {D}\ nE = {E}");
# Plot
fh=pl.figure(fig ); 
ax=pl.axes(projection ="3d");
# Fusspunkt
OVP(F)
# Ortsvektoren Ecken
OVP(A)
OVP(B)
OVP(C)
OVP(D)
OVP(E)

# Fusspunkt zu den Ecken

VVP(F, A-F)
VVP(F, B-F)
VVP(F, C-F)
VVP(F, D-F)
VVP(F, E-F)

# Kantenvektoren Grundfläche

VVP(A, B-A)
VVP(B, C-B)
VVP(C, D-C)
VVP(D, E-D)
VVP(E, A-E)

ax.set_xlabel("$x$")
ax.set_ylabel("$y$")
ax.set_zlabel("$z$")
ax.set_box_aspect((1,1,1))
ax.view_init(el,az)