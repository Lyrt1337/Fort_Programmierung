"""
-------------------------
Pruefung Fort.Prog
Autor: Christian Gilomen
Datum: 05.07.2023
-------------------------
"""


def primefactors(n):
    list_of_primefactors = []
    # If given number is greater than 1
    while n != 0:
        i = 2
        while True:
            for j in range(2, int(i / 2) + 1):
                if (i % j) == 0:
                    print(i, "is not a prime number")
                    i += 1
                    break
            else:
                print(i, "is a prime number")
                if n % i != 0:
                    list_of_primefactors.append(i)
                    n = n/i
                    print(list_of_primefactors)
                    False
                else:
                    i += 1
            
    print(list_of_primefactors)



    return

primefactors(100)

