def cutting_rec(n):
    if n == 0:
        return 0
    # if R[n] > 0:
    #     return R[n]
    for i in range(1, n + 1):
        R[n] = max(R[n], p[i] + cutting_rec(n-i))
        print(R)
    return R[n]


n = 10
# p = [0, 1, 3, 5, 5, 9, 10, 10, 11, 13]
p = [0, 1, 3, 7, 9, 11, 14, 18, 21, 25, 30]
R = p

result = cutting_rec(n)
print(result)
