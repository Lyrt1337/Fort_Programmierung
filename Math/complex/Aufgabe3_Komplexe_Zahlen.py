import numpy as np

# Aufgabe3

a=[3,0,0,1,"a"]
b=[0,1,3,0,"b"]
c=[2,3,2,3,"c"]
d=[3,4,3,-4,"d"]
e=[-3,4,-3,-4,"e"]
f=[4,9,3,7,"f"]
g=[6,1,1,-1,"g"]
h=[-2,-2,-3,1,"h"]
i=[5,6,5,-6,"i"]
j=[0,7,0,9,"j"]
k=[12,0,0,4,"k"]
l=[1,np.sqrt(3),1,-np.sqrt(3),"l"]
aufgaben=[a,b,c,d,e,f,g,h,i,j,k,l]

   
for i in aufgaben:
    z1=np.complex(i[0],i[1])
    z2=np.complex(i[2],i[3])
    print("---------")
    print("Aufgabe",i[4])
    print(z1 + z2)
    print(z1- z2)
    print(z1 * z2)
    print(z1 / z2)
    print("---------")



