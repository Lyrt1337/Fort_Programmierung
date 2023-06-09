import requests
import json
url = "https://swapi.dev/api/"

person = 1

# response = requests.get(url + "people/20")
# print(response.json())

while True:
    response = requests.get(url + "people/" + str(person))
    print(response.json())
    person +=1

