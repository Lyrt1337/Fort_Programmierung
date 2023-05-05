# Test 03: Matrix Multiplication

import numpy as np
import timeit
import matplotlib.pyplot as plt
from numba import jit

MAX = 11
REPEAT = 5

@jit
def mat_mul(A, B, C, vec_len):
  for i in range(vec_len):
    for j in range(vec_len):
      for k in range(vec_len):
        C[i,j] += A[i,k]*B[k,j]

flops = []
x = []

for i in range(MAX):
  vec_len = 2**i
  A = np.random.rand(vec_len, vec_len)
  B = np.random.rand(vec_len, vec_len)
  C = np.zeros((vec_len, vec_len))
  start = timeit.default_timer()
  for r in range(REPEAT):
    C.fill(0.)
    mat_mul(A, B, C, vec_len)
  stop = timeit.default_timer()
  ctime = (stop-start)/REPEAT
  flops.append((2*vec_len*vec_len*vec_len/ctime)/10**9)
  x.append(vec_len)
  print(i, "done...", flush=True)

plt.plot(x, flops, 'r-')
plt.plot(x, flops, 'r.')
plt.xscale("log")
plt.xlabel("Vector length [n]")
plt.ylabel("Performance [GFlop/s]")
plt.show()
