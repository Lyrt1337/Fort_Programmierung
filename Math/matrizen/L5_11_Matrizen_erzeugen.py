import numpy as np;

A=np.zeros((2,3));
B=np.ones((2,3));
C=np.array([np.r_[1.:6.],np.r_[6.:11.]]);
D=np.array([np.r_[1.:10.:2],np.r_[3.:16.:3]]);
E=np.eye(3);
F=-2*np.eye(3);

print("A= ")
print(A)
print("B= ")
print(B)
print("C= ")
print(C)
print("D= ")
print(D)
print("E= ")
print(E)
print("F= ")
print(F)