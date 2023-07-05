# A 7, 8, 9
import numpy as np
import random as rnd

class Flight:
    usecase = "travel"

    def __init__(self, Flughafen, Flugnummer, Fluggesellschaft, Flugdauer, Zielflughafen):
        self.Flughafen = Flughafen
        self.Flugnummer = Flugnummer
        self.Fluggesellschaft = Fluggesellschaft
        self.Flugdauer = Flugdauer
        self.Zielflughafen = Zielflughafen

    def flugpreis(self, PreisCHF):
        Preis = PreisCHF * 0.98
        print(f"Flug {self.Flugnummer} von {self.Flughafen} nach {self.Zielflughafen} kostet {Preis} Euro ")

    def delay(self, verspaetung):
        print(f"Der Flug von {self.Flughafen} nach {self.Zielflughafen}, Flugnummer {self.Flugnummer}"
              f"wird sich um {verspaetung} verspäten")

    def __repr__(self):
        rep = Flight(' + self.Flughafen + ', ' + str(self.Flugnummer) + ', ' + \
              str(self.Fluggesellschaft) + ', ' + str(self.Flugdauer) + ', ' + str(self.Zielflughafen)')
        return rep

# mögliche Klassenattribute: travel, transport
# instanzattribute sind: Flughafen, Flugnummer, Fluggesellschaft, Flugdauer, Zielflughafen
# weitere Instanzattribute: Preis, Flugzeugtyp, max. Reisegeschwindigkeit


flight_list = []


def create_flight_list(num_of_flights):
    for i in range(1, num_of_flights + 1):
        moegliche_Flughafen = ["Zürich", "Amsterdam", "Lisabon", "Rom", "Innsbruck", "Berlin", "New York"]
        Flughafen = np.random.choice(moegliche_Flughafen)
        Flugnummer = rnd.randint(1, 3000)
        Fluggesellschaften = ["Swiss", "Easy-Jet", "Lufthansa"]
        Fluggesellschaft = np.random.choice(Fluggesellschaften)
        Flugdauer = str(rnd.randint(30, 720)) + "min"
        Zielflughafen = np.random.choice(moegliche_Flughafen)

        new_flight = Flight(Flughafen, Flugnummer,
                              Fluggesellschaft, Flugdauer, Zielflughafen)

        flight_list.append([new_flight.Flughafen, new_flight.Flugnummer, new_flight.Fluggesellschaft,
                         new_flight.Flugdauer, new_flight.Zielflughafen])

    return flight_list

vehicle_list = create_flight_list(12)
print(*flight_list, sep="\n")

def writeFlightFile():
    with open("Flight_list", "w") as f:
        f.write(repr(Flight))
