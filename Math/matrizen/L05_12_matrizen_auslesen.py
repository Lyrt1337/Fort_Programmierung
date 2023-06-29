import numpy as np

M = np.array([np.r_[1.:7.], np.r_[7.:13.], np.r_[13.:19.], np.r_[19.:25.]])

print("M = \n", M)

# a) Komponente M_34
a = M[2:3,3:4]
a1 = M[2,3]

b = M[1:2, :]
b1 = M[1, :]

c = M[:,2:3]
c1 = M[:, 2]

d = M[:, 5:6]
d1 = M[:, 5]
d2 = M[:, -1]

e = M[[0,-1],:]

f = M[:, 1::2]
print("a= \n", a)
print("a1= \n", a1)


print("b = \n", b)
print("b1 = \n", b1)

print("c = \n", c)
print("c1 = \n", c1)

print("d = \n", d)
print("d1 = \n", d1)
print("d2 = \n", d2)

print("e = \n", e)

print("f = \n", f)