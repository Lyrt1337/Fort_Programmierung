from lxml import etree
from datetime import datetime
import requests
import pandas as pd


# Function
def context_iter(temp_path):
    return etree.iterparse(source=temp_path)


def get_data(keyword):
    # Variables
    start_year = 2000
    end_year = 2023
    # keyword = "Machine Learning"

    search_string = ""

    for i in keyword.split(" "):
        search_string += i+"$"
    print("Searching by: ", search_string)
    key_counts = []

    # Search
    start_date_time = datetime.now()
    print('-------------------------------------------------------------')
    print("Start time: ", start_date_time.strftime("%Y-%m-%d %H:%M:%S"))
    print('-------------------------------------------------------------')

    print('--------------------------------------------')
    print('DBLP find keyword: ', keyword)
    print('---------------------------------------------')

    url = 'https://dblp.org/search/publ/api?q='
    num_of_hits = 1000
    starting_point = 0
    for i in range(start_year, end_year+1):

        page = requests.get(url + search_string + str(i))
        xml = page.content
        # print(xml)

        # XML temporär speichern
        f = open("dash_data/xml_api_temp.xml", "wb")
        f.write(xml)
        f.close()

        for _, elem in context_iter("dash_data/xml_api_temp.xml"):

            if elem.tag == 'hits':
                for item in elem.attrib.items():
                    # print(item[0], item[1])
                    if item[0] == 'total':
                        print('Total Found: ', item[1])
                        temp_res = (i, item[1])
                        key_counts.append(temp_res)
            if elem.tag == 'time':
                # Laufzeit in Milli...
                print('Duration (milliseconds): ', float(elem.text))
            elem.clear()

    # print('')
    # print(key_counts)

    # to DF
    cols = ["Year", "Count"]
    df = pd.DataFrame(key_counts, columns=cols)
    # print(df)
    df.to_csv(f"dash_data/{keyword}.csv")
    # with open(f"{keyword}.txt", "w") as f:
    #     f.write(str(key_counts))

    # Laufzeit
    end_date_time = datetime.now()
    diff_date_time = end_date_time - start_date_time

    # Ausgabe Console
    print('-------------------------------------------------------------')
    print("End time: ", end_date_time.strftime("%Y-%m-%d %H:%M:%S"))
    print("Duration: ", diff_date_time)
    print('-------------------------------------------------------------')
    # return key_counts


# get_data("Machine Learning")
