n = 10

# a = 1/k

# for i in range(1, n+1):
#     print(i)
#     summation = 1/i
#     print(summation)
def myfunc(n):
    k = n
    summation = 0
    return calc(1, k, summation)


def calc(k, n, summation):
    if n <= k:
        summation += 1/k
    return calc(k, n+1, summation)


res = myfunc(10)
print(res)


# def factorial(n):
#     return fac_prod(1, n)
#
#
# def fac_prod(m, n):
#     if n == 0:
#         return m
#     else:
#         return fac_prod(m*n, n-1)