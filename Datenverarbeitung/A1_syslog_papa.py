# Datenverarbeitung, Aufgabe_1, Teil 1, syslog
import re
from datetime import datetime
import time
date_pattern = ''
time_pattren = r'\d\d:\d\d:\d\d'     # oder r"\d\d:\d\d:\d\d", mit r geht es nicht...

# aktuelles Jahr ermitteln (year)
print('')
currentDateTime = datetime.now()
date = currentDateTime.date()
year = date.strftime("%Y")
print(f"Current Year => {year}")
print('')

# input-file
file = open("data/syslog", "r", encoding='UTF-8')
for zeile in file:

    # -------------------------------------------
    # Datum (Apr 17)
    # -------------------------------------------
    print('-- nur Datum')
    # alle Monatsnamen (Kurz) + Leerschlag + 2 Ziffern
    date_pattern = re.compile(r"((?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Sept|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)\s\d\d)")

    # x = re.search(date_pattern, zeile)
    # print(x)

    # r1 ist eine Liste mit allen Match-Werten (pattern)
    r1 = re.findall(date_pattern, zeile)
    for d in r1:
        # print(d)

        sdatetime = d + ' ' + year

        # Datum als Object
        dDate = datetime.strptime(sdatetime, '%b %d %Y')
        print(dDate.strftime("%b %d %Y"))

    # -------------------------------------------
    # Zeit (06:48:59)
    # -------------------------------------------
    print('-- nur Zeit')

    time_pattern = re.compile(r"\d\d:\d\d:\d\d")

    # <re.Match object; span=(7, 15), match='06:48:59'>
    # x = re.search(time_pattern, zeile)
    # print(x)

    # r1 ist eine Liste mit allen Match-Werten (pattern)
    r1 = re.findall(time_pattern, zeile)
    for d in r1:
        print(d)

        # funktioniert nicht ganz, Stunden unter 10 werden einstellig ausgegeben !
        time_obj = time.strptime(d, '%H:%M:%S')
        print(str(time_obj.tm_hour) + ":" + str(time_obj.tm_min) + ":" + str(time_obj.tm_sec))


    # -------------------------------------------------
    # Datum (Apr 17) + aktuelles Jahr + Zeit (06:48:59)
    # -------------------------------------------------
    print('-- Datum und Zeit')
    date_time_pattern = re.compile(r"((?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Sept|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)\s\d\d\s\d\d:\d\d:\d\d)")
    r1 = re.findall(date_time_pattern, zeile)

    for d in r1:
        print(d)

        # mit aktuellem Jahr verbinden
        dDateTime = str(d[0:6]) + ' ' + str(year) + ' ' + str(d[7:len(d)])
        print(dDateTime)

        # Datum/Zeit als Object
        dDateObject = datetime.strptime(dDateTime, '%b %d %Y %H:%M:%S')
        print(dDateObject)
        print(dDateObject.strftime("%b %d %Y %H:%M:%S"))

    print('')