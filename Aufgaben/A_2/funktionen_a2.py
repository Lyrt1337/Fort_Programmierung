"""
-------------------------
Funktionen für Aufgabenblatt_2 Fort.Prog
Autor: Christian Gilomen
Datum: 13.03.2023
-------------------------
"""
# A6
# a)
def factorial(n):
    return fac_prod(1, n)


def fac_prod(m, n):
    if n == 0:
        return m
    else:
        return fac_prod(m*n, n-1)

# -------------------
# b)
def fibonnaci(n):
    return fib_help(n, 0, 1)


def fib_help(n, m, l):
    if n == 0:
        return m
    if n == 1:
        return l
    else:
        return fib_help(n-1, l, m+l)
    
# -------------------
# c)

def sumup(n):
    return sum_help(0, n*2)


def sum_help(m, n):
    if (n % 2) != 0:
        n -= 1
    if n == 0:
        return m
    else:
        return sum_help(m+n, n-1)
    
# -------------------
# A8 (factorial already done in A6)
def mult(x):
    f = 2*x
    return f

def quad(x):
    f = x*x
    return f

def h_ord(n, func):
    res = 0
    for i in range(1, n+1):
        res += func(i)
    return res

# -------------------
# A10


def listOp(liste, op):
    res = op(liste)
    return res


def sort_asc(liste):
    for i in range(len(liste)):
        for j in range(i+1, len(liste)):
            
            if str(liste[i]) > str(liste[j]):
                liste[i], liste[j] = liste[j], liste[i]
    
    return liste


def sort_desc(liste):
    for i in range(len(liste)):
        for j in range(i+1, len(liste)):
            
            if str(liste[i]) < str(liste[j]):
                liste[i], liste[j] = liste[j], liste[i]
    
    return liste


def reverse(liste):
    new_list = []
    for i in range(len(liste)):
        new_list.append(liste[len(liste)-1-i])
    return new_list


def concatenate(liste):
    list_string = ""
    for i in range(len(liste)):
        list_string += " "
        list_string += str(liste[i])
    return list_string



