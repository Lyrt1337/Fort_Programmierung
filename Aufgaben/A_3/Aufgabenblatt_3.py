"""
-------------------------
Aufgabenblatt_3.py Fort.Prog
Autor: Christian Gilomen
Datum: 23.03.2023
-------------------------
"""

from funktionen_a3 import *
import random as rnd
import numpy as np

print("----------------------")
print("Aufgabe 11 - Klassen und Attribute")
print("----------------------")

class Vehicle:
    def __init__(self, color, brand, construction_year, number_of_tyres, power):
        self.color = color
        self.brand = brand
        self.construction_year = construction_year
        self.number_of_tyres = number_of_tyres
        self.power = f"{power} PS"




print("----------------------")
print("Aufgabe 12 - Methoden")
print("----------------------")


def tyres(self):
    print(f"The {self.brand} needs {self.number_of_tyres} tyres")


def con_year(self):
    print(f"The {self.color} {self.brand} was built in {self.construction_year}")

print("----------------------")
print("Aufgabe 13 - Objekte und Instanzen")
print("----------------------")


vehicles = []

def create_vehicles(num_of_Vehicles):
    for i in range(1, num_of_Vehicles + 1):
        # name = "Vehicle No."+ str(i)
        colors = ["blue", "red", "yellow", "orange", "black", "white", "green"]
        color = np.random.choice(colors)
        brands = ["Toyota", "Nissan", "Porsche", "VW", "Opel", "Skoda", "Volvo", "Koenigsegg", "Honda", "Suzuki"]
        brand = np.random.choice(brands)
        construction_year = rnd.randint(1900, 2023)
        if brand == "Honda" or brand == "Suzuki":
            number_of_tyres = 2
        else:
            number_of_tyres = 4
        power = rnd.randint(50, 1500)
        new_vehicle = Vehicle(color, brand,
                              construction_year, number_of_tyres, power)

        vehicles.append(new_vehicle.brand)

        # print(new_vehicle.color)
        # print(new_vehicle.brand)
        # print(new_vehicle.construction_year)
        # print(new_vehicle.number_of_tyres)
        # print(new_vehicle.power)
        # print("---------------")
    return vehicles


vehicle_list = create_vehicles(12)


print(vehicle_list)


print("----------------------")
print("Aufgabe 14 - Vererbung")
print("----------------------")


class Car(Vehicle):
    usecase = "transport"
    def __init__(self, num_of_doors, num_of_seats, warranty):
        self.number_of_doors = num_of_doors
        self.num_of_seats = num_of_seats
        self.warranty = warranty


class Motorbike(Vehicle):
    def __init__(self, num_of_mirrors, bodykit, exhaust_type):
        self.num_of_mirrors = num_of_mirrors
        self.bodykit = bodykit
        self.exhaust_type = exhaust_type


class Truck(Vehicle):
    def __init__(self, hanger_length, load_capacity, special_permit):
        self.hanger_length = hanger_length
        self.load_capacity = load_capacity
        self.special_permit = special_permit


some = Truck("blue", "volvo", 1988, 18, 2500, 20, 7500, "g56n")

print("Hanger Length:", some.hanger_length)
print("Number of tyres:", some.number_of_tyres)
print("Capacity:", some.load_capacity)


print("----------------------")
print("Aufgabe 15 - Objekte und Datenbanken")
print("----------------------")

