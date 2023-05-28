"""
-------------------------
Aufgabenblatt_5 Fort.Prog
Aufgabe 21
Autor: Christian Gilomen
Datum: 17.05.2023
-------------------------
"""
from lxml import etree as ET
import nltk
from nltk.corpus import stopwords
import re
from datetime import datetime

nltk.download('stopwords')
languages = ["English", "German", "French"]

# Set to store all stopwords
stop_words = set()

# Iterate over each language and add its stopwords to the set
for lang in set(languages):
    stop_words.update(stopwords.words(lang.lower()))

# results
keyword_counts = dict()
keyword_list = []


def readDataToList(file_path="dataset/dblp.xml"):
    start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Start time: {start_time}")
    parsed = ET.iterparse(open(file_path, mode="rb"), events=('start', 'end'), load_dtd=True, remove_pis=True,
                          remove_blank_text=True, remove_comments=True)

    # iterate and filter stopwords
    for event, elem in parsed:
        if elem.tag == 'title' and event == 'start':
            title = elem.text
            if title is not None:
                text = re.findall(r'\b\w+\b', title.lower())
                filtered_words = [word for word in text if word not in stop_words]

                # counting words
                for word in filtered_words:
                    word = word.title()
                    if keyword_counts.get(word) is None:
                        keyword_counts[word] = 1
                    else:
                        keyword_counts[word] += 1

        elem.clear()
    # results sorted by value
    res_top100 = sorted(keyword_counts.items(), key=lambda x: x[1], reverse=True)

    with open('keywords/Keywords.txt', 'w', encoding="UTF-8") as writer:
        for word, count in res_top100:
            writer.write(f'{word}: {count}\n')
    end_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"End Time: {end_time}")
    return res_top100


readDataToList()
