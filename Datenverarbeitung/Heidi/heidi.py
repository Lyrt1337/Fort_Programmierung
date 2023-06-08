import pandas as pd
import re

with open("heidi.md", "r", encoding="utf-8") as f:
    heidi_data = f.read()

# print(heidi_data)

print(len(re.findall("Heidi", heidi_data)))

# alle Buchstaben
print(len(re.findall(r"\w", heidi_data)))

fliesstext = "".join(re.findall(r"\w", heidi_data))
# print(fliesstext)

# Zeichenauswahl
print(len(re.findall(r"[A-ZÄÖÜ]", heidi_data)))

# Anzahl Punkte
print(len(re.findall(r"[\.]", heidi_data)))

# Anzahl Zeilenumbrüche
print(len(re.findall(r"[\n]", heidi_data)))

# Anzahl Wörter mit 5 Buchstaben
print(len(re.findall(r"\b\w{5}\b", heidi_data)))

# Anzahl Wörter Doppelkonsonanten
print(len(re.findall(r"([b-df-hj-np-tv-z])\1", heidi_data)))

# Überschriften
print(len(re.findall(r"^#.*$", heidi_data, re.MULTILINE)))
print(*re.findall(r"^#.*$", heidi_data, re.MULTILINE), sep="\n")

# Anzahl Leerzeilen
print(len(re.findall(r"^$", heidi_data, re.MULTILINE)))
