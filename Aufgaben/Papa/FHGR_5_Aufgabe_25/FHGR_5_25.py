import os
from lxml import etree
from datetime import datetime
import csv

# all of the element types in dblp
all_elements = ["article", "inproceedings", "proceedings", "book", "incollection", "phdthesis", "mastersthesis", "www"]

keyword_pairs_counts = dict()

# load TOP 10
top10_pairs_path = 'U5_25_Keywords_TOP10_Pairs.csv'

with open(top10_pairs_path, 'r', encoding='UTF-8-sig') as file:
    reader = csv.reader(file)
    top10_pairs = {rows[0]: int(rows[1]) for rows in reader}


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


def barchart3D(dblp_path):
    type_name = ['article', 'book', 'incollection', 'inproceedings' 'proceedings', 'phdthesis', 'mastersthesis', 'www']
    log_msg("PROCESS: Start parsing for {}...".format(str(type_name)))

    for _, elem in context_iter(dblp_path):
        if elem.tag in type_name:

            # ist ein Keyword im Titel vorhanden
            for a in elem.findall('title'):
                if a.text is not None:

                    new_string2 = a.text.lower()                        # umwandeln in Kleinbuchstaben
                    new_string2.replace(".", " ")                       # . entfernen
                    new_string2.replace(",", " ")                       # , entfernen
                    new_string2.replace(";", " ")                       # ; entfernen
                    new_string2.replace("-", " ")                       # - entfernen
                    new_string2.replace(" - ", " ")                     # - entfernen

                    split_list = new_string2.split()
                    for i in split_list:
                        for tp in top10_pairs:
                            tp_split = tp.split()
                            substring1 = tp_split[0]
                            substring2 = tp_split[1]

                            if substring1 in split_list and substring2 in split_list:
                                # Treffer gefunden
                                keyword_pairs_counts[tp] = keyword_pairs_counts.get(tp, 0) + 1
                                # print('stop')


        elif elem.tag not in all_elements:
            continue
        clear_element(elem)

    return keyword_pairs_counts


def main():
    dblp_path = '../DBLP/dblp.xml'
    save_path = 'U5_25_Keywords_Pairs_Count.csv'

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

    # Parse all Titles
    keyword_pairs_counts_res = barchart3D(dblp_path)

    # Laufzeit
    end_date_time = datetime.now()
    diff_date_time = end_date_time - start_date_time

    # Ausgabe Console
    print('-------------------------------------------------------------')
    print("End time: ", end_date_time.strftime("%Y-%m-%d %H:%M:%S"))
    print("Duration: ", diff_date_time)
    print('-------------------------------------------------------------')

    # nur die Top-100für den Plot und Export .csv (sortiert)
    # keyword_pairs_counts_res = dict(sorted(keyword_pairs_counts_res.items(), key=lambda x: x[1], reverse=True)[:100])
    keyword_pairs_counts_res = sorted(keyword_pairs_counts_res.items())

    # Save Excel .csv
    with open(save_path, 'w', encoding='UTF-8') as f:
        for key in keyword_pairs_counts_res.keys():
            f.write("%s, %s\n" % (str(key), keyword_pairs_counts_res[key]))


if __name__ == '__main__':
    main()