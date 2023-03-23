"""
-------------------------
Aufgabenblatt_2.py Fort.Prog
Autor: Christian Gilomen
Datum: 13.03.2023
-------------------------
"""

from funktionen_a2 import factorial, fibonnaci, sumup, mult, quad, h_ord, \
listOp, sort_asc, sort_desc, reverse, concatenate

print("----------------------")
print("Aufgabe 6 - Endrekursion")
print("----------------------")


while True:
    try:
        n = int(input("Integer eingeben: "))
        if n < 0:
            print("Negative Zahlen werden nicht zugelassen!")
        else:
            break
    except ValueError:
        print("Bitte nur Integer eingeben!")

print("a) Fakutät berechnen:")
print(f"{n}! = {factorial(n)}")
print("--------------\n")

print("b) Fibonnaci-Folge:")
print(f"Fibo_{n} = {fibonnaci(n)}")
print("--------------\n")

print("c) Summe der ersten n geraden natürlichen Zahlen:")      
print(f"Summe_{n} = {sumup(n)}")
print("--------------\n")


print("----------------------")
print("Aufgabe 7 - lambda Funktionen")
print("----------------------")


print("a) Multiplikation mit 4")
while True:
    try:
        a = float(input("Zahl eingeben: "))
        f = lambda a: a*4
        print(f"{a} * 4 = {f(a)}")
        break
    except ValueError:
        print("Bitte nur Zahlen eingeben!")

print("--------------\n")

print("b) dritte Wurzel aus x*x")
while True:
    try:
        b = float(input("Zahl eingeben: "))
        f = lambda b: (b*b)**(1/3)
        print(f"({b} * {b}) ** (1/3) = {f(b)}")
        break
    except ValueError:
        print("Bitte nur Zahlen eingeben!")

print("--------------\n")

print("c) Summe aller Zahleneinträge einer Liste")
array = [0]
while True:
    try:
        c = float(input("Zahlen eingeben? (Abbruch mit 0): "))
        if c != 0:
            array.append(c)
        else:
            f = lambda c: c[0] if len(c) == 1 else c[0] + f(c[1:])
            print("--------------")
            print(f"alle Zahlen {array} aufsummiert: {f(array)}")
            break
    except ValueError:
        print("Bitte nur Zahlen eingeben!")

print("--------------\n")


print("----------------------")
print("Aufgabe 8 Funktionen höherer Ordnung")
print("----------------------")


while True:
    print("Wählen Sie die Funktion aus:")
    print("1 - mit 2 Multiplizieren")
    print("2 - Quadrieren")
    print("3 - Fakultät berechnen")
    try:
        funktion = int(input("Auswahl: "))
        if funktion <= 0 or funktion > 3:
            print("Auswahl ungültig! Wählen Sie Option: 1, 2 oder 3")
        else:
            if funktion == 1:
                func = mult
            if funktion == 2:
                func = quad
            if funktion == 3:
                func = factorial
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


print("----------------------")
print("Aufgabe 9")
print("----------------------")


# anonyme Fakultätsfunktion
while True:
    try:
        n = int(input("Integer eingeben um Fakultät auszurechnen: "))
        if n < 0:
            print("Negative Zahlen werden nicht zugelassen!")
        else:
            f = lambda n : 1 if n <= 1 else n*f(n-1)
            print(f"{n}! = {f(n)}")
            break
    except ValueError:
        print("Bitte nur Integer eingeben!")
        


print("----------------------")
print("Aufgabe 10")
print("----------------------")

# list1 =[7.3, 5, "ich bin ein String", True]
# print(listOp(list1, sort_asc))

list1 = [True, 84, 25, False, "Stringy"]

list1.append(input("Möchten Sie weitere Werte in die Liste eintragen?: "))
while True:   
    c = input("Weitere Einträge? (Abbruch mit esc): ")
    if c != "esc":
        list1.append(c)
    else:
        break
    
while True:
    try:
        print("bitte gewünschte Aktion wählen:")
        print("1 - Liste aufsteigend sortieren")
        print("2 - Liste absteigend sortieren")
        print("3 - Liste umkehren")
        print("4 - Liste in einen String konkatenieren")
        auswahl = int(input("Auswahl: "))
        if auswahl <= 0 or auswahl > 4:
            print("Auswahl ungültig! Wählen Sie Option: 1, 2, 3 oder 4")
        else:
            if auswahl == 1:
                func = sort_asc
            if auswahl == 2:
                func = sort_desc
            if auswahl == 3:
                func = reverse
            if auswahl == 4:
                func = concatenate
            f = listOp(list1, func)
            print("--------------")
            print(f"Neue Liste: {f}")
            break
    except ValueError:
        print("Auswahl ungültig! Wählen Sie Option: 1, 2, 3 oder 4")
