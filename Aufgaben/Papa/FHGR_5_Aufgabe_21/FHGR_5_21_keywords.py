from lxml import etree
from datetime import datetime
import nltk
from nltk.corpus import stopwords

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

def load_stopwords():
    print('-----------------')
    print('STOPWORDS: (nltk)')
    print('-----------------')

    # Download der Liste
    nltk.download('stopwords')

    # In den Stopword kann für diverse Sprachen eine Liste erstellt werden
    stopwords_englisch = stopwords.words('english')
    stopwords_german = stopwords.words('german')
    # usw.

    print('Stopwords englisch:', stopwords_englisch)
    print('Stopwords german:', stopwords_german)

    print('-----------------')


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

def readDataToList(dblp_path):
    type_name = ['article', 'book', 'incollection', 'inproceedings' 'proceedings', 'phdthesis', 'mastersthesis', 'www']
    log_msg("PROCESS: Start parsing for {}...".format(str(type_name)))

    for _, elem in context_iter(dblp_path):
        if elem.tag in type_name:

            # ist ein Keyword im Titel vorhanden (Liste ist vorher bereinigt Stop-Words ausgeschlossen)
            for a in elem.findall('title'):
                if a.text is not None:

                    if search_string == '*':
                        # Nur wenn über alle Titels (Wörter) gesucht werden soll

                        mytext = a.text.lower()                             # umwandeln in Kleinbuchstaben
                        new_string2 = mytext.replace(".", " ")              # . entfernen
                        new_string2.replace(",", " ")                       # , entfernen
                        new_string2.replace(";", " ")                       # ; entfernen
                        new_string2.replace("-", " ")                       # - entfernen
                        new_string2.replace(" - ", " ")                     # - entfernen

                        split_list = new_string2.split()

                        for i in split_list:
                            if  i not in stopwords_englisch and i not in stopwords_german and not i in stopwords_dblp:
                                if i == '-':
                                    print('stop')

                                keyword_counts[i] = keyword_counts.get(i, 0) + 1
                    else:
                        # Nur wenn ein Such-Satz, Wort eingegeben wurde
                        split_list = a.text.split()
                        for i in split_list:
                            if i in input_all_keywords:
                                keyword_counts[i] = keyword_counts.get(i, 0) + 1


        elif elem.tag not in all_elements:
            continue
        clear_element(elem)

    return keyword_counts

def main():

    dblp_path = '../DBLP/dblp.xml'
    save_path = 'U5_21_Keywords_TOP100.csv'

    global all_keywords
    global search_string

    # Wonach willst du suchen ?
    search_string = input('Search in DBLP titles (whole sentence or "*"): ')
    if search_string is None or search_string == '':
        log_msg("LOG: no input for search, Exit \"{}\".".format(dblp_path))
        exit()

    # print('OK, ich suche nach: ' + search_string)
    global input_all_keywords

    # Stop-Words für die Suche bereinigen, und Duplikate entfernen
    if not search_string == '*':   # Suche nach allen Keywords aus den Titeln

        # alles in Kleinbuchstaben
        search_string_lower = search_string.lower()      # umwandeln in Kleinbuchstaben
        search_string_lower.replace(".", " ")           # . entfernen
        search_string_lower.replace(",", " ")           # , entfernen
        search_string_lower.replace(";", " ")           # ; entfernen
        search_string_lower.replace("-", " ")           # - entfernen
        search_string_lower.replace(" - ", " ")         # - entfernen

        # Suchstring in Wörter splitten
        input_all_keywords = search_string_lower.split()

        for i in stopwords_englisch:
            for y in input_all_keywords:
                if y == i:
                    input_all_keywords.remove(i)

        for i in stopwords_german:
            for y in input_all_keywords:
                if y == i:
                    input_all_keywords.remove(i)

        for i in stopwords_dblp:
            for y in input_all_keywords:
                if y == i:
                    input_all_keywords.remove(i)
        print('-------------------------------------------------------------')
        print("")
        print("Search Keyword(s): ", input_all_keywords)
        print("")

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

    # Parse the keywords in titles
    # load_stopwords()
    print('Stopwords englisch:', stopwords_englisch)
    print('Stopwords german:', stopwords_german)

    # Parse all Titles
    keyword_counts = readDataToList(dblp_path)

    # Laufzeit
    end_date_time = datetime.now()
    diff_date_time = end_date_time - start_date_time

    # Ausgabe Console
    print('-------------------------------------------------------------')
    print("End time: ", end_date_time.strftime("%Y-%m-%d %H:%M:%S"))
    print("Duration: ", diff_date_time)
    print('-------------------------------------------------------------')

    # nur die Top-100 für den Plot und Export .csv (sortiert)
    res_top100 = dict(sorted(keyword_counts.items(), key=lambda x: x[1], reverse=True)[:100])

    # Save Excel .csv
    with open(save_path, 'w', encoding='UTF-8') as f:
        for key in res_top100.keys():
            try:
                f.write("%s, %s\n" % (str(key), res_top100[key]))
            except:
                print('Fehler in: ', str(key), res_top100[key])

if __name__ == '__main__':
    main()