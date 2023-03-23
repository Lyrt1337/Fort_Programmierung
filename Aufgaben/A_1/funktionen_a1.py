"""
-------------------------
Funktionen für Aufgabenblatt_1 Fort.Prog
Autor: Christian Gilomen
Datum: 08.03.2023
-------------------------
"""

memo = {
}

def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n-1)


def binomial(n, k):
    if k == 0 or k == n:
        return 1
    else:
        return binomial(n-1, k-1) + (binomial(n-1, k))


def ackermann_calc(x, y):
    if x == 0:
        return y + 1
    elif y == 0:
        return ackermann(x-1, 1)
    else:
        return ackermann(x-1, ackermann(x, y-1))


def ackermann(x, y):
    if not (x, y) in memo:
        for i in range(0, x+1):
            for j in range(0, y+1):
                memo[i, j] = ackermann_calc(i, j)
        return memo[x, y]
    else:
        return memo[x, y]

print(binomial(10, 7))
