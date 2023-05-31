import dblp
import pandas as pd
from lxml import etree
import requests
#do a simple author search for michael ley
search_key = '"Machine$Learning$"$'
authors = dblp.search(search_key + "&h=0")

# authors = 'https://dblp.org/search/publ/api?q=' + search_key + '&h=2'
# page = requests.get(authors)
# xml = page.content
# print(xml)

# authors2 = dblp.search(search_key + "&h=0")
# authors3 = dblp.search(search_key + "&h=0")
# michael = authors[0]

# df = pd.DataFrame(authors)
# print(authors.head(5))
authors.to_csv("out.csv")
# authors2.to_csv("out2.csv")
# authors3.to_csv("out3.csv")

# print(len(michael.publications))

# a = dblp.get_pub_data(authors)
# print(a)