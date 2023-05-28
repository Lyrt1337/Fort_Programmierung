import csv
import math
import mplcursors
import numpy as np
import matplotlib.pyplot as plt
plt.close("all")

keys = []
values = []

# ----------------------------------------------------------------------------
# Import Excel .csv (aus FHGR_5_25.py => U5_25_Keywords_Pairs_Count.csv)
# ----------------------------------------------------------------------------
top100_path = 'U5_25_Keywords_Pairs_Count.csv'

with open(top100_path, 'r') as file:
    reader = csv.reader(file)
    res_top100 = {rows[0]: int(rows[1]) for rows in reader}

for [k, v] in res_top100.items():
    print(f"{k}: {v}")

    # Liste aller Keys
    keys.append(k)

    # Liste aller Values
    values.append(v)

# ----------------------------------------------------------------------------

# set up the figure and axes
fig = plt.figure()
# ax1 = fig.add_subplot(121, projection='3d')
# ax2 = fig.add_subplot(122, projection='3d')
ax3 = fig.add_subplot(projection="3d")
# fake data

# x_wurzel = int(math.sqrt(len(res_top100)))

# x ist die Anzahl der x-werte
x_data = np.arange(9)

# x ist die Anzahl der y-werte
y_data = np.arange(5)

xx, yy = np.meshgrid(x_data, y_data)
x, y = xx.ravel(), yy.ravel()


top = values

# top = x * y
bottom = np.zeros_like(top)
width = depth = 1
# print(np.zeros_like(top))

# ax1.bar3d(x, y, bottom, width, depth, top, shade=True)
# ax1.set_xlabel("x")
# ax1.set_ylabel("y")
# ax1.set_zlabel("z")
# ax1.set_title('Shaded')
#
# ax2.bar3d(x, y, bottom, width, depth, top, shade=False)
# ax2.set_title('Not Shaded')


ax3.bar3d(x, y, bottom, width, depth, top, shade=True)
ax3.set_title('Shaded')

# cursor = mplcursors.cursor
# cursor = mplcursors.cursor(hover=mplcursors.HoverMode.Transient)  # Hover Cursor (ToolTip)




def hover(event):
    # print('stop')
    print(event)

    # if fig.canvas.widgetlock.locked():
    #    # Don't do anything if the zoom/pan tools have been enabled.
    #    return

    # fig.canvas.set_cursor(
    #    event.inaxes.cursor_to_use if event.inaxes else Cursors.POINTER)

# cursor(hover=True)
fig.canvas.mpl_connect('motion_notify_event', hover)

# pick_event_method
# def pick_event_method(event):
   # print('stop')
   # ind = event.ind[0]
   # x, y, z = event.artist._offsets3d
   # print(x[ind], y[ind], z[ind])

# Connect pick_event_method with pick_event
# fig.canvas.mpl_connect('pick_event', pick_event_method)

plt.show()