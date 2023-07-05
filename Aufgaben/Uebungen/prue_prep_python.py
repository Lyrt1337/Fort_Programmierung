# lambda
f = lambda a: a*4
# ---------------------------
x = lambda a: a + 10
# print(x(5))
# output : 15
# ---------------------------

x = lambda a, b: a * b
# print(x(5, 6))
# ---------------------------


# The power of lambda is better shown when you use them as an anonymous function inside another function.
def myfunc(n):
    return lambda a: a * n


mytripler = myfunc(3)
# print(mytripler(11))
# output : 33
# ---------------------------
# ---------------------------


# factorial
def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n-1)
# -----------------------------------------


# endrecursive factorial
def factorial(n):
    return fac_prod(1, n)


def fac_prod(m, n):
    if n == 0:
        return m
    else:
        return fac_prod(m*n, n-1)
# -----------------------------------------


# binominal
def binomial(n, k):
    if k == 0 or k == n:
        return 1
    else:
        return binomial(n-1, k-1) + (binomial(n-1, k))
# -----------------------------------------


# endrecursive fibonnaci
def fibonnaci(n):
    return fib_help(n, 0, 1)


def fib_help(n, m, l):
    if n == 0:
        return m
    if n == 1:
        return l
    else:
        return fib_help(n-1, l, m+l)
# -----------------------------------------
# -----------------------------------------


# list comprehension
# syntax:
# newlist = [expression for item in iterable if condition == True]

# examples:
h_letters = [letter for letter in 'human']
# print( h_letters)
#same:
letters = list(map(lambda x: x, 'human'))
# output: ['h', 'u', 'm', 'a', 'n']
# -----------------------------------------

number_list = [x for x in range(20) if x % 2 == 0]
# output: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
# -----------------------------------------

# nested if
num_list = [y for y in range(100) if y % 2 == 0 if y % 5 == 0]
# print(num_list)
# output: [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
# -----------------------------------------

# if else
obj = ["Even" if i%2==0 else "Odd" for i in range(10)]
# print(obj)
# output: ['Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd']
# -----------------------------------------

# transpose matrix
transposed = []
matrix = [[1, 2, 3, 4], [4, 5, 6, 8]]

for i in range(len(matrix[0])):
    transposed_row = []

    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

print(transposed)
# [[1, 4], [2, 5], [3, 6], [4, 8]]
