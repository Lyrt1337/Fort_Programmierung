# ----------------------------------------------------------------

# Klasse Author definieren
class author:

    def __init__(self, orcid, name, publications):
        author.orcid = orcid  # primary key
        author.name = name
        author.publications = []


    # mögliche Methoden in der Klasse
    def myfunc(author):
        print("Function myfunc => Authors Orcid / Name: " + author.orcid + ', ' + author.name)
        return None

# appending instances to list
# list.append(author("xxx-yyy-zzz", 'Christian', []))
# list.append(author("aaa-bbb-ccc", 'Manfred', []))

# Accessing object value using a for loop
# for obj in list:
#     print(obj.orcid, obj.name, sep=' ')

# creating list
authors = []
# ----------------------------------------------------------------
# Authoren hinzufügen (Liste)
# ----------------------------------------------------------------
p1 = author("xxx-yyy-zzz", 'Christian', ["Titel 1", "Titel 2"])
authors.append(p1)


p2 = author("aaa-bbb-ccc", 'Manfred', ["Titel 9", "Titel 8"])
authors.append(p2)

print(p1.name)
print(p2.name)

# author1 = author
# author1.orcid = 'xxx-yyy-zzz'
# author1.name = 'Christian'
# author1.publications = ["Titel 1", "Titel 2"]

# author.list.append(author1)

# author2 = author
# author2.orcid = 'aaa-bbb-ccc'
# author2.name = 'Manfred'
# author2.publications = ["Titel 9", "Titel 8"]

# author.list.append(author2)

# ----------------------------------------------------------------
# Authoren ausgeben
# ----------------------------------------------------------------
for obj in list:
    print(obj.orcid, obj.name)
    print(obj.publications)
    print('')
    print(author.myfunc(obj))
    print('')

# ----------------------------------------------------------------

