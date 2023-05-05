# Test 02: Matrix-Vector Multiplication

import numpy as np
import timeit
import matplotlib.pyplot as plt
from numba import jit

MAX = 15
REPEAT = 5

@jit
def mat_vec_prod(A, b, c, vec_len):
  for i in range(vec_len):
    for j in range(vec_len):
      c[i] += A[i,j]*b[j]

flops = []
x = []

for i in range(MAX):
  vec_len = 2**i
  A = np.random.rand(vec_len, vec_len)
  b = np.random.rand(vec_len)
  c = np.zeros(vec_len)
  start = timeit.default_timer()
  for r in range(REPEAT):
    c.fill(0.)
    mat_vec_prod(A, b, c, vec_len)
  stop = timeit.default_timer()
  ctime = (stop-start)/REPEAT
  flops.append((2*vec_len*vec_len/ctime)/10**9)
  x.append(vec_len)
  print(i, "done...", flush=True)

plt.plot(x, flops, 'r-')
plt.plot(x, flops, 'r.')
plt.xscale("log")
plt.xlabel("Vector length [n]")
plt.ylabel("Performance [GFlop/s]")
plt.show()
