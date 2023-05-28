"""
-------------------------
Aufgabenblatt_5 Fort.Prog
Aufgabe 25
Autor: Christian Gilomen
Datum: 17.05.2023
-------------------------
"""
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
import re
from lxml import etree as ET

path = "dataset/dblp.xml"
data = "keywords/Keywords.txt"

df = pd.read_csv(data, sep=':', names=['Keyword', 'Count'], nrows=10)

keywords = []
for i in df["Keyword"]:
    keywords.append(i.lower())
# print(df["Keyword"])
# print(".......")
# print(keywords)

# set up the figure and axes
x_data = np.arange(len(keywords))
y_data = np.arange(len(keywords))
xx, yy = np.meshgrid(x_data, y_data)
x, y = xx.ravel(), yy.ravel()

bottom = np.zeros_like(len(keywords)**2)
width = depth = 1

parsed = ET.iterparse(open(path, mode="rb"), events=('start', 'end'), load_dtd=True, remove_pis=True,
                      remove_blank_text=True, remove_comments=True)

def make_pairs(keywords):
    pair_list = []
    for i in range(0, len(keywords)):
        for j in range(0, len(keywords)):
            temp = [keywords[j], keywords[i], 0]
            pair_list.append(temp)
    return pair_list


# append pair-list with value = [[a, a, 1], [a, b, 2], ...]
def add_values(pair_list):
    complete_list = pair_list
    for event, elem in parsed:
        if elem.tag == 'title' and event == 'start':
            title = elem.text
            if title is not None:
                text = re.findall(r'\b\w+\b', title.lower())
                for i in range(len(complete_list)):
                    if complete_list[i][0] in text and complete_list[i][1] in text:
                        complete_list[i][2] += 1
        elem.clear()
    return complete_list


# take z values from complete list [[a, a, 1], [a, b, 2], ...]
def get_z_values(complete_list):
    z_values = []
    for i in range(len(complete_list)):
        z_values.append(complete_list[i][2])
    return z_values


# plot
def plot_3d_bars(x, y, bottom, width, depth, z_values):
    cmap = plt.colormaps.get_cmap('jet')  # Get desired colormap - you can change this!
    max_height = np.max(z_values)  # get range of colorbars so we can normalize
    min_height = np.min(z_values)
    # scale each z to [0,1], and get their rgb values
    rgba = [cmap((k - min_height) / max_height) for k in z_values]

    plt.figure("3D Barchart")
    ax = plt.axes(projection="3d")
    ax.bar3d(x, y, bottom, width, depth, z_values, shade=True, color=rgba, zsort="average")
    ax.set_title(f"Top {len(keywords)} Keyword-Pairs")
    ax.set_xlabel("x", labelpad=12)
    ax.set_ylabel("y", labelpad=12)
    ax.set_zlabel("z", labelpad=12)
    ax.set_xticks(x_data + 0.5)
    ax.set_yticks(y_data + 0.5)
    ax.set_xticklabels(keywords, rotation=0)
    ax.set_yticklabels(keywords, rotation=0)

    # annotation on every bar
    z_index = 0
    for i in range(1, len(keywords)+1):
        for x_1, y_1, z_1 in zip(xx[i-1], yy[i-1], z_values):
            label = f"{z_values[z_index]}"
            ax.text(x_1+0.5, y_1+0.5, z_values[z_index]+1, label,
                    horizontalalignment="center",
                    verticalalignment="center",
                    rotation="vertical"
                    )
            z_index += 1

    plt.show()


start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(f"Start time: {start_time}")

pairs = make_pairs(keywords)
complete_list = add_values(pairs)
z_values = get_z_values(complete_list)
plot_3d_bars(x, y, bottom, width, depth, z_values)

end_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(f"End Time: {end_time}")
