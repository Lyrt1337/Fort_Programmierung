# ----------------------------------------------------------------------
# 1. Verwenden sie das request - Modul.
# ----------------------------------------------------------------------
import requests
import json

# -------------------------------------------------------------------------------------------------
# 3. Verwenden sie die API unter "https://swapi.dev/api/", um die Daten dieses Charakters zu laden.
# -------------------------------------------------------------------------------------------------
url = "https://swapi.dev/api/"

"""
HTTP 200 OK
Content-Type: application/json
Vary: Accept
Allow: GET, HEAD, OPTIONS
{
    "people": "https://swapi.dev/api/people/",
    "planets": "https://swapi.dev/api/planets/",
    "films": "https://swapi.dev/api/films/",
    "species": "https://swapi.dev/api/species/",
    "vehicles": "https://swapi.dev/api/vehicles/",
    "starships": "https://swapi.dev/api/starships/"
}
"""
# -------------------------------------------------------------------------

print('')
print('-------------------------------------------------------------------------------------------')

print('Aufgabe 3: HTTP-API / FHGR Juni 2023, Gilomen Christian')

print('-------------------------------------------------------------------------------------------')

""""
Führen Sie in einem Jupyter Notebook die folgenden Aufgaben durch:

1. Verwenden sie das request - Modul.
2. Legen Sie in einer Variable die ID eines Star-Wars-Charakters fest.
3. Verwenden sie die API unter "https://swapi.dev/api/", um die Daten dieses Charakters zu laden.
4. Geben Sie den Namen des Charakters aus.
5. Werten Sie den Rückgabewert aus, um die Filme zu finden, in denen der gewählte Charakter mitspielt.
6. Laden Sie über die API diese Filme.
7. Geben Sie die Titel der Filme in einer Liste aus.
8. Erstellen sie auf "https://studio.apollographql.com/public/star-wars-swapi/variant/current/explorer"
   eine Abrage, mit der Sie dieselben Daten mit einer einzigen Abfrage holen können.
   Holen Sie dabei nur die minimal erforderlichen Felder ab.
9. Dokumentieren Sie desen Query im Jupyter-Notebook als mehrzeilige Zeichenkette.

"""

# ----------------------------------------------------------------------
# 2. Legen Sie in einer Variable die ID eines Star-Wars-Charakters fest.
# ----------------------------------------------------------------------
person = 1      # Luke Skywalker


print('')
# -------------------------------------------------------------------------------------------------
# 3. Verwenden sie die API unter "https://swapi.dev/api/", um die Daten dieses Charakters zu laden.
# -------------------------------------------------------------------------------------------------
resp_people = requests.get(url + "people/" + str(person))
resp_people_json = resp_people.json()
print('json:', resp_people_json)

"""
print("Print each key-value pair from JSON response")
for key, value in resp_people_json.items():
    print(key, ":", value)
"""

# Dictionary
dict_people = resp_people.json()
print('dict:', resp_people.json())
"""
# people alle Felder als Dictionary
print('Als Dictionary:', dict_people)
for k,v in dict_people.items():
    print(f"{k}:\t\t\t {v}")

print('')
"""

print('')

# ------------------------------------------
# 4. Geben Sie den Namen des Charakters aus.
# ------------------------------------------
print('4. Name des Charakters:')
print('  json => ',  resp_people_json["name"])
print('  dict => ',  dict_people.get('name'))
print('')

# ------------------------------------------------------------------------------------------------------
# 5. Werten Sie den Rückgabewert aus, um die Filme zu finden, in denen der gewählte Charakter mitspielt.
# (Liste films "file-link" aus people => zeigt direkt zum Film
# 6. Laden Sie über die API diese Filme.
# 7. Geben Sie die Titel der Filme in einer Liste aus.
# ------------------------------------------------------------------------------------------------------
print('5./6./7. spielt in folgenden Filmen (Titel) mit:')
print ('')

list_title = []

str_json = json.dumps(resp_people_json['films'])
list_json = json.loads(str_json)

for film in list_json:
    resp_film = requests.get(film)          # API film = url aus people/films
    resp_film_json = resp_film.json()
    # print('Film json:', resp_film.json())
    print('   json =>', film, resp_film_json["title"])
    list_title.append(resp_film_json["title"])
print('')
# liste der gefundenen Film-Titel
print('   json => Titel-Liste: ', list_title)

print ('')

list_title = []
list_filme = dict_people.get('films')
for film in list_filme:
    resp_film = requests.get(film)          # API film = url aus people/films
    resp_film_json = resp_film.json()
    dict_film = resp_film.json()
    print('   dict =>', film, dict_film.get("title"))
    list_title.append(dict_film.get("title"))
print('')
# liste der gefundenen Film-Titel
print('   dict => Titel-Liste: ', list_title)

""""
# Film alle Felder als Dictionary
dict_film = resp_film.json()
print('Als Dictionary:', dict_film)
for k,v in dict_film.items():
    print(f"{k}:\t\t\t {v}")

print('   ',  dict_film.get('title'))

"""
# print('')

# -------------------------------------------------------------------------------------------------------
# 8. Erstellen sie auf "https://studio.apollographql.com/public/star-wars-swapi/variant/current/explorer"
#    eine Abrage, mit der Sie dieselben Daten mit einer einzigen Abfrage holen können.
#    Holen Sie dabei nur die minimal erforderlichen Felder ab.
# -------------------------------------------------------------------------------------------------------
# Query: person(id: "cGVvcGxlOjE=") = Luke Skywalker
# (Generiert über den Link in der Aufgabe 3/Teil 8)

"""
query Person {
    person(id: "cGVvcGxlOjE=") {
    name
      filmConnection {
        films {
          title
        }
      }
    }
}
"""
print('')
print('')
print('')
print('Grüassli Papa ;-)')