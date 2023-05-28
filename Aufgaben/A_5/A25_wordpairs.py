import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
import re
from lxml import etree as ET

path = "dataset/dblp.xml"
data = "keywords/Keywords.txt"

df = pd.read_csv(data, sep=':', names=['Keyword', 'Count'], nrows=3)

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


start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(f"Start time: {start_time}")

pairs = make_pairs(keywords)
complete_list = add_values(pairs)


with open('keywords/wordpairs.txt', 'w', encoding="UTF-8") as w:
    w.write(str(complete_list))

end_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(f"End Time: {end_time}")
