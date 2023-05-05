# Test 04: Matrix Multiplication with Cache Blocking

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

@jit
def mat_mul_cb(A, B, C, vec_len, bsize):
  nb = int(vec_len/bsize)
  for i in range(nb):
    for j in range(nb):
      for k in range(nb):
        for x in range(bsize):
          for y in range(bsize):
            for z in range(bsize):
              C[i*bsize+x,j*bsize+y] += A[i*bsize+x,k*bsize+z]*B[k*bsize+z,j*bsize+y]

flops = [[],[]]
x = []

for i in range(4, MAX):
  vec_len = 2**i
  A = np.random.rand(vec_len, vec_len)
  B = np.random.rand(vec_len, vec_len)
  C = np.zeros((vec_len, vec_len))

  # original matrix multiplication
  start = timeit.default_timer()
  for r in range(REPEAT):
    C.fill(0.)
    mat_mul(A, B, C, vec_len)
  stop = timeit.default_timer()
  ctime = (stop-start)/REPEAT
  flops[0].append((2*vec_len*vec_len*vec_len/ctime)/10**9)

  # cache blocking with block size 16
  start = timeit.default_timer()
  for r in range(REPEAT):
    C.fill(0.)
    mat_mul_cb(A, B, C, vec_len, 16)
  stop = timeit.default_timer()
  ctime = (stop-start)/REPEAT
  flops[1].append((2*vec_len*vec_len*vec_len/ctime)/10**9)

  x.append(vec_len)
  print(i, "done...", flush=True)

plt.plot(x, flops[0], 'r-', label='original')
plt.plot(x, flops[0], 'r.')
plt.plot(x, flops[1], 'g--', label='CB size=16')
plt.plot(x, flops[1], 'g.')
plt.xscale("log")
plt.xlabel("Vector length [n]")
plt.ylabel("Performance [GFlop/s]")
plt.legend(frameon=False)
plt.show()
