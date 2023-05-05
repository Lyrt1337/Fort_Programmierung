# Test 01: SchÃ¶nauer Vector Triad

import numpy as np
import timeit
import matplotlib.pyplot as plt
from numba import jit

MAX = 26
REPEAT = 5

@jit
def vec_triad(a, b, c, d, vec_len):
  for i in range(vec_len):
    a[i] = b[i] + c[i]*d[i]

flops = []
x = []

for i in range(MAX):
  vec_len = 2**i
  a = np.zeros(vec_len)
  b = np.random.rand(vec_len)
  c = np.random.rand(vec_len)
  d = np.random.rand(vec_len)
  start = timeit.default_timer()
  for r in range(REPEAT):
    vec_triad(a, b, c, d, vec_len)
  stop = timeit.default_timer()
  ctime = (stop-start)/REPEAT
  flops.append((2*vec_len/ctime)/10**9)
  x.append(vec_len)
  print(i, "done...", flush=True)

plt.plot(x, flops, 'r-')
plt.plot(x, flops, 'r.')
plt.xscale("log")
plt.xlabel("Vector length [n]")
plt.ylabel("Performance [GFlop/s]")
plt.show()