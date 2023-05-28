import csv
import matplotlib.pyplot as plt
import mplcursors

# ----------------------------------------------------------------------------
# Import Excel .csv (aus FHGR_5_25.py => U5_25_Keywords_Pairs_Count.csv)
# ----------------------------------------------------------------------------
top100_path = 'U5_25_Keywords_Pairs_Count.csv'

with open(top100_path, 'r') as file:
    reader = csv.reader(file)
    res_top100 = {rows[0]: int(rows[1]) for rows in reader}

# ----------------------------------------------------------------------------

font = {'family': 'arial',
        'color': 'blue',
        'weight': 'bold',
        'size': 10,
        }
# ----------------------------------------------------------------------------

# labels = string.ascii_uppercase[:9]
labels = list(res_top100.keys())  # Keywords X
values = list(res_top100.values())  # Values Y

plt.figure("Uebung5_FortProg / Aufgabe 22 / Top100 aus Aufgabe 21 / Christian Gilomen")  # Fenstertitel
plt.title('DBLP: Keywords - Top100', fontdict=font)  # Plottitel
plt.xlabel('Keywords (hover or zoom)', fontdict=font)  # Titel x-Achse
plt.ylabel('Frequencies', fontdict=font)  # Titel y-Achse

plt.bar(range(len(res_top100)), values)  # Plot Range
cursor = mplcursors.cursor(hover=mplcursors.HoverMode.Transient)  # Hover Cursor (ToolTip)


@cursor.connect("add")
def on_add(sel):
    x, y, width, height = sel.artist[sel.index].get_bbox().bounds

    xn = str(labels[sel.index])
    yn = str(values[sel.index])

    sel.annotation.set(text=xn + ': ' + yn)
    sel.annotation.xy = (x + width / 2, y + height)


plt.show()
