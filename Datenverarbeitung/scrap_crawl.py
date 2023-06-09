from bs4 import BeautifulSoup

with open("data/web/index.html")as f:
    document = f.read()

soup = BeautifulSoup(document, "html.parser")
print([i.text for i in soup.select(".movies td")])
print([i.select("td") for i in soup.select(".movies tr:has(td)")])

print(
    [{"title": i.select_one("td:first-child").text,
      "year": int(i.select_one("td:last-child").text)
      }
     for i in soup.select(".movies tr:has(td)")
     ]
)

