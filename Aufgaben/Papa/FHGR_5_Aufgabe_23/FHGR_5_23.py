import os
from lxml import etree
from datetime import datetime
import nltk
from nltk.corpus import stopwords
import csv

# all of the element types in dblp
all_elements = ["article", "inproceedings", "proceedings", "book", "incollection", "phdthesis", "mastersthesis", "www"]

# Stopwords
nltk.download('stopwords')
stopwords_englisch = stopwords.words('english')
stopwords_german = stopwords.words('german')

# DBLP spezifische Stopwords zusätzlich
stopwords_dblp = ["home", "page", "using", "base", "based", "the", "an", "using",
                  "based", "on", "with", "via", "deep", "data", "de", "new", " - ", "-"]

# Suchresultat
keyword_counts = dict()

# load TOP 10
top10_path = 'U5_21_Keywords_TOP10.csv'

with open(top10_path, 'r', encoding='UTF-8-sig') as file:
    reader = csv.reader(file)
    res_top10 = {rows[0]: int(rows[1]) for rows in reader}

# alte file (Top10) löschen
for i in res_top10:
    try:
        os.remove('Export/U23_' + i + '.csv')
        os.remove('Export/U23_' + i + '.txt')
    except:
        print('File not found: ' + 'U23_' + i + '.csv')


def log_msg(message):
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), message)


def context_iter(dblp_path):
    """Create a dblp data iterator of (event, element) pairs for processing"""
    return etree.iterparse(source=dblp_path, dtd_validation=True, load_dtd=True,
                           remove_pis=True, remove_blank_text=True, remove_comments=True)  # required dtd


def clear_element(element):
    """Free up memory for temporary element tree after processing the element"""
    element.clear()
    while element.getprevious() is not None:
        del element.getparent()[0]


def fillcsv(keyword, titletext):
    # Save Excel .csv / pro Keyword
    with open('Export/' + 'U23_' + keyword + '.csv', 'a', encoding='UTF-8') as f:
        f.write(str(titletext) + '\n')
        # print(keyword + ': ' + titletext)

def filltxt(keyword, titletext):
    # Save als Text / pro Keyword
    with open('Export/' + 'U23_' + keyword + '.txt', 'a', encoding='UTF-8') as f:
        f.write(str(titletext) + '\n')
        # print(keyword + ': ' + titletext)

def splitFile(dblp_path):
    type_name = ['article', 'book', 'incollection', 'inproceedings' 'proceedings', 'phdthesis', 'mastersthesis', 'www']
    log_msg("PROCESS: Start parsing for {}...".format(str(type_name)))

    last_i = ''
    last_text = ''

    for _, elem in context_iter(dblp_path):
        if elem.tag in type_name:

            # ist ein Keyword im Titel vorhanden
            for a in elem.findall('title'):
                if a.text is not None:

                    mytext = a.text.lower()                         # umwandeln in Kleinbuchstaben
                    new_string2 = mytext.replace(".", " ")          # . entfernen
                    new_string2.replace(",", " ")                   # , entfernen
                    new_string2.replace(";", " ")                   # ; entfernen
                    new_string2.replace("-", " ")                   # - entfernen
                    new_string2.replace(" - ", " ")                 # - entfernen

                    split_list = new_string2.split()
                    for i in split_list:
                        if i in res_top10 and i not in stopwords_englisch and i not in stopwords_german and not i in stopwords_dblp:
                            keyword_counts[i] = keyword_counts.get(i, 0) + 1

                            # Hier müssen noch die Titels eingetragen werden, pro Keyword = Export
                            # print(i, ': ', a.text)

                            # ACHTUNG: kommt ein Keyword mehrfach im gleichen Titel vor, wird der Titel 2x exportiert
                            if not i == last_i and not a.text == last_text:
                                fillcsv(i, a.text)
                                filltxt(i, a.text)

                            # Titel wurde im Export eingetragen
                            last_i = i
                            last_text = a.text

        elif elem.tag not in all_elements:
            continue
        clear_element(elem)

    return keyword_counts


def main():
    dblp_path = '../DBLP/dblp.xml'
    save_path = 'U5_23_Keywords_Count10.csv'

    start_date_time = datetime.now()
    print('-------------------------------------------------------------')
    print("Start time: ", start_date_time.strftime("%Y-%m-%d %H:%M:%S"))
    print('-------------------------------------------------------------')

    try:
        context_iter(dblp_path)
        log_msg("LOG: Successfully loaded \"{}\".".format(dblp_path))
    except IOError:
        log_msg("ERROR: Failed to load file \"{}\". Please check your XML and DTD files.".format(dblp_path))
        exit()

    # load_stopwords()
    print('Stopwords englisch:', stopwords_englisch)
    print('Stopwords german:', stopwords_german)

    # Parse all Titles
    keyword_counts = splitFile(dblp_path)

    # Laufzeit
    end_date_time = datetime.now()
    diff_date_time = end_date_time - start_date_time

    # Ausgabe Console
    print('-------------------------------------------------------------')
    print("End time: ", end_date_time.strftime("%Y-%m-%d %H:%M:%S"))
    print("Duration: ", diff_date_time)
    print('-------------------------------------------------------------')

    # nur die Top-100für den Plot und Export .csv (sortiert)
    keyword_counts = dict(sorted(keyword_counts.items(), key=lambda x: x[1], reverse=True)[:10])

    # Save Excel .csv
    with open(save_path, 'w', encoding='UTF-8') as f:
        for key in keyword_counts.keys():
            f.write("%s, %s\n" % (str(key), keyword_counts[key]))


if __name__ == '__main__':
    main()
