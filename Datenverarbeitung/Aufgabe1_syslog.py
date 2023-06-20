import re
from datetime import datetime

akt_year = datetime.now().year
months = {"Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "Mai": 5, "Jun": 6,
          "Jul": 7, "Aug": 8, "Sep": 9, "Okt": 10, "Nov": 11, "Dec": 12}

with open("data/syslog", encoding="utf-8") as f:
    syslog_data = f.read()

syslog_line = re.split(r"\n", syslog_data)

sys_list_dict = [
    {"Datum": re.findall(r"^((?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s\d\d?|$)", line)[0],
     "Uhrzeit": re.findall(r"\d\d:\d\d:\d\d|$", line)[0],
     "Rechnername": re.findall(r".{3}-.{3}|$", line)[0],
     "Prozessname": re.split(r"\[|]|:", re.findall(r"\b[A-za-z0-9\-.]{3,}\b\[?\d*?]?:+|$", line)[0])[0],
     "Numerische Prozess-ID": "".join(re.split(r"\D",
                                                  re.findall(r"\s\b[A-za-z0-9\-.]{3,}\b\[?\d*?]?:+|$", line)[0])),
     "Nachricht": re.findall(r"(?<=\D:\s).*|$", line)[0]
    }
    for line in syslog_line]

# convert "Datum" and "Uhrzeit" to datetime-object
for i in sys_list_dict:
    if i["Uhrzeit"] == "":
        sys_list_dict.remove(i)
    else:
        h, m, s = i["Uhrzeit"].split(":")
        i["Datum"] = datetime(akt_year, months[i["Datum"].split(" ")[0]],
                              int(i["Datum"].split(" ")[1]), int(h), int(m), int(s)).strftime('%Y/%m/%d %H:%M:%S')
    del i["Uhrzeit"]


# print line by line for nicer view

for i in sys_list_dict:
    print(i)
