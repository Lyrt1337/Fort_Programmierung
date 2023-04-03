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
import pandas as pd

print("----------------------")
print("Aufgabe 11 - Klassen und Attribute")
print("----------------------")


class Vehicle:
    usecase = "transport"

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


def create_vehicles(num_of_vehicles):
    for i in range(1, num_of_vehicles + 1):
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

        vehicles.append([new_vehicle.color, new_vehicle.brand, new_vehicle.construction_year,
                         new_vehicle.number_of_tyres, new_vehicle.power])

        # print(new_vehicle.color)
        # print(new_vehicle.brand)
        # print(new_vehicle.construction_year)
        # print(new_vehicle.number_of_tyres)
        # print(new_vehicle.power)
        # print("---------------")
    return vehicles


vehicle_list = create_vehicles(12)


print(*vehicle_list, sep="\n")


print("----------------------")
print("Aufgabe 14 - Vererbung")
print("----------------------")


class Car(Vehicle):
    def __init__(self, color, brand, construction_year, number_of_tyres, power,
                 num_of_doors, num_of_seats, warranty):
        self.number_of_doors = num_of_doors
        self.num_of_seats = num_of_seats
        self.warranty = warranty
        super().__init__(color, brand, construction_year, number_of_tyres, power)


class Motorbike(Vehicle):
    def __init__(self, color, brand, construction_year, number_of_tyres, power,
                 num_of_mirrors, bodykit, exhaust_type):
        self.num_of_mirrors = num_of_mirrors
        self.bodykit = bodykit
        self.exhaust_type = exhaust_type
        super().__init__(color, brand, construction_year, number_of_tyres, power)


class Truck(Vehicle):
    def __init__(self, color, brand, construction_year, number_of_tyres, power,
                 hanger_length, load_capacity, special_permit):
        self.hanger_length = hanger_length
        self.load_capacity = load_capacity
        self.special_permit = special_permit
        super().__init__(color, brand, construction_year, number_of_tyres, power)


"""
some = Truck("blue", "volvo", 1988, 18, 2500, 20, 7500, "g56n")
another = Motorbike("blue", "Suzuki", 1988, 2, 276, 2, "racer", "standard")

print("Hanger Length:", some.hanger_length)
print("Number of tyres:", some.number_of_tyres)
print("Capacity:", some.load_capacity)
print(some.usecase)

print("--------------------")
print("Mirrors:", another.num_of_mirrors)
print("Number of tyres:", another.number_of_tyres)
print("Bodykit:", another.bodykit)
print(another.usecase)

"""

print("----------------------")
print("Aufgabe 15 - Objekte und Dateneingabe")
print("----------------------")

headers = ["color", "brand", "construction_year", "number_of_tyres", "power",
           "num_of_doors", "num_of_seats", "warranty",
           "num_of_mirrors", "bodykit", "exhaust",
           "hanger_length", "load_capacity", "special_permit"]
df = pd.DataFrame(columns=headers)

df2 = df.copy()

counter = 0
vehicle_list_2 = []
while True:
    start = input("Would you like to register a vehicle? (Y/N): ")
    if start.lower() == "n":
        df.to_csv("vehicle_registration.csv")
        df3 = pd.DataFrame(vehicle_list_2, columns=headers)
        df3.to_csv("vehicle_registration_2.csv")
        print("----------df-----------")
        print(df3)
        break
    if start.lower() == "y":
        vehicle_type = input("What kind of Vehicle is it? (Car, Motorbike, Truck, unspecified): ")
        color = input("Color: ")
        brand = input("Brand: ")
        construction_year = input("Construction year: ")
        number_of_tyres = input("Number of tyres: ")
        power = input("Power (PS): ")

    if vehicle_type.lower() == "car":
        num_of_doors = input("Number of Doors: ")
        num_of_seats = input("Number of Seats: ")
        warranty = input("Warranty: ")

        car = Car(color, brand, construction_year, number_of_tyres,
                  power, num_of_doors, num_of_seats, warranty)

        vehicle_list_2.append([car.color, car.brand, car.construction_year, car.number_of_tyres,
                               car.power, car.number_of_doors, car.num_of_seats, car.warranty,
                               np.nan, np.nan, np.nan,
                               np.nan, np.nan, np.nan])

        new_entry = pd.DataFrame(
            {"color": [car.color], "brand": [car.brand], "construction_year": [car.construction_year],
             "number_of_tyres": [car.number_of_tyres], "power": [car.power],
             "number_of_doors": [car.number_of_doors], "num_of_seats": [car.num_of_seats], "warranty": [car.warranty]
             },
            index=[counter]
        )

    if vehicle_type.lower() == "motorbike":
        num_of_mirrors = input("Number of Mirrors: ")
        bodykit = input("Bodykit: ")
        exhaust = input("Exhaust: ")

        bike = Motorbike(color, brand, construction_year, number_of_tyres,
                         power, num_of_mirrors, bodykit, exhaust)

        vehicle_list_2.append([bike.color, bike.brand, bike.construction_year, bike.number_of_tyres,
                               bike.power,
                               np.nan, np.nan, np.nan,
                               bike.num_of_mirrors, bike.bodykit, bike.exhaust_type,
                               np.nan, np.nan, np.nan])

        new_entry = pd.DataFrame(
            {"color": [bike.color], "brand": [bike.brand], "construction_year": [bike.construction_year],
             "number_of_tyres": [bike.number_of_tyres], "power": [bike.power],
             "number_of_mirrors": [bike.num_of_mirrors], "bodykit": [bike.bodykit], "exhaust": [bike.exhaust_type]
             },
            index=[counter]
        )

    if vehicle_type.lower() == "truck":
        hanger_length = input("Hanger Length: ")
        load_capacity = input("Load Capacity: ")
        special_permit = input("Special Permit: ")

        truck = Truck(color, brand, construction_year, number_of_tyres,
                      power, hanger_length, load_capacity, special_permit)

        vehicle_list_2.append([truck.color, truck.brand, truck.construction_year, truck.number_of_tyres,
                               truck.power, np.nan, np.nan, np.nan,
                               np.nan, np.nan, np.nan,
                               truck.hanger_length, truck.load_capacity, truck.special_permit])

        new_entry = pd.DataFrame(
            {"color": [truck.color], "brand": [truck.brand], "construction_year": [truck.construction_year],
             "number_of_tyres": [truck.number_of_tyres], "power": [truck.power],
             "hanger_length": [truck.hanger_length], "load_capacity": [truck.load_capacity],
             "special_permit": [truck.special_permit]
             },
            index=[counter]
        )

    df = pd.concat([df, new_entry])
    # df2 = df.loc[len(df2)] = vehicle_list_2

    counter += 1
    print(*vehicle_list_2, sep="\n")


