
from lxml import etree
from datetime import datetime
import requests
import pandas as pd


def context_iter(temp_path):
    return etree.iterparse(source=temp_path)


# Du suchst nach was ?
# keyword = input('Gib ein Keyword ein: ')
keyword = "Machine$Learning$"

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
page = requests.get(url + keyword + f'&h={num_of_hits}' + f"&f={starting_point}")
xml = page.content
# print(xml)

# XML temporär speichern
f = open("myxmlfile_temp.xml", "wb")
f.write(xml)
f.close()

for _, elem in context_iter('myxmlfile_temp.xml'):

    if elem.tag == 'hits':
        for item in elem.attrib.items():
            # print(item[0], item[1])
            if item[0] == 'total':
                print('Total Found: ', item[1])
    if elem.tag == 'time':
        # Laufzeit in Milli...
        print('Duration (milliseconds): ', float(elem.text))

print('')

# cols = ["authors", "year"]
df = pd.read_xml("myxmlfile_temp.xml")
df.to_csv("testing_dataframe.csv")
# print(df.head(20))
# Laufzeit
end_date_time = datetime.now()
diff_date_time = end_date_time - start_date_time

# Ausgabe Console
print('-------------------------------------------------------------')
print("End time: ", end_date_time.strftime("%Y-%m-%d %H:%M:%S"))
print("Duration: ", diff_date_time)
print('-------------------------------------------------------------')

