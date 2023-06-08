import json
from jsonpath_ng.ext import parse
from numpy import mean

with open("data/movies.json") as fh:
    movies = json.load(fh)

# print(parse("$.movies[0]").find(movies)[0].value)

# liste = [m.value for m in parse("$.movies[0]").find(movies)]
# print(liste)

# liste = [m.value for m in parse("$.movies[0].*").find(movies)]
# print(liste)

# liste = [m.value for m in parse("$.movies[*]").find(movies)]
# print(liste)

# liste = [m.value for m in parse("$.movies").find(movies)]
# print(liste)

# liste = [m.value for m in parse("$.movies[?(@.year > 1995)]").find(movies)]
# print(liste)

# liste = [m.value for m in parse("$.movies[?(@.title =~'Kill.*')]").find(movies)]
# print(liste)

# liste = [m.value for m in parse("$.movies[?(@.cast[*] = 'Uma Thurman')]").find(movies)]
# print(liste)

# liste = [m.value for m in parse("$.movies[?(@.cast[*] = 'Uma Thurman' & @.year > 2000)]").find(movies)]
# print(liste)

movie_age = 2023-mean([m.value for m in parse("$..year").find(movies)])
print(movie_age)
