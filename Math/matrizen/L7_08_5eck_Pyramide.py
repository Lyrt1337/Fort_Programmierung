# Python initialisieren :
import matplotlib . pyplot as pl;
import numpy as np;
# Parameter :
Q=np. array ([2 ,3 ,6]); h =14; N=5; p =49/3; A=np. array ([0 ,0 ,p ]);
lw =2; az =110 -90; el =20; fig =1;
col_O =(0 ,0.447 ,0.741); col_V =(0.85 ,0.325 ,0.098);
# Funktionen fuer Generator und Drehmatix :
def J(w):
    M=np. array ([[0 , -w[2] ,w[1]] ,[w[2] ,0 , -w[0]] ,[ -w[1] ,w [0] ,0]]);
    return M;
def R(phi ,n):
    nn=n/np. linalg . norm (n);
    M=np.eye (3)+(1 - np.cos(phi ))*J(nn)@J(nn )+ np. sin( phi )*J(nn );
    return M;
# Funktionen zum Plot von Orts - und Verbindungsvektoren :
def OVP(v):
    pl. quiver (0 ,0 ,0 ,v[0] ,v[1] ,v[2] , color =col_O ,
    linewidth =lw , arrow_length_ratio =0);
    return ;
def VVP(P,v):
    pl. quiver (P[0] ,P[1] ,P[2] ,v[0] ,v[1] ,v[2] , color =col_V ,linewidth =lw , arrow_length_ratio =0);
    return ;
# Berechnungen :
n=Q/np. linalg . norm (Q); # Einheitsvektor entlang Symmetrie - Achse
phi =2* np.pi/N; # Drehwinkel
F=h*n; # Fusspunkt F
B=R(phi ,n)@A; # Ecke B
C=R(2* phi ,n)@A; # Ecke C
D=R(3* phi ,n)@A; # Ecke D
E=R(4* phi ,n)@A; # Ecke E
# Ausgabe :
print (f"A = {A}\ nB = {B}\ nC = {C}\ nD = {D}\ nE = {E}");
# Plot :
fh=pl. figure (fig ); ax=pl. axes ( projection ="3d");
# Plot Ortsvektor des Fusspunkts F:
OVP(F);
# Plot Ortsvektoren der Ecken :
OVP(A); OVP(B); OVP(C); OVP(D); OVP(E);
# Plot Verbindungsvektoren Fusspunkt -> Ecken :
VVP(F,A-F); VVP(F,B-F); VVP(F,C-F); VVP(F,D-F); VVP(F,E-F);
# Plot Kantenvektoren der Grundflaeche :
VVP(A,B-A); VVP(B,C-B); VVP(C,D-C); VVP(D,E-D); VVP(E,A-E);
ax. set_xlabel (r"$x$ "); ax. set_ylabel (r"$y$"); ax. set_zlabel ("$z$");
ax. set_box_aspect ((1 ,1 ,1)); ax. view_init (el ,az );
