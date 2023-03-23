"""
-------------------------
Aufgabenblatt_1.py Fort.Prog
Autor: Christian Gilomen
Datum: 08.03.2023
-------------------------
"""

from funktionen_a1 import factorial, binomial, ackermann
import pandas as pd



print("----------------------")
print("Aufgabe 1")
print("----------------------")


projekt_gruppe = {"Lead": "Eli Preter",
                  "Member 1": "Thomas Mächler",
                  "Member 2": "Joshua Kohler",
                  "Member 3": "Christian Gilomen"}

print("Gruppe:")
for i in projekt_gruppe:
    print(i, ":", projekt_gruppe[i])


print("----------------------")
print("Aufgabe 2")
print("----------------------")

df = pd.read_feather("../dataset/dblp.feather")
cols = df.columns
shape = df.shape

print("a) Komponenten:")
print(f"{cols}")
print("b)")
print(f"Rows: {shape[0]}")
print(f"Rows: {shape[1]}")
print("Leere Zellen: 163776323")
print(f"Datenelemente: {int(shape[0] * shape[1] - 163776323)}")
print("Für genauere Angaben siehe dblp_report.html")
print("Speicherplatz: 3.53 GB in xml und 808 MB in Feather")
print("Speicherplatz in Memory: 1.82 GB")
print("c) Forschungsfrage")
print("- Welche Autoren arbeiten am häufigsten zusammen?")
print("- In welchem Feld ist die Forschung stark zurückgegangen / angestiegen?")
print("- In welchem Zeitraum gab es die meisten Publikationen?")


print("----------------------")
print("Aufgabe 3 - Rekursive Funktion")
print("----------------------")


for i in range(0, 10):
    result = factorial(i)
    print(f"{i}! = {result}")


print("----------------------")
print("Aufgabe 4 - Mehrfach rekursive Funktion")
print("----------------------")


result = binomial(10, 7)
print(result)


print("----------------------")
print("Aufgabe 5 - Die Ackermann-Funktion")
print("----------------------")


# Ackermann für (1, 1), (2, 2) und (3, 3)
for i in range(1, 4):
    a = ackermann(i, i)
    print(f"Ackermann({i}, {i}) = {a}")

# Ackermann(4, 4) rekursiv zu berechnen würde unglaublich lange dauern
# die Zahl kann ausserdem nur noch mit Knuth's notation dargestellt werden
print("Ackermann(4, 4) = 2 ↑↑ (y + 3) - 3   bzw.:   2**(2**(65536)-3)")
