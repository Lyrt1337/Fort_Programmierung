"""
-------------------------
Aufgabenblatt_5 Fort.Prog
Aufgabe 23
Autor: Christian Gilomen
Datum: 17.05.2023
-------------------------
"""
import pandas as pd
from datetime import datetime
from lxml import etree as ET

path = "dataset/dblp.xml"
data = "keywords/Keywords.txt"
df = pd.read_csv(data, sep=':', names=['Keyword', 'Count'], nrows=10)
read_titles = None


def splitFile(file_path):
    start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Start time: {start_time}")
    parsed = ET.iterparse(open(file_path, mode="rb"), events=('start', 'end'), load_dtd=True, remove_pis=True,
                          remove_blank_text=True, remove_comments=True)

    for event, elem in parsed:
        if elem.tag == 'title' and event == 'start':
            if elem.text is not None:
                for i in df["Keyword"]:
                    if i in elem.text:
                        with open(f"splitFiles/{i}.txt", "a+", encoding="UTF-8") as f:
                            f.write(f"{elem.text}\n")
        elem.clear()

    end_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"End Time: {end_time}")


splitFile(path)
