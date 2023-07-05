def quad(x):
    return x*4

def fifth_root(x):
    return x**(1/5)

def another(x):
    return (x+3)*(x-3)

def h_ord(n, func):
    res = 1
    for i in range(1, n+1):
        if i % 2 == 0:
            res = res * func(i)
    return res


while True:
    print("Wählen Sie die Funktion aus:")
    print("1 - mit 4 Multiplizieren")
    print("2 - 5-te Wurzel")
    print("3 - (x+3)(x-3)")
    try:
        funktion = int(input("Auswahl: "))
        if funktion <= 0 or funktion > 3:
            print("Auswahl ungültig! Wählen Sie Option: 1, 2 oder 3")
        else:
            if funktion == 1:
                func = quad
            if funktion == 2:
                func = fifth_root
            if funktion == 3:
                func = another
            break
    except ValueError:
        print("Es sind nur Integer erlaubt")

while True:
    try:
        n = int(input("Integer eingeben: "))
        if n < 0:
            print("Negative Zahlen werden nicht zugelassen!")
        else:
            break
    except ValueError:
        print("Bitte nur Integer eingeben!")

res = h_ord(n, func)
print(res)
