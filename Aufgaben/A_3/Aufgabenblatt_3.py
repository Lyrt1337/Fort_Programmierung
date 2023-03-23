"""
-------------------------
Aufgabenblatt_3.py Fort.Prog
Autor: Christian Gilomen
Datum: 23.03.2023
-------------------------
"""

from funktionen_a3 import *

print("----------------------")
print("Aufgabe 11 - Klassen und Attribute")
print("----------------------")

class Vehicle:
    def __init__(self, color, brand, construction_year, number_of_tyres, power):
        self.color = color
        self.brand = brand
        self.construction_year = construction_year
        self.number_of_tyres = number_of_tyres
        self.power = power

    def tyres(self):
        print(f"The {self.brand} needs {self.number_of_tyres} tyres")

    def con_year(self):
        print(f"The {self.color} {self.brand} was built in {self.construction_year}")


print("----------------------")
print("Aufgabe 12 - Methoden")
print("----------------------")



print("----------------------")
print("Aufgabe 13 - Objekte und Instanzen")
print("----------------------")



print("----------------------")
print("Aufgabe 14 - Vererbung")
print("----------------------")



print("----------------------")
print("Aufgabe 15 - Objekte und Datenbanken")
print("----------------------")

