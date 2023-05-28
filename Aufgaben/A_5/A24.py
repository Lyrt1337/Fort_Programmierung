"""
-------------------------
Aufgabenblatt_5 Fort.Prog
Aufgabe 24
Autor: Christian Gilomen
Datum: 17.05.2023
-------------------------
"""
import re
from lxml import etree as ET


class Author:
    def __init__(self, name, orcid, first_publication_year):
        self.name = name
        self.orcid = orcid
        self.first_publication_year = first_publication_year
        self.publications = []

    def add_publication(self, publication):
        self.publications.append(publication)

    def generate_keywords(self):
        keywords = []
        for publication in self.publications:
            if publication['title'] is not None:
                title = publication['title'].strip()
                publication_keywords = re.findall(r'\b\w+\b', title)
                keywords.extend(publication_keywords)
        return keywords


def read_data(file_path='../dataset/dblp.xml'):
    authors = {}

    ctx = ET.iterparse(open(file_path, mode="rb"), events=('start', 'end'), load_dtd=True, remove_pis=True,
                       remove_blank_text=True, remove_comments=True)

    for event, elem in ctx:
        if elem.tag == 'author' and event == 'start':
            name = elem.text
            if name is not None:
                name = name.strip()
            orcid = elem.get('orcid')
            first_publication_year = elem.get('first_publication_year')
            if first_publication_year is not None:
                first_publication_year = int(first_publication_year)
            author = authors.get(name)

            if author is None:
                author = Author(name, orcid, first_publication_year)
                authors[name] = author

            elem.clear()
        elif elem.tag == 'title' and event == 'start':
            title = elem.text
            if title is not None:
                title = title.strip()
            publication = {'title': title}
            author.add_publication(publication)
            elem.clear()

    return authors


def top_authors_by_publications(authors, n=10):
    sorted_authors = sorted(authors.values(), key=lambda x: len(x.publications), reverse=True)
    return sorted_authors[:n]


def top_authors_by_keywords(authors):
    sorted_authors = sorted(authors.values(), key=lambda x: len(x.generate_keywords()), reverse=True)[:10]
    print("Top 10 Autoren nach Anzahl der Keywords:")
    for author in sorted_authors:
        print(f"Name: {author.name}, Keywords: {len(author.generate_keywords())}")
    return sorted_authors


# Beispielverwendung:
dataset_path = '../dataset/dblp.xml'
authors = read_data(dataset_path)

top_authors_publications = top_authors_by_publications(authors)
top_authors_keywords = top_authors_by_keywords(authors)

print("Top 10 Autoren nach Anzahl der Publikationen:")
for author in top_authors_publications:
    print(f"Name: {author.name}, Publikationen: {len(author.publications)}")

print("\nTop 10 Autoren nach Anzahl der Keywords:")
for author in top_authors_keywords:
    keywords = author.generate_keywords()
    keyword_list = ", ".join([f"{keyword}: {keywords.count(keyword)}" for keyword in set(keywords)])
    print(f"Name: {author.name}, Keywords: {keyword_list}")
