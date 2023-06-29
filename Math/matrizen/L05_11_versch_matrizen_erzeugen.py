import numpy as np

a = np.zeros([2,3])
b = np.ones((2,3))
c = np.array([np.r_[1.:6.], np.r_[6.:11.]])
d = np.array([np.r_[1.:10.:2], np.r_[3.:16.:3]])
e = np.eye(3)
f = -2 * np.eye(3)


print("a = \n", a)
print("b = \n", b)
print("c = \n", c)
print("d = \n", d)
print("e = \n", e)
print("f = \n", f)
